# Generated by Django 4.2.11 on 2024-03-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_learning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='note_images/'),
        ),
    ]
