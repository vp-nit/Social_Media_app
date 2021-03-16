# Generated by Django 3.1.7 on 2021-03-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210307_0731'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profiles.Profile'),
        ),
    ]