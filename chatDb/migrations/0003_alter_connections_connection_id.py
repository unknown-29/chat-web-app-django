# Generated by Django 4.1.7 on 2023-03-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatDb', '0002_alter_connections_connection_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connections',
            name='connection_id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]