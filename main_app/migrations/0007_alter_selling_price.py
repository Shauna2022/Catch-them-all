# Generated by Django 4.0.6 on 2022-07-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_selling_options_selling_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selling',
            name='price',
            field=models.IntegerField(choices=[('H', 'High'), ('M', 'Mid'), ('L', 'Low')], default='H'),
        ),
    ]
