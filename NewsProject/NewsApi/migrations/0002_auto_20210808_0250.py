# Generated by Django 3.2.6 on 2021-08-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]