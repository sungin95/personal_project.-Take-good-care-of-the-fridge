# Generated by Django 3.2.13 on 2022-10-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_recipe',
            name='ingredients',
            field=models.TextField(),
        ),
    ]
