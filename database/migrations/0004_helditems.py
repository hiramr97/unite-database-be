# Generated by Django 4.2 on 2023-05-01 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_builds'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeldItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('image', models.TextField()),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='held_items', to='database.builds')),
            ],
        ),
    ]
