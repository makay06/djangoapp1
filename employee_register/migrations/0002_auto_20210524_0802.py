# Generated by Django 3.1.2 on 2021-05-24 08:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='ex',
            field=models.CharField(default='12', max_length=115),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=115),
        ),
    ]
