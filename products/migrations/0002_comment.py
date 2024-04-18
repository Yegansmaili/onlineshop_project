# Generated by Django 5.0.3 on 2024-04-11 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.basemodel')),
                ('text', models.TextField()),
                ('stars', models.CharField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Very Good')], max_length=10)),
                ('commented_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_comments', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('products.basemodel',),
        ),
    ]