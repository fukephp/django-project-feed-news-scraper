# Generated by Django 3.2.6 on 2021-08-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApi', '0003_auto_20210808_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
