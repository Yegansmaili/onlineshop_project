# Generated by Django 5.0.3 on 2024-04-10 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.basemodel')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('unavailable', 'Out of stock'), ('new', 'new'), ('preparing', 'preparing'), ('charged', 'charged'), ('Limited', 'Limited')], default='available', max_length=15, null=True)),
            ],
            bases=('products.basemodel',),
        ),
    ]
