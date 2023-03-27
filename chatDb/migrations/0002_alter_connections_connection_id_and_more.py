# Generated by Django 4.1.7 on 2023-03-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatDb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connections',
            name='connection_id',
            field=models.CharField(auto_created=True, max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
