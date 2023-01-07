# Generated by Django 4.1.4 on 2023-01-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='fullname',
            new_name='color',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(default='1', max_length=600),
            preserve_default=False,
        ),
    ]