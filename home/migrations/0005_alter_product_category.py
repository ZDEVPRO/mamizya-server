# Generated by Django 4.1.4 on 2023-01-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('man', 'Erkaklar uchun'), ('woman', 'Ayollar uchun'), ('kids', 'Bolalar uchun'), ('shoes', 'Oyoq kiyimlar')], max_length=600),
        ),
    ]
