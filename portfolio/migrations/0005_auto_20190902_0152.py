# Generated by Django 2.2.4 on 2019-09-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20190902_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='info',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección web'),
        ),
    ]
