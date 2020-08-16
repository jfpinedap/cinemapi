# Generated by Django 2.2.8 on 2020-08-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=225)),
                ('first_name', models.CharField(max_length=225)),
                ('aliases', models.CharField(max_length=225)),
                ('movies_as_actor', models.ManyToManyField(blank=True, related_name='casting', to='movies.Movie')),
                ('movies_as_director', models.ManyToManyField(blank=True, related_name='directors', to='movies.Movie')),
                ('movies_as_producer', models.ManyToManyField(blank=True, related_name='producers', to='movies.Movie')),
            ],
        ),
    ]
