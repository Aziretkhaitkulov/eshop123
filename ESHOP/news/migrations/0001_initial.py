# Generated by Django 5.1b1 on 2024-07-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('article', models.TextField()),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
