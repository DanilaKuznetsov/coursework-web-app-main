import os
import django
import urllib.request
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from store.models import Category, Product

Category.objects.all().delete()
Product.objects.all().delete()

c1 = Category.objects.create(name='Смартфоны', slug='smartphones', description='Современные телефоны для связи и развлечений')
c2 = Category.objects.create(name='Ноутбуки', slug='laptops', description='Мощные ноутбуки для работы и игр')
c3 = Category.objects.create(name='Аксессуары', slug='accessories', description='Чехлы, кабели, наушники')

def create_product(category, name, desc, price, stock, specs, img_url):
    p = Product(
        category=category,
        name=name,
        description=desc,
        price=price,
        stock=stock,
        specifications=specs
    )
    if img_url:
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            filename = img_url.split('?')[0].split('/')[-1] + '.jpg'
            p.image.save(filename, ContentFile(response.read()), save=False)
        except Exception as e:
            print(f"Failed to load image for {name}: {e}")
    p.save()

create_product(
    c1, 
    'iPhone 15 Pro', 
    'Флагманский смартфон с титановым корпусом и отличной камерой.', 
    115000.00, 
    10, 
    'Память: 256GB, Экран: OLED 6.1"',
    'https://images.unsplash.com/photo-1695048133142-1a20484d2569?q=80&w=600&auto=format&fit=crop'
)

create_product(
    c1, 
    'Samsung Galaxy S24 Ultra', 
    'Топовый смартфон на Android со стилусом и нейросетями.', 
    125000.00, 
    7, 
    'Память: 512GB, Экран: AMOLED 6.8"',
    'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?q=80&w=600&auto=format&fit=crop'
)

create_product(
    c2, 
    'MacBook Air M2', 
    'Легкий, тонкий и очень быстрый ноутбук.', 
    135000.00, 
    5, 
    'ОЗУ: 8GB, SSD: 256GB, Процессор: M2',
    'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=600&auto=format&fit=crop'
)

create_product(
    c2, 
    'ASUS ROG Strix G15', 
    'Мощный игровой ноутбук с подсветкой и отличным охлаждением.', 
    145000.00, 
    3, 
    'ОЗУ: 16GB, SSD: 1TB, Видеокарта: RTX 3060',
    'https://images.unsplash.com/photo-1593640408182-31c70c8268f5?q=80&w=600&auto=format&fit=crop'
)

create_product(
    c3, 
    'AirPods Pro 2', 
    'Беспроводные наушники с активным шумоподавлением.', 
    26000.00, 
    20, 
    'Интерфейс: Bluetooth 5.3, Автономность: 6ч',
    'https://images.unsplash.com/photo-1588423771073-b8903fbb85b5?q=80&w=600&auto=format&fit=crop'
)

create_product(
    c3, 
    'Зарядное устройство 20W', 
    'Блок питания для быстрой зарядки телефона.', 
    2500.00, 
    50, 
    'Мощность: 20W, Разъем: USB-C',
    'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=600&auto=format&fit=crop'
)

print("Тестовые данные (категории и товары) успешно загружены в базу!")
