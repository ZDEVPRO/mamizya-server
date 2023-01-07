from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rang'
        verbose_name_plural = 'Ranglar'


class Size(models.Model):
    title = models.CharField(max_length=600)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "O'lcham"
        verbose_name_plural = "O'lchamlar"


class Product(models.Model):
    CATEGORY = (
        ('man', 'Erkaklar uchun'),
        ('woman', 'Ayollar uchun'),
        ('kids', 'Bolalar uchun'),
        ('shoes', 'Oyoq kiyimlar')
    )

    title = models.CharField(max_length=400)
    category = models.CharField(max_length=600, choices=CATEGORY)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    content = RichTextField()
    additional_description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'


class ImageItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.title


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_title = models.CharField(max_length=600)
    product_price = models.CharField(max_length=600)
    amount = models.IntegerField()
    size = models.CharField(max_length=600)
    color = models.CharField(max_length=600)
    phone = models.CharField(max_length=600)
    address = models.TextField()
    ip = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class Contact(models.Model):
    first_name = models.CharField(max_length=600)
    last_name = models.CharField(max_length=600)
    phone = models.CharField(max_length=600)
    message = models.TextField()
    ip = models.CharField(max_length=600)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Aloqa bo'limi"
        verbose_name_plural = "Aloqa bo'limi"
