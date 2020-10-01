# Generated by Django 3.0.3 on 2020-10-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('author', models.CharField(default='Неизвестный', max_length=250, verbose_name='Автор')),
                ('date_of_issue', models.DateField(blank=True, null=True, verbose_name='Дата выпуска')),
                ('count_of_pages', models.IntegerField(default=0, verbose_name='Количество страниц')),
                ('price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('date_of_issue', models.DateField(blank=True, null=True, verbose_name='Дата выпуска')),
                ('timing', models.FloatField(default=0, verbose_name='Длительность (в минутах)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('date_of_issue', models.DateField(blank=True, null=True, verbose_name='Дата выпуска')),
                ('timing', models.FloatField(default=0, verbose_name='Длительность (в секундах)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Музыкальный трек',
                'verbose_name_plural': 'Музыкальные треки',
            },
        ),
    ]