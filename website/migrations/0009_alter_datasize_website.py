# Generated by Django 5.0.1 on 2024-01-24 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_datasize_received_data_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasize',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='website.site'),
        ),
    ]
