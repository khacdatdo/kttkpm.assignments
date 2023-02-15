# Generated by Django 4.1.7 on 2023-02-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=20)),
                ('load_currency', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
