# Generated by Django 2.2.4 on 2019-09-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190902_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
    ]
