# Generated by Django 4.1.4 on 2023-01-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_contact_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageitem',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
