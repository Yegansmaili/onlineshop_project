# Generated by Django 5.0.3 on 2024-05-22 19:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=3, null=True),
        ),
    ]
