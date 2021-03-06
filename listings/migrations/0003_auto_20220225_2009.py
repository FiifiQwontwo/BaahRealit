# Generated by Django 3.2.11 on 2022-02-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_furnished_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='furnished_state',
            field=models.CharField(blank=True, choices=[('FF', 'Fully Furnished'), ('SF', 'Semi Furnished'), ('NF', 'Not Furnished')], max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='square_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
