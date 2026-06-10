from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem, Cart, CartItem
from .forms import CustomUserCreationForm

def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# --- Корзина (через БД) ---

@login_required(login_url='/login/')
def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return cart

@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required(login_url='/login/')
def remove_from_cart(request, product_id):
    cart = get_cart(request)
    CartItem.objects.filter(cart=cart, product_id=product_id).delete()
    return redirect('cart_detail')

@login_required(login_url='/login/')
def cart_detail(request):
    cart = get_cart(request)
    cart_items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # Чтобы шаблон не сломался (если он ожидает price и quantity)
    # мы передаем cart_items напрямую (у них есть item.product, item.quantity)
    # но в шаблоне может потребоваться вызов item.product.price * item.quantity 
    # В шаблоне мы это поправим
    
    return render(request, 'store/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

# --- Оформление заказа ---

@login_required(login_url='/login/')
def checkout(request):
    cart = get_cart(request)
    cart_items = cart.items.all()
    if not cart_items:
        return redirect('product_list')
        
    if request.method == 'POST':
        delivery_address = request.POST.get('delivery_address')
        order = Order.objects.create(
            user=request.user,
            delivery_address=delivery_address,
            total_price=0
        )
        total = 0
        for item in cart_items:
            price = item.product.price * item.quantity
            total += price
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        order.total_price = total
        order.save()
        
        # Очищаем корзину
        cart.items.all().delete()
        return redirect('order_history')
        
    return render(request, 'store/checkout.html')

@login_required(login_url='/login/')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

# --- Авторизация ---

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('product_list')
