# Generated by Django 3.1.dev20200327073858 on 2020-05-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rate',
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
