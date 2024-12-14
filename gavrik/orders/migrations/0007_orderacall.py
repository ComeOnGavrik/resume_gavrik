# Generated by Django 5.1.3 on 2024-12-13 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderACall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('subscriber_phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='status_call', to='orders.status')),
            ],
            options={
                'verbose_name': 'Заказ звонка',
                'verbose_name_plural': 'Заказ звонков',
            },
        ),
    ]
