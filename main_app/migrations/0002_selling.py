# Generated by Django 4.0.6 on 2022-07-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.IntegerField(choices=[('H', 'High'), ('M', 'Mid'), ('L', 'Low')], default='H', max_length=1)),
            ],
        ),
    ]
