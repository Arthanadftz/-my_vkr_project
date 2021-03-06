# Generated by Django 2.2 on 2019-05-17 05:57

import attendance_control.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='title',
        ),
        migrations.AddField(
            model_name='attendance',
            name='group',
            field=models.CharField(choices=[('ИУ1', 'ИУ-1'), ('ИУ2', 'ИУ-2'), ('ИУ3', 'ИУ-3'), ('ИУ4', 'ИУ-4'), ('ИУ5', 'ИУ-5'), ('ИУ6', 'ИУ-6'), ('ИУ7', 'ИУ-7'), ('ИУ8', 'ИУ-8')], default='ИУ6', max_length=3, verbose_name='Группа студента'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/attendance/%Y%m%D/', validators=[attendance_control.models.validate_file_extension], verbose_name='Файл'),
        ),
        migrations.CreateModel(
            name='Disciple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название предмета')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='disciple',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance_control.Disciple', verbose_name='Дисциплина'),
        ),
    ]
