# Generated by Django 3.1.dev20200327073858 on 2020-05-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
