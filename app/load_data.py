import os
import django

# Настраиваем окружение Django для скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from store.models import Category, Product

# Очищаем старые данные (по желанию, чтобы не дублировать)
Category.objects.all().delete()
Product.objects.all().delete()

# Создаем категории
c1 = Category.objects.create(name='Смартфоны', description='Современные телефоны для связи и развлечений')
c2 = Category.objects.create(name='Ноутбуки', description='Мощные ноутбуки для работы и игр')
c3 = Category.objects.create(name='Аксессуары', description='Чехлы, кабели, наушники')

# Создаем товары
Product.objects.create(
    category=c1, 
    name='iPhone 15 Pro', 
    description='Флагманский смартфон с титановым корпусом и отличной камерой.', 
    price=115000.00, 
    stock=10, 
    image_url='https://images.unsplash.com/photo-1695048133142-1a20484d2569?q=80&w=600&auto=format&fit=crop'
)

Product.objects.create(
    category=c1, 
    name='Samsung Galaxy S24 Ultra', 
    description='Топовый смартфон на Android со стилусом и нейросетями.', 
    price=125000.00, 
    stock=7, 
    image_url='https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?q=80&w=600&auto=format&fit=crop'
)

Product.objects.create(
    category=c2, 
    name='MacBook Air M2', 
    description='Легкий, тонкий и очень быстрый ноутбук.', 
    price=135000.00, 
    stock=5, 
    image_url='https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=600&auto=format&fit=crop'
)

Product.objects.create(
    category=c2, 
    name='ASUS ROG Strix G15', 
    description='Мощный игровой ноутбук с подсветкой и отличным охлаждением.', 
    price=145000.00, 
    stock=3, 
    image_url='https://images.unsplash.com/photo-1593640408182-31c70c8268f5?q=80&w=600&auto=format&fit=crop'
)

Product.objects.create(
    category=c3, 
    name='AirPods Pro 2', 
    description='Беспроводные наушники с активным шумоподавлением.', 
    price=26000.00, 
    stock=20, 
    image_url='https://images.unsplash.com/photo-1588423771073-b8903fbb85b5?q=80&w=600&auto=format&fit=crop'
)

Product.objects.create(
    category=c3, 
    name='Зарядное устройство 20W', 
    description='Блок питания для быстрой зарядки телефона.', 
    price=2500.00, 
    stock=50, 
    image_url='https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=600&auto=format&fit=crop'
)

print("Тестовые данные (категории и товары) успешно загружены в базу!")
