# Generated by Django 2.1.7 on 2020-04-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20200420_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningpro',
            name='url',
            field=models.URLField(blank=True, default='', null=True, verbose_name='远程桌面链接'),
        ),
    ]
