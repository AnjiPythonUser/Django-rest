# Generated by Django 5.0.2 on 2024-02-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=60)),
                ('mark', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('price_usd', models.IntegerField()),
            ],
        ),
    ]
