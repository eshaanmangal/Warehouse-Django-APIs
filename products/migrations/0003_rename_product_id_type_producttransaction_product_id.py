# Generated by Django 4.0 on 2022-07-04 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_category_id_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttransaction',
            old_name='product_id_type',
            new_name='product_id',
        ),
    ]