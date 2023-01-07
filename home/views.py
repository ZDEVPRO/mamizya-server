import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import *
from site_settings.models import *
from django.core.paginator import Paginator


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    return render(request, 'home.html')


def shop(request):
    products = Product.objects.all().order_by('-id')
    p = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    count = products.count()
    if request.method == 'POST':
        category = request.POST.get('category')
        if category == 'all':
            return redirect('shop')
        else:
            return redirect('filter', category)

    context = {
        'products': products,
        'count': count,
        'page_obj': page_obj
    }
    return render(request, 'shop.html', context)


def about(request):
    about_data = About.objects.last()
    context = {
        'about': about_data
    }

    return render(request, 'about.html', context)


def contact(request):
    contact_data = ContactData.objects.last()

    if request.method == 'POST':
        data = Contact()
        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')
        data.phone = request.POST.get('phone')
        data.message = request.POST.get('message')
        data.ip = get_client_ip(request)
        data.save()
        messages.success(request, 'Xabaringiz muvoffaqiyatli yetkazildi! Sizga qisqa muddat ichida aloqaga chiqamiz!')

        text = f'🇺🇿 YANGI XABAR KELDI! 🇺🇿 \n' \
               f'\n 👨  FISH: {data.first_name} {data.last_name}' \
               f'\n 📲  Telefon raqam: {data.phone}' \
               f'\n 🌐  IP RAQAM: {data.ip}' \
               f'\n 🕒  VAQT: {data.create_at.strftime("%H:%M")}' \
               f'\n 📆  SANA: {data.create_at.strftime("%d-%m-%Y")}' \
               f'\n 📩  XABAR: {data.message}'
        text1 = "".join(text)

        bot_token = '5260192605:AAEGRPGEAyN-g6ygFy-pvZNFsgZk9eQu6Gc'
        bot_chatID = '1255807110'

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

        response = requests.get(url)

    context = {
        'contact': contact_data
    }

    return render(request, 'contact.html', context)


def shop_detail(request, id):
    product = Product.objects.get(id=id)
    images = ImageItem.objects.filter(product__id=id)
    sizes = product.size.all()
    colors = product.color.all()

    if request.method == 'POST':
        amount = request.POST.get('amount')
        print(amount)

    context = {
        'product': product,
        'images': images,
        'sizes': sizes,
        'colors': colors
    }

    return render(request, 'shop_detail.html', context)


def buy_product(request, id):
    product = Product.objects.get(id=id)
    sizes = product.size.all()
    colors = product.color.all()

    if request.method == 'POST':
        data = Order()
        data.product = product
        data.product_title = product.title
        data.product_price = product.price
        data.amount = request.POST.get('amount')
        data.size = request.POST.get('product_size')
        data.color = request.POST.get('product_color')
        data.phone = request.POST.get('phone')
        data.address = request.POST.get('address')
        data.ip = get_client_ip(request)
        data.save()
        messages.success(request,
                         "So'rovingiz qabul qilindi! Tez orada sizga qo'ng'iroq qilamiz. Xaridingiz uchun raxmat")

        text = f'🇺🇿 YANGI BUYURTMA! \n' \
               f'\n 🛒 Maxsulot: {data.product.title}' \
               f'\n 📱 Telefon: {data.phone}' \
               f'\n 🏫 Manzil: {data.address}' \
               f'\n 🕒  VAQT: {data.create_at.strftime("%H:%M")}' \
               f'\n 📆  SANA: {data.create_at.strftime("%d-%m-%Y")}'
        text1 = "".join(text)

        bot_token = '5260192605:AAEGRPGEAyN-g6ygFy-pvZNFsgZk9eQu6Gc'
        bot_chatID = '1255807110'

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

        requests.get(url)

    context = {
        'product': product,
        'sizes': sizes,
        'colors': colors
    }
    return render(request, 'buy_product.html', context)


def filter_view(request, category):
    products = Product.objects.filter(category=category).order_by('-id')
    p = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    count = products.count()
    context = {
        'products': products,
        'category': category,
        'page_obj': page_obj,
        'count': count
    }
    return render(request, 'filter.html', context)


def search_view(request):
    try:
        if request.method == 'GET':
            keywords = request.GET.get('keywords')
            result = Product.objects.filter(title__icontains=keywords)

            context = {
                'result': result
            }
            return render(request, 'search.html', context)
    except Exception as e:
        print(e)
