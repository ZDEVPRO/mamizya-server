# Generated by Django 4.1.4 on 2023-01-06 23:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_contact_alter_color_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]