# Generated by Django 3.2.6 on 2021-08-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApi', '0004_auto_20210808_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='article',
            name='symbol',
        ),
    ]
