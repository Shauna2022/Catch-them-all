# Generated by Django 4.0.6 on 2022-07-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_cards_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selling',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
