# Generated by Django 4.1.4 on 2023-01-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0005_contactdata_instagram_contactdata_telegram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='working_time',
            field=models.CharField(default='1', max_length=10000),
            preserve_default=False,
        ),
    ]
