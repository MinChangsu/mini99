# Generated by Django 4.1.5 on 2023-01-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_info_a"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="encoder_l",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="info",
            name="encoder_r",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
