# Generated by Django 3.1.2 on 2020-11-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201107_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]
