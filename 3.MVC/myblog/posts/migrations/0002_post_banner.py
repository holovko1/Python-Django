# Generated by Django 5.1.3 on 2024-11-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
