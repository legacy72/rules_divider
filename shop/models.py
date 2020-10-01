from django.db import models


class Book(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250, blank=False, null=False)
    author = models.CharField(verbose_name='Автор', max_length=250, default='Неизвестный')
    date_of_issue = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    count_of_pages = models.IntegerField(verbose_name='Количество страниц', default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=30, decimal_places=2)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Film(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250, blank=False, null=False)
    date_of_issue = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    timing = models.FloatField(verbose_name='Длительность (в минутах)', default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=30, decimal_places=2)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Music(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250, blank=False, null=False)
    date_of_issue = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    timing = models.FloatField(verbose_name='Длительность (в секундах)', default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=30, decimal_places=2)

    class Meta:
        verbose_name = 'Музыкальный трек'
        verbose_name_plural = 'Музыкальные треки'
