# Generated by Django 3.2.5 on 2021-07-16 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='last_updated',
            new_name='last_name',
        ),
    ]
