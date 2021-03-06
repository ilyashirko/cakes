from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from .helpers import check_payment, create_payment
from .models import (
    Berry,
    Customer,
    Decoration,
    Delivery,
    Form,
    Level,
    Order,
    Promo,
    Topping,
    Utm
)

def save_and_pay_order(request):
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
        user=request.user
    )
    customer.mailbox = request.GET['EMAIL']
    customer.first_name = request.GET['NAME']
    customer.phonenumber = request.GET['PHONE']
    customer.save()

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

    try:
        promo = Promo.objects.get(title=request.GET.get("PROMO"))
    except Promo.DoesNotExist:
        promo = None
    if promo and promo.is_valid:
        promo_cost = cost - promo.number
    else:
        promo_cost = cost
    payment = create_payment(
        promo_cost,
        request.build_absolute_uri('/accounts/profile/')
    )
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
        promo=promo,
        promo_cost=promo_cost,
        utm=utm,
        payment_id=payment['id']
    )
    return payment['url']


def index(request):
    if 'utm_source' in request.GET:
        request.session["utm_source"] = request.GET["utm_source"]
        request.session["utm_medium"] = request.GET["utm_medium"]
        request.session["utm_campaign"] = request.GET["utm_campaign"]
        request.session["utm_content"] = request.GET.get("utm_content")
        request.session["utm_term"] = request.GET.get("utm_term")

    if 'LEVELS' in request.GET and request.user.is_authenticated:
        payment_url = save_and_pay_order(request)
        return redirect(payment_url)
    if 'LEVELS' in request.GET and not request.user.is_authenticated:
        request.session['order'] = request.GET
        return redirect('login')
        
    context = {}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def lk(request):
    if 'order' in request.session:
        request.GET = request.session['order']
        del request.session['order']
        payment_url = save_and_pay_order(request)
        return redirect(payment_url)

    if 'EMAIL' in request.GET:
        customer, _ = Customer.objects.get_or_create(
            user=request.user
        )
        customer.mailbox = request.GET['EMAIL']
        customer.first_name = request.GET['NAME']
        customer.phonenumber = request.GET['PHONE']
        customer.save()
    user = request.user
    try:
        for order in Order.objects.filter(
            customer=user.customer,
            payment_status=False
        ):
            if check_payment(order.payment_id):
                order.payment_status = True
                order.save()
    except ObjectDoesNotExist:
        pass
    context = {}
    return render(request, 'lk.html', context)
