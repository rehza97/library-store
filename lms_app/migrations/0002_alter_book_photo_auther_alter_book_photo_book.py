# Generated by Django 4.1.7 on 2023-02-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo_auther',
            field=models.ImageField(blank=True, null=True, upload_to='auther'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover'),
        ),
    ]
