# Generated by Django 4.0.6 on 2022-07-13 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_cards_user_alter_selling_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='user',
        ),
    ]
