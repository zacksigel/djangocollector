# Generated by Django 4.2 on 2023-04-13 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_film_director_film_genre_film_release_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='screening date')),
                ('theater', models.CharField(choices=[('P', 'Pantheon'), ('W', "World's Theater"), ('R', 'Regal Cinemas')], default='P', max_length=1, verbose_name='theater')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.film')),
            ],
        ),
    ]
