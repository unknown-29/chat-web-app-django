# Generated by Django 4.1.7 on 2023-03-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatDb', '0008_dummy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummy',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]