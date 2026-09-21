from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='main/categories/', verbose_name='фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['-created_at']


class Brand(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'
        ordering = ['-created_at']


class ContactMessage(models.Model):
    name = models.CharField(max_length=60, verbose_name='имя')
    email = models.EmailField(verbose_name='Почта')
    number = models.CharField(max_length=13, verbose_name='номер')
    subject = models.CharField(verbose_name='Тема', max_length=150)
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'Сообщение контактной формы'
        verbose_name_plural = 'Сообщения контактной формы'



class Product(models.Model):
    class ProductStatus(models.TextChoices):
        NEW = 'new', 'Новинка'
        SALE = 'sale', 'Распродажа'
        SOLD = 'sold', 'Продано'

    title = models.CharField(max_length=100, verbose_name='Название', unique=True)
    short_description = models.TextField(max_length=200, verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    preview = models.ImageField(upload_to='main/products/previews/', null=True, blank=True, verbose_name='Фото')
    status = models.CharField(max_length=20, choices=ProductStatus.choices, default=ProductStatus.NEW,
                              verbose_name='Статус')
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=3)
    quantity = models.PositiveBigIntegerField(default=10, verbose_name='Кол-во в наличии')
    additional = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name='Категории')
    tag = models.ManyToManyField(Tag, verbose_name='Теги')
    brand = models.ManyToManyField(Brand, verbose_name='Бренды')
    sku = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(verbose_name='дата создания')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'продукты'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='images')
    image = models.ImageField(verbose_name='Фото', upload_to='main/products/photos/')

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фотки продукта'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='comments')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user_comments')
    review = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Комментарий продукта'
        verbose_name_plural = 'Комментарии продукта'


class HomeSlider(models.Model):
    image = models.ImageField(upload_to='home-page/slider/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото слайдера'
        verbose_name_plural = 'Фотки слайдера'








