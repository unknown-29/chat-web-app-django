# Generated by Django 4.1.7 on 2023-03-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatDb', '0004_dummy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dummy',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='static/images/default.jpg', upload_to='static/images'),
        ),
    ]
