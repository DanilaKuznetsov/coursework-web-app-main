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
c4 = Category.objects.create(name='Планшеты', slug='tablets', description='Удобные планшеты для учебы и медиа')
c5 = Category.objects.create(name='Умные часы', slug='smartwatches', description='Гаджеты для спорта и уведомлений')

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
            print(f"Loaded image for {name}")
        except Exception as e:
            print(f"Failed to load image for {name}: {e}")
    p.save()

products = [
    (c1, 'iPhone 15 Pro', 'Флагманский смартфон с титановым корпусом.', 115000, 10, 'Память: 256GB', 'https://images.unsplash.com/photo-1695048133142-1a20484d2569?q=80&w=600&auto=format&fit=crop'),
    (c1, 'Samsung Galaxy S24 Ultra', 'Топовый смартфон на Android.', 125000, 7, 'Память: 512GB', 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?q=80&w=600&auto=format&fit=crop'),
    (c1, 'Google Pixel 8 Pro', 'Смартфон с лучшей камерой для фото.', 90000, 5, 'Память: 128GB', 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=600&auto=format&fit=crop'),
    (c1, 'Xiaomi 14 Pro', 'Быстрый смартфон с отличным экраном.', 80000, 12, 'Память: 256GB', 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=600&auto=format&fit=crop'),
    (c1, 'iPhone 13', 'Проверенная временем классика.', 60000, 20, 'Память: 128GB', 'https://images.unsplash.com/photo-1605236453806-6ff36851218e?q=80&w=600&auto=format&fit=crop'),
    (c1, 'Poco F5', 'Игровой смартфон среднего бюджета.', 35000, 15, 'Память: 256GB', 'https://images.unsplash.com/photo-1533228100845-08145b01de14?q=80&w=600&auto=format&fit=crop'),
    
    (c2, 'MacBook Air M2', 'Легкий и очень быстрый ноутбук.', 135000, 5, 'ОЗУ: 8GB, SSD: 256GB', 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=600&auto=format&fit=crop'),
    (c2, 'ASUS ROG Strix G15', 'Мощный игровой ноутбук.', 145000, 3, 'ОЗУ: 16GB, RTX 3060', 'https://images.unsplash.com/photo-1593640408182-31c70c8268f5?q=80&w=600&auto=format&fit=crop'),
    (c2, 'Lenovo Legion 5', 'Отличный выбор для геймеров.', 120000, 8, 'ОЗУ: 16GB, RTX 4060', 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?q=80&w=600&auto=format&fit=crop'),
    (c2, 'Dell XPS 15', 'Премиальный ноутбук для работы.', 180000, 2, 'ОЗУ: 32GB, OLED экран', 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=600&auto=format&fit=crop'),
    
    (c3, 'AirPods Pro 2', 'Беспроводные наушники с шумоподавлением.', 26000, 20, 'Bluetooth 5.3', 'https://images.unsplash.com/photo-1588423771073-b8903fbb85b5?q=80&w=600&auto=format&fit=crop'),
    (c3, 'Зарядное устройство 20W', 'Блок питания для быстрой зарядки.', 2500, 50, 'Мощность: 20W', 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=600&auto=format&fit=crop'),
    (c3, 'Чехол Silicone Case', 'Защитный чехол для смартфона.', 1500, 100, 'Материал: Силикон', 'https://images.unsplash.com/photo-1603313011101-320f26a4f6f6?q=80&w=600&auto=format&fit=crop'),
    (c3, 'Кабель USB-C', 'Плетеный кабель зарядки.', 1000, 80, 'Длина: 1 метр', 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=600&auto=format&fit=crop'),
    (c3, 'Sony WH-1000XM5', 'Полноразмерные премиум наушники.', 35000, 10, 'Hi-Res Audio', 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?q=80&w=600&auto=format&fit=crop'),
    
    (c4, 'iPad Pro 11"', 'Мощный планшет на чипе M2.', 85000, 6, 'Память: 256GB', 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?q=80&w=600&auto=format&fit=crop'),
    (c4, 'Samsung Galaxy Tab S9', 'Лучший Android планшет.', 80000, 4, 'AMOLED дисплей', 'https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?q=80&w=600&auto=format&fit=crop'),
    (c4, 'Xiaomi Pad 6', 'Отличный планшет по соотношению цены и качества.', 35000, 15, '144 Гц экран', 'https://images.unsplash.com/photo-1622543925917-763c34d1a86e?q=80&w=600&auto=format&fit=crop'),
    
    (c5, 'Apple Watch Series 9', 'Самые популярные смарт-часы.', 45000, 8, 'Размер: 45мм', 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?q=80&w=600&auto=format&fit=crop'),
    (c5, 'Samsung Galaxy Watch 6', 'Умные часы для экосистемы Samsung.', 30000, 10, 'Измерение ЭКГ', 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?q=80&w=600&auto=format&fit=crop'),
    (c5, 'Garmin Fenix 7', 'Часы для профессиональных спортсменов.', 75000, 3, 'GPS, Автономность: 20 дней', 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=600&auto=format&fit=crop'),
]

for p in products:
    create_product(*p)

print(f"Тестовые данные: загружено {Category.objects.count()} категорий и {Product.objects.count()} товаров!")
