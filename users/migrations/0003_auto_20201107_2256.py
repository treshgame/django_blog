# Generated by Django 3.1.2 on 2020-11-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201107_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/avatar.jpg', upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]