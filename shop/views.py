from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import get_object_or_404,redirect,render
from django.db.models import Q
from .models import Product,Category,Order,OrderItem,CartItem

def _session_cart(request):
    return request.session.setdefault('cart',{})

def product_list(request):
    products=Product.objects.filter(active=True).select_related('category')
    q=request.GET.get('q','').strip()
    category=request.GET.get('category','').strip()
    if q: products=products.filter(Q(name__icontains=q)|Q(description__icontains=q))
    if category: products=products.filter(category__slug=category)
    return render(request,'shop/product_list.html',{'products':products,'categories':Category.objects.all(),'q':q})

def product_detail(request,pk):
    return render(request,'shop/product_detail.html',{'product':get_object_or_404(Product,pk=pk,active=True)})

def cart_add(request,product_id):
    product=get_object_or_404(Product,pk=product_id,active=True)
    if request.user.is_authenticated:
        item,created=CartItem.objects.get_or_create(user=request.user,product=product)
        if not created: item.quantity+=1
        item.save()
    else:
        cart=_session_cart(request); key=str(product.id); cart[key]=cart.get(key,0)+1; request.session.modified=True
    return redirect('cart_detail')

def cart_remove(request,product_id):
    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user,product_id=product_id).delete()
    else:
        cart=_session_cart(request); cart.pop(str(product_id),None); request.session.modified=True
    return redirect('cart_detail')

def _cart_rows(request):
    if request.user.is_authenticated:
        return [(x.product,x.quantity) for x in CartItem.objects.filter(user=request.user).select_related('product')]
    cart=_session_cart(request); ids=[int(x) for x in cart]
    products={p.id:p for p in Product.objects.filter(id__in=ids)}
    return [(products[i],cart[str(i)]) for i in ids if i in products]

def cart_detail(request):
    rows=_cart_rows(request); total=sum((p.price*q for p,q in rows),Decimal('0'))
    return render(request,'cart/cart_detail.html',{'rows':rows,'total':total})

@transaction.atomic
def checkout(request):
    rows=_cart_rows(request)
    if not rows: return redirect('product_list')
    total=sum((p.price*q for p,q in rows),Decimal('0'))
    if request.method=='POST':
        order=Order.objects.create(user=request.user if request.user.is_authenticated else None,
          full_name=request.POST.get('full_name',''),email=request.POST.get('email',''),
          address=request.POST.get('address',''),city=request.POST.get('city',''),
          postal_code=request.POST.get('postal_code',''),total=total)
        for p,q in rows:
            OrderItem.objects.create(order=order,product=p,product_name=p.name,price=p.price,quantity=q)
        if request.user.is_authenticated: CartItem.objects.filter(user=request.user).delete()
        request.session['cart']={}; messages.success(request,'Order created. Configure Stripe sandbox for payment.')
        return redirect('orders')
    return render(request,'orders/checkout.html',{'rows':rows,'total':total})

@login_required
def orders(request):
    return render(request,'orders/orders.html',{'orders':Order.objects.filter(user=request.user).prefetch_related('items')})

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid(): user=form.save(); login(request,user); return redirect('product_list')
    else: form=UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})

@login_required
def profile(request): return render(request,'accounts/profile.html')
