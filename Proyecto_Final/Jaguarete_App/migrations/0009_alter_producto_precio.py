# Generated by Django 3.2.4 on 2021-07-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jaguarete_App', '0008_delete_carrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
