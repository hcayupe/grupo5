# Generated by Django 3.1.2 on 2020-10-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarW', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderGaleria',
            fields=[
                ('ident', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('slider1', models.ImageField(null=True, upload_to='car')),
                ('slider2', models.ImageField(null=True, upload_to='car')),
            ],
        ),
    ]
