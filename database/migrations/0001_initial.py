# Generated by Django 4.2 on 2023-04-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('difficulty', models.CharField(max_length=21)),
                ('role', models.CharField(max_length=21)),
                ('image', models.TextField()),
            ],
        ),
    ]
