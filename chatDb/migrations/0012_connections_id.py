# Generated by Django 4.1.7 on 2023-03-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatDb', '0011_alter_userprofilepic_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='connections',
            name='id',
            field=models.IntegerField(null=True),
        ),
    ]
