# Generated by Django 2.2 on 2019-05-17 05:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20190516_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pred_date_rdy',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 5, 55, 18, 310363, tzinfo=utc), verbose_name='Предварительная дата готовности'),
        ),
    ]
