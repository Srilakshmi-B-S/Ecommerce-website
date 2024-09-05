
from django.shortcuts import render,get_object_or_404, redirect
from .models import Product,Delivery
from .forms import DeliveryForm

def product_list(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request,'index2.html', {'product': product})

def delivery_details(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.product = product
            delivery.save()
            return redirect('payment', delivery_id=delivery.id)
    else:
        form = DeliveryForm()
    return render(request, 'delivery_details.html', {'form': form, 'product': product})


def payment(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    if request.method == 'POST':
        # Handle payment details here
        payment_method = request.POST.get('payment_method')
        payment_reference = request.POST.get('payment_reference')
        # Assume payment is successful
        delivery.payment_status = 'Completed'
        delivery.payment_method = payment_method
        delivery.payment_reference = payment_reference
        delivery.save()
        return redirect('confirmation', delivery_id=delivery.id)
    return render(request, 'payment.html', {'delivery': delivery})

def confirmation(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    return render(request, 'confirmation.html', {'delivery': delivery})

def home(request):
    return render(request, 'home.html')