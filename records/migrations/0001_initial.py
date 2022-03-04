# Generated by Django 3.2.12 on 2022-03-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Расстояние')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
