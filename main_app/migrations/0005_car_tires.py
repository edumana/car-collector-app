# Generated by Django 4.1.3 on 2022-11-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_color_tires_hardness'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tires',
            field=models.ManyToManyField(to='main_app.tires'),
        ),
    ]