from datetime import datetime

from django.shortcuts import render

from .models import Berry, Customer, Decoration, Delivery, Form, Order, Topping


def index(request):
    if request.GET:
        delivery, _ = Delivery.objects.get_or_create(
            address=request.GET["ADDRESS"],
            datetime=datetime.strptime(
                f'{request.GET["DATE"]}{request.GET["TIME"]}',
                "%Y-%m-%d%H:%M"
            ),
            comment=request.GET.get("DELIVCOMMENTS")
        )

        customer, _ = Customer.objects.get_or_create(
                first_name=request.GET["NAME"],
                phonenumber=request.GET["PHONE"],
                mailbox=request.GET["EMAIL"]
            )

        berries, decoration = None, None

        if request.GET.get("BERRIES"):
            berries = Berry.objects.get(num=request.GET["BERRIES"])
        if request.GET.get("DECOR"):
            decoration = Decoration.objects.get(num=request.GET["DECOR"])

        Order.objects.create(
            levels=request.GET["LEVELS"],
            form=Form.objects.get(num=request.GET["FORM"]),
            topping=Topping.objects.get(num=request.GET["TOPPING"]),
            berries=berries,
            decoration=decoration,
            signature=request.GET.get("WORDS"),
            comment=request.GET.get("COMMENTS"),
            customer=customer,
            delivery=delivery
        )

    some_data = {

    }
    context = {
        'DATA': some_data
    }
    return render(request, 'index.html', context)


def lk(request):

    context = {

    }
    return render(request, 'index.html', context)
