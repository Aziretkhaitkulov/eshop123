# Generated by Django 5.1b1 on 2024-07-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField(default=0)),
            ],
        ),
    ]