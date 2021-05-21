# Generated by Django 3.2.2 on 2021-05-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
                ('month', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
            ],
        ),
    ]
