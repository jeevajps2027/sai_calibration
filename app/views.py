import json
from django.http import JsonResponse
from django.shortcuts import render


def login(request):
    return render(request,"app/login.html")

def index(request):
    return render(request,"app/index.html")


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Customer, EngineerManagerDetails, SettingPlugMaster, SettingPlugTrace, SettingRingMaster, SettingRingTrace


@csrf_exempt
def master(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            form_type = data.get('formType')
            form_data = data.get('formData')

            print("form_type",form_type)
            print("form_data",form_data)
            
            if form_type == 'customer':
                # Save customer data to the Customer model
                customer = Customer.objects.create(
                    customer_name=form_data['customer_name'],
                    primary_contact_person=form_data['primary_contact_person'],
                    secondary_contact_person=form_data['secondary_contact_person'],
                    primary_email=form_data['primary_email'],
                    secondary_email=form_data['secondary_email'],
                    primary_phone_no=form_data['primary_phone_no'],
                    secondary_phone_no=form_data['secondary_phone_no'],
                    gst_no=form_data['gst_no'],
                    dept=form_data['dept'],
                    address=form_data['address']
                )
                customer.save()

            elif form_type == 'setting_plug_trace':
                # Save or update setting_plug_trace table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        # Update existing record
                        obj = SettingPlugTrace.objects.get(id=row_id)
                        obj.master_name = row['masterName']
                        obj.id_no = row['idNo']
                        obj.calibration_report_no = row['calibrationReportNo']
                        obj.valid_upto = row['validUpto']
                        obj.traceability = row['traceability']
                        obj.save()
                    else:
                        # Create new record
                        SettingPlugTrace.objects.create(
                            master_name=row['masterName'],
                            id_no=row['idNo'],
                            calibration_report_no=row['calibrationReportNo'],
                            valid_upto=row['validUpto'],
                            traceability=row['traceability']
                        )

            elif form_type == 'setting_ring_trace':
                # Save or update setting_ring_trace table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = SettingRingTrace.objects.get(id=row_id)
                        obj.master_name = row['masterName']
                        obj.id_no = row['idNo']
                        obj.calibration_report_no = row['calibrationReportNo']
                        obj.valid_upto = row['validUpto']
                        obj.traceability = row['traceability']
                        obj.save()
                    else:
                        SettingRingTrace.objects.create(
                            master_name=row['masterName'],
                            id_no=row['idNo'],
                            calibration_report_no=row['calibrationReportNo'],
                            valid_upto=row['validUpto'],
                            traceability=row['traceability']
                        )

            elif form_type == 'setting_plug_master':
                # Save or update setting_plug_master table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = SettingPlugMaster.objects.get(id=row_id)
                        obj.parameter_name = row['parameterName']
                        obj.ref_size = row['refSize']
                        obj.nominal = row['nominal']
                        obj.save()
                    else:
                        SettingPlugMaster.objects.create(
                            parameter_name=row['parameterName'],
                            ref_size=row['refSize'],
                            nominal=row['nominal']
                        )

            elif form_type == 'setting_ring_master':
                # Save or update setting_ring_master table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = SettingRingMaster.objects.get(id=row_id)
                        obj.parameter_name = row['parameterName']
                        obj.ref_size = row['refSize']
                        obj.nominal = row['nominal']
                        obj.save()
                    else:
                        SettingRingMaster.objects.create(
                            parameter_name=row['parameterName'],
                            ref_size=row['refSize'],
                            nominal=row['nominal']
                        )

            elif form_type == 'engineer_manager_details':
                # Save or update engineer_manager_details table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = EngineerManagerDetails.objects.get(id=row_id)
                        obj.calib_engineer = row['calibEngineer']
                        obj.quality_manager = row['qualityManager']
                        obj.certificate_no = row['certificateNo']
                        obj.save()
                    else:
                        EngineerManagerDetails.objects.create(
                            calib_engineer=row['calibEngineer'],
                            quality_manager=row['qualityManager'],
                            certificate_no=row['certificateNo']
                        )

            return JsonResponse({'status': 'success', 'message': 'Data saved successfully.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
    elif request.method == 'GET':
        customer_value = Customer.objects.all()
        SettingPlugTrace_value = SettingPlugTrace.objects.all()
        SettingRingTrace_value = SettingRingTrace.objects.all()
        SettingPlugMaster_value = SettingPlugMaster.objects.all()
        SettingRingMaster_value = SettingRingMaster.objects.all()
        EngineerManagerDetails_value = EngineerManagerDetails.objects.all()

        context ={
            'customer_value': customer_value, 
            'SettingPlugTrace_value': SettingPlugTrace_value,
            'SettingRingTrace_value': SettingRingTrace_value,
            'SettingPlugMaster_value' : SettingPlugMaster_value,
            'SettingRingMaster_value' : SettingRingMaster_value,
            'EngineerManagerDetails_value' : EngineerManagerDetails_value
        }

    elif request.method == 'DELETE':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            form_type = data.get('formType')
            ids_to_delete = data.get('idsToDelete', [])

            if form_type == 'tableBody-1':
                # Delete setting_plug_trace records
                SettingPlugTrace.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-2':
                # Delete setting_ring_trace records
                SettingRingTrace.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-3':
                # Delete setting_plug_master records
                SettingPlugMaster.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-4':
                # Delete setting_ring_master records
                SettingRingMaster.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-5':
                # Delete engineer_manager_details records
                EngineerManagerDetails.objects.filter(id__in=ids_to_delete).delete()

            else:
                return JsonResponse({'error': 'Invalid form type'}, status=400)

            return JsonResponse({'success': True, 'message': 'Data deleted successfully'})

        except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)

   
    
    return render(request,"app/master.html",context)





def calib(request):
    if request.method == 'GET':
        customer_value = Customer.objects.all()
        SettingPlugTrace_value = SettingPlugTrace.objects.all()
        SettingRingTrace_value = SettingRingTrace.objects.all()
        SettingPlugMaster_value = SettingPlugMaster.objects.all()
        SettingRingMaster_value = SettingRingMaster.objects.all()
        EngineerManagerDetails_value = EngineerManagerDetails.objects.all()

    context ={
            'customer_value': customer_value, 
            'SettingPlugTrace_value': SettingPlugTrace_value,
            'SettingRingTrace_value': SettingRingTrace_value,
            'SettingPlugMaster_value' : SettingPlugMaster_value,
            'SettingRingMaster_value' : SettingRingMaster_value,
            'EngineerManagerDetails_value' : EngineerManagerDetails_value
        }
    return render(request,"app/calib.html",context)

def output(request):
    if request.method == 'GET':
        SettingPlugTrace_value = SettingPlugTrace.objects.all()
        SettingRingTrace_value = SettingRingTrace.objects.all()
        SettingPlugMaster_value = SettingPlugMaster.objects.all()
        SettingRingMaster_value = SettingRingMaster.objects.all()

    context ={
            'SettingPlugTrace_value': SettingPlugTrace_value,
            'SettingRingTrace_value': SettingRingTrace_value,
            'SettingPlugMaster_value' : SettingPlugMaster_value,
            'SettingRingMaster_value' : SettingRingMaster_value,
        }
    return render(request,"app/output.html",context)

import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import WorkOrder, Customer  # Ensure WorkOrderItem is imported if needed

from django.db import IntegrityError

def inward(request):
    if request.method == 'POST':
        # Check if we are fetching work orders based on customer name
        customer_name = request.POST.get('customer_name')
        if customer_name:
            work_orders = WorkOrder.objects.filter(customer_name=customer_name).distinct().values('work_order_no')
            work_order_list = list(work_orders)
            return JsonResponse(work_order_list, safe=False)

        # Handle normal workflow to create or update a work order
        try:
            data = json.loads(request.body)

            # Extract main form data
            customer_name = data.get('customerName')
            wo_date = data.get('woDate')
            work_order_no = data.get('workOrderNo')
            customer_po_no = data.get('customerPoNo')
            customer_ref_date = data.get('customerRefDate')
            order_type = data.get('orderType')
            customer_address = data.get('customerAddress')

            if not all([customer_name, wo_date, work_order_no]):
                return JsonResponse({'error': 'Missing required fields.'}, status=400)

            items = data.get('items', [])
            saved_items = []
            skipped_items = []

            for item in items:
                if item.get('item'):
                    # Check if the item already exists in the database
                    exists = WorkOrder.objects.filter(
                        customer_name=customer_name,
                        work_order_no=work_order_no,
                        item=item.get('item'),
                        hsn=item.get('hsn'),
                        sr_no=item.get('srNo')
                    ).exists()

                    if not exists:
                        work_order = WorkOrder.objects.create(
                            customer_name=customer_name,
                            wo_date=wo_date,
                            work_order_no=work_order_no,
                            customer_po_no=customer_po_no,
                            customer_ref_date=customer_ref_date,
                            order_type=order_type,
                            customer_address=customer_address,
                            item=item.get('item'),
                            hsn=item.get('hsn'),
                            sr_no=item.get('srNo'),
                            id_no=item.get('idNo'),
                            range=item.get('range'),
                            make=item.get('make')
                        )
                        saved_items.append(work_order.id)
                    else:
                        skipped_items.append(item)

            return JsonResponse({
                'message': 'Work order processed successfully!',
                'saved_items': saved_items,
                'skipped_items': skipped_items
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)



    elif request.method == 'GET':
        # Check if we are fetching work order details based on work order number
        work_order_no = request.GET.get('work_order_no')  # Fetch work order number from GET request

        if work_order_no:  # If work order number is provided, fetch related data
            try:
                # Fetch all work orders with the provided work order number
                work_orders = WorkOrder.objects.filter(work_order_no=work_order_no)

                if not work_orders.exists():
                    return JsonResponse({'success': False, 'error': 'Work order not found.'})

                # Prepare response data
                data = {
                    'success': True,
                    'wo_date': work_orders.first().wo_date,  # Assuming wo_date is the same for all items
                    'customer_po_no': work_orders.first().customer_po_no,
                    'customer_ref_date': work_orders.first().customer_ref_date,
                    'order_type': work_orders.first().order_type,
                    'customer_address': work_orders.first().customer_address,
                    'items': []
                }

                # Loop through each work order item and append it to the items list
                for work_order in work_orders:
                    data['items'].append({
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

        # Fetch all Customer objects to pass them to the template for normal GET requests
        customer_value = Customer.objects.all()

        # Render the form with the customer data
        context = {
            'customer_value': customer_value,
        }
        return render(request, "app/inward.html", context)
    
    elif request.method == 'DELETE':
        try:
            # Parse the request body to get the work order ID
            data = json.loads(request.body)
            work_order_id = data.get('work_order_id')

            if not work_order_id:
                return JsonResponse({'success': False, 'error': 'Missing work order ID.'}, status=400)

            print("Attempting to delete work order with ID:", work_order_id)  # Debug print

            # Find and delete the work order
            work_order = WorkOrder.objects.get(id_no=work_order_id)
            work_order.delete()

            return JsonResponse({'success': True, 'message': 'Work order deleted successfully!'})

        except WorkOrder.DoesNotExist:
            print("Work order not found with ID:", work_order_id)  # Debug print
            return JsonResponse({'success': False, 'error': 'Work order not found.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            print("Error during deletion:", e)  # Debug print
            return JsonResponse({'success': False, 'error': str(e)}, status=500)



    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)

