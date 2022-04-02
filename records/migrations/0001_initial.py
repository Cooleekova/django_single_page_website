# Generated by Django 3.2.12 on 2022-04-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Длина')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('subject', models.CharField(max_length=100, verbose_name='Жанр')),
                ('actor', models.CharField(max_length=100, verbose_name='Актёр')),
                ('actress', models.CharField(max_length=100, verbose_name='Актриса')),
                ('director', models.CharField(max_length=100, verbose_name='Режиссёр')),
                ('popularity', models.IntegerField(blank=True, null=True, verbose_name='Популярность')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['-popularity'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Расстояние')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['date'],
            },
        ),
    ]
