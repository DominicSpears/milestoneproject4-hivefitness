# Generated by Django 3.2.7 on 2021-09-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.SlugField(max_length=254),
        ),
    ]
