# Generated by Django 4.2.7 on 2023-11-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputSong', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SongRecomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackName', models.CharField(max_length=120)),
                ('artist', models.CharField(max_length=120)),
                ('album', models.CharField(max_length=120)),
            ],
        ),
    ]
