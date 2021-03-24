# Generated by Django 3.1.7 on 2021-03-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_task', '0002_auto_20210319_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(blank=True, default=0, max_length=50, verbose_name='select group'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, default=0, max_length=50, verbose_name='User nickname'),
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]
