# Generated by Django 4.0.3 on 2022-04-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=23, upload_to='gallery'),
            preserve_default=False,
        ),
    ]