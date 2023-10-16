# Generated by Django 3.2.22 on 2023-10-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20231011_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatLifeguard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('cat_quantity', models.PositiveSmallIntegerField()),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]