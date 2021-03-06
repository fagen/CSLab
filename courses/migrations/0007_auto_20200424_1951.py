# Generated by Django 2.1.7 on 2020-04-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200424_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docimage',
            name='local_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='本地镜像路径'),
        ),
        migrations.AlterField(
            model_name='docimage',
            name='remote_url',
            field=models.URLField(blank=True, default='', null=True, verbose_name='镜像地址'),
        ),
    ]
