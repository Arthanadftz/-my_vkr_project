# Generated by Django 2.2 on 2019-04-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190427_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_role',
            field=models.CharField(choices=[('СТ', 'Студент'), ('УЧ', 'Учитель')], default='СТ', max_length=2, verbose_name='Роль пользователя'),
        ),
    ]
