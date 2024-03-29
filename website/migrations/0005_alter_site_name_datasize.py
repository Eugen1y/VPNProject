# Generated by Django 5.0.1 on 2024-01-24 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_site_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='DataSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_data_size', models.DecimalField(decimal_places=2, max_digits=20)),
                ('received_data', models.DecimalField(decimal_places=2, max_digits=20)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.site')),
            ],
        ),
    ]
