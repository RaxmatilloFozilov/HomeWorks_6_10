# Generated by Django 5.0.3 on 2024-03-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('view', models.CharField(max_length=100)),
                ('template', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]