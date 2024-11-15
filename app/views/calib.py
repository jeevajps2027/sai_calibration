
import re
from django.shortcuts import render
from django.http import JsonResponse
from app.models import Customer, EngineerManagerDetails, MainCalibration, SettingPlugMaster, SettingPlugTrace, SettingRingMaster, SettingRingTrace, WorkOrder, CalibrationEquipment, CalibrationResult


def calib(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        if customer_name:
            # Get distinct work order numbers and inward numbers for the customer
            work_orders = WorkOrder.objects.filter(customer_name=customer_name).distinct().values('work_order_no')
            inward_no_list = WorkOrder.objects.filter(customer_name=customer_name).distinct().values_list('inward_no', flat=True)

            # Check if all inward_no values are in MainCalibration
            main_calibration_inward_nos = MainCalibration.objects.values_list('inward_no', flat=True)
            all_inward_in_main_calibration = all(inward_no in main_calibration_inward_nos for inward_no in inward_no_list)

            # If all inward_no are in MainCalibration, do not send work orders
            if all_inward_in_main_calibration:
                return JsonResponse([], safe=False)  # Send an empty response

            # If any inward_no is missing in MainCalibration, send work orders to the frontend
            work_order_list = list(work_orders)
            print("work_order_list", work_order_list)
            return JsonResponse(work_order_list, safe=False)

    elif request.method == 'GET':
        work_order_no = request.GET.get('work_order_no')  # Fetch work order number from GET request
        print("work_order_no",work_order_no)
        inward_no = request.GET.get('inward_no')  # Fetch sr_no from GET request
        print('inward_no',inward_no)
       
        if inward_no:
            try:
                # Fetch the specific item based on sr_no
                work_order = WorkOrder.objects.filter(work_order_no=work_order_no, inward_no=inward_no).first()
                print("work_order",work_order)
                if not work_order:
                    return JsonResponse({'success': False, 'error': 'Item not found.'})

                # Prepare response data for the specific item
                item_data = {
                    'id_no': work_order.id_no,
                    'sr_no': work_order.sr_no,
                    'make': work_order.make,
                    'range': work_order.range,
                    'customer_po_no': work_order.customer_po_no,
                    'customer_ref_date':work_order.customer_ref_date,
                    'inward_no':work_order.inward_no,
                    'inward_date':work_order.wo_date,
                    'channels':work_order.channels,
                    

                }
                print("item_data",item_data)

                return JsonResponse({'success': True, 'item': item_data})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
            

        if work_order_no:
            try:
                # Fetch work orders based on the provided work_order_no
                work_orders = WorkOrder.objects.filter(work_order_no=work_order_no)
                if not work_orders.exists():
                    return JsonResponse({'success': False, 'error': 'Work order not found.'})

                # Get all inward_no values in MainCalibration to filter them out
                main_calibration_inward_nos = MainCalibration.objects.values_list('inward_no', flat=True)
                print("main_calibration_inward_nos ",main_calibration_inward_nos)
                
                # Prepare response data
                data = {
                    'success': True,
                    'wo_date': work_orders.first().wo_date,
                    'customer_po_no': work_orders.first().customer_po_no,
                    'customer_ref_date': work_orders.first().customer_ref_date,
                    'order_type': work_orders.first().order_type,
                    'customer_address': work_orders.first().customer_address,
                    'items': []
                }

                # Filter out work orders with inward_no in main_calibration_inward_nos
                for work_order in work_orders:
                    if work_order.inward_no not in main_calibration_inward_nos:
                        data['items'].append({
                            'inward_no': work_order.inward_no,
                            'item': work_order.item,
                            'hsn': work_order.hsn,
                            'sr_no': work_order.sr_no,
                            'id_no': work_order.id_no,
                            'range': work_order.range,
                            'make': work_order.make
                        })

                return JsonResponse(data)
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})

   
         # Retrieve the latest certificate number
        last_certificate = MainCalibration.objects.order_by('-id').first()
        
        if last_certificate and last_certificate.certificate_num:
            # Extract the number at the end of the certificate number and increment it
            match = re.search(r'(\d+)$', last_certificate.certificate_num)
            if match:
                # Get the numeric part, increment it, and format it with leading zeros
                number = int(match.group(1)) + 1
                new_certificate_num = re.sub(r'(\d+)$', f'{number:03}', last_certificate.certificate_num)
            else:
                new_certificate_num = last_certificate.certificate_num + '001'  # Default if no number found
        else:
            # Default starting certificate number if none exists
            new_certificate_num = 'SAI/CH/24-25/001'
            
        customer_value = Customer.objects.all()
        SettingPlugTrace_value = SettingPlugTrace.objects.all()
        SettingRingTrace_value = SettingRingTrace.objects.all()
        SettingPlugMaster_value = SettingPlugMaster.objects.all()
        SettingRingMaster_value = SettingRingMaster.objects.all()
        EngineerManagerDetails_value = EngineerManagerDetails.objects.all()
        # MainCalibration_value = MainCalibration.objects.all()
        # CalibrationEquipment_value = CalibrationEquipment.objects.all()
        # CalibrationResult_value = CalibrationResult.objects.all()
      

    context ={
            'customer_value': customer_value, 
            'SettingPlugTrace_value': SettingPlugTrace_value,
            'SettingRingTrace_value': SettingRingTrace_value,
            'SettingPlugMaster_value' : SettingPlugMaster_value,
            'SettingRingMaster_value' : SettingRingMaster_value,
            'EngineerManagerDetails_value' : EngineerManagerDetails_value,
            'new_certificate_num': new_certificate_num,
        }
    return render(request,"app/calib.html",context)