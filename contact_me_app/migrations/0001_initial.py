# Generated by Django 4.1.3 on 2022-12-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('number', models.CharField(max_length=13)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.URLField(max_length=100)),
                ('instagram', models.URLField(max_length=100)),
                ('github', models.URLField(max_length=100)),
            ],
        ),
    ]
