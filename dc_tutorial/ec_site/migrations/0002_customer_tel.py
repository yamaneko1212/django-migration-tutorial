# Generated by Django 4.1.3 on 2022-11-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tel',
            field=models.CharField(blank=True, max_length=11, verbose_name='電話番号'),
        ),
    ]
