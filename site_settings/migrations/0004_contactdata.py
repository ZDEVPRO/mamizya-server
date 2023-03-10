# Generated by Django 4.1.4 on 2023-01-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_about_big_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(max_length=600)),
                ('phone2', models.CharField(max_length=600)),
                ('email', models.CharField(max_length=600)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Aloqa Malumotlari',
                'verbose_name_plural': 'Aloqa Malumotlari',
            },
        ),
    ]
