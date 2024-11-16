from django.shortcuts import render


def invoice(request):
     return render(request, "app/invoice.html")