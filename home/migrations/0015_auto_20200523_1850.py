# Generated by Django 3.1.dev20200327073858 on 2020-05-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200522_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
