# Generated by Django 2.2 on 2019-05-12 18:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190512_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pred_date_rdy',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 15, 18, 14, 31, 939552, tzinfo=utc), verbose_name='Предварительная дата готовности'),
        ),
    ]
