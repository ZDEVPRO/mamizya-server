# Generated by Django 4.1.4 on 2023-01-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_order_product_price_order_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=600)),
                ('last_name', models.CharField(max_length=600)),
                ('phone', models.CharField(max_length=600)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': "Aloqa bo'limi",
                'verbose_name_plural': "Aloqa bo'limi",
            },
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Rang', 'verbose_name_plural': 'Ranglar'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Buyurtma', 'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Maxsulot', 'verbose_name_plural': 'Maxsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': "O'lcham", 'verbose_name_plural': "O'lchamlar"},
        ),
    ]
