# Generated by Django 2.1.7 on 2020-04-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='static/images/course.jpg', upload_to='courses/%Y/%m', verbose_name='封面图'),
        ),
    ]
