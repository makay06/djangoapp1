# Generated by Django 3.1.2 on 2021-05-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_auto_20210524_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
