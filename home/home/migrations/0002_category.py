# Generated by Django 3.2.4 on 2021-07-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('rent', models.IntegerField()),
            ],
        ),
    ]
