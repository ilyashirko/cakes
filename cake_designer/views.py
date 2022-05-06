from datetime import datetime
import json

from django.shortcuts import render

from .models import Berry, Customer, Decoration, Delivery, Form, Order, Topping, Utm, Level


def index(request):
    print('-' * 50)
    print(json.dumps(dict(request.session), indent=4, ensure_ascii=False))
    print('-' * 50)
    print(json.dumps(dict(request.GET), indent=4, ensure_ascii=False))
    print(f'{"-" * 50}')
    print(request.__dict__)
    print(f'{"-" * 50}')
    

    if 'utm_source' in request.GET:
        print("UTM WAS HESE")
        request.session["utm_source"] = request.GET["utm_source"]
        request.session["utm_medium"] = request.GET["utm_medium"]
        request.session["utm_campaign"] = request.GET["utm_campaign"]
        request.session["utm_content"] = request.GET.get("utm_content")
        request.session["utm_term"] = request.GET.get("utm_term")

    if 'LEVELS' in request.GET:
        if 'utm_source' in request.session:
            utm, _ = Utm.objects.get_or_create(
                source=request.session["utm_source"],
                medium=request.session["utm_medium"],
                campaign=request.session["utm_campaign"],
                content=request.session["utm_content"],
                term=request.session["utm_term"]
            )
        else:
            utm = None

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

        levels = Level.objects.get(num=request.GET["LEVELS"])
        form = Form.objects.get(num=request.GET["FORM"])
        topping = Topping.objects.get(num=request.GET["TOPPING"])

        cost = levels.cost + form.cost + topping.cost

        berries, decoration = None, None
        if request.GET.get("BERRIES"):
            berries = Berry.objects.get(num=request.GET["BERRIES"])
            cost += berries.cost
        if request.GET.get("DECOR"):
            decoration = Decoration.objects.get(num=request.GET["DECOR"])
            cost += decoration.cost

        Order.objects.create(
            levels=levels,
            form=form,
            topping=topping,
            berries=berries,
            decoration=decoration,
            signature=request.GET.get("WORDS"),
            comment=request.GET.get("COMMENTS"),
            customer=customer,
            delivery=delivery,
            cost=cost,
            utm=utm
        )
        print(f'redirected from: {request.GET.get("redirected_from")}')
    
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
