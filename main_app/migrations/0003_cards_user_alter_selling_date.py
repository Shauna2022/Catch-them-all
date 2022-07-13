# Generated by Django 4.0.6 on 2022-07-13 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_selling'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='selling',
            name='date',
            field=models.DateField(verbose_name='Price range'),
        ),
    ]
