# Generated by Django 4.1.4 on 2023-01-07 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0004_contactdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='instagram',
            field=models.CharField(default='1', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdata',
            name='telegram',
            field=models.CharField(default='2', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdata',
            name='whatsapp',
            field=models.CharField(default='3', max_length=1000),
            preserve_default=False,
        ),
    ]