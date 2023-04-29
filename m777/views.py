from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
from django.core.mail import send_mail
from abc_mart import settings
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer
# Create your views here.


def index(request):

    if request.method == 'POST':
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1

        else:
            cart_id = {}
            cart_id[product_id] = 1

        request.session['cart'] = cart_id
        print(request.session['cart'])

    cate = Category.objects.all()
    cat_id = request.GET.get('category_id')
    if cat_id:
        pro = Product.objects.filter(category=cat_id)
    else:
        pro = Product.objects.all()
    return render(request, 'home.html', {'cat': cate, 'pro': pro})


def contact(request):
    cate = Category.objects.all()
    return render(request, 'contact.html', {'cat': cate})


def user_registration(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('emailid')
        password = request.POST.get('pwd')
        mobile = request.POST.get('mbl')
        gender = request.POST.get('gender')
        msg = 'WELCOME TO M777'
        subject = 'USER REGISTRATION'
        message = msg
        from_email = settings.EMAIL_HOST_USER
        recipent_list = [email]
        send_mail(subject, message, from_email,
                  recipent_list, fail_silently=True)

        info = Signup(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            mobile_no=mobile,
            gender=gender
        )
        info.save()

        return redirect('home')


def login(request):
    if request.method == 'POST':
        emailb = request.POST.get('email')
        passwordb = request.POST.get('pwd')
        try:
            fetch_info = Signup.objects.get(email=emailb)
            if check_password(passwordb, fetch_info.password):
                request.session['name'] = fetch_info.first_name
                request.session['customer'] = fetch_info.id
                return redirect('home')
                # return HttpResponse('login succesful')
            else:
                return HttpResponse('enter a valid password')
        except:
            return HttpResponse('enter a valid password')


def logout(request):
    request.session.clear()
    return redirect('home')


def cart(request):
    cart_info = request.session['cart'].keys()
    cart_dtls = Product.objects.filter(id__in=cart_info)
    print(cart_info)
    print(list(cart_dtls))
    return render(request, 'cart.html', {'cart_dtls': cart_dtls})


def Checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list(cart.keys()))

        print(customer_id, 56565)

        if not customer_id:
            return HttpResponse('please login')

        for pro in product:
            save_ord_dtls = Order(
                address=address,
                mobile_no=mobile,
                customer=Signup(id=customer_id),
                product=pro,
                quantity=cart.get(str(pro.id)),
                price=pro.price

            )
            save_ord_dtls.save()
            save_ord_history = Order_history(
                address=address,
                mobile_no=mobile,
                customer=Signup(id=customer_id),
                product=pro,
                quantity=cart.get(str(pro.id)),
                price=pro.price

            )
            save_ord_history.save()
        request.session['cart'] = {}
        return redirect('Order_dtls')


def Order_dtls(request):
    customer_id = request.session.get('customer')
    fetch_order = Order.objects.filter(customer=customer_id)
    tp = 0
    for i in fetch_order:
        tp = tp + (i.price*i.quantity)
    # print(list(fetch_order))
    return render(request, 'order.html', {'fetch_order': fetch_order, 'tppp': tp})


def find(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        # if name in
        fnd = Product.objects.filter(Q(pro_name__icontains=name))
        if fnd:
            return render(request, 'search.html', {'fnd': fnd})
    return HttpResponse('result not found')


def clear_table(request):
    Order. objects.all().delete()
    return redirect('home')


def order_history(request):
    customer_id = request.session.get('customer')
    fetch_orde = Order_history.objects.filter(customer=customer_id)
    # date =

    # print(list(fetch_order))
    return render(request, 'order_history.html', {'fetch_order': fetch_orde})


class UserViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = UserSerializer
