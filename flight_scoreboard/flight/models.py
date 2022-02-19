# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Flight(models.Model):
    STATUS = (
        (None, 'Выберите статус'),
        ('v', 'Вылетел'),
        ('p', 'Приземлился'),
        ('i', 'Идет посадка'),
        ('z ', 'Задержан'),

    )

    number = models.TextField(verbose_name='Номер рейса')
    departure_city = models.ForeignKey('City', verbose_name='Город вылета', related_name='input_flights')
    arrival_city = models.ForeignKey('City', verbose_name='Город прибытия', related_name='output_flights')
    plane_type = models.ForeignKey('Airbus', verbose_name='Тип самолета')
    planned_departure_time = models.DateTimeField(verbose_name='Плановая дата и время вылета')
    planned_arrival_time = models.DateTimeField(verbose_name='Плановая дата и время прилета')
    actual_departure_time = models.DateTimeField(null=True, blank=True, verbose_name='Фактическая дата и время вылета',
                                                 default=None)
    actual_arrival_time = models.DateTimeField(null=True, blank=True, verbose_name='Фактическая дата и время прилета',
                                               default=None)
    status = models.CharField(max_length=100, choices=STATUS, verbose_name='Статус рейса')

    class Meta:
        verbose_name_plural = 'Рейсы'
        verbose_name = 'Рейс'
        ordering = ['planned_departure_time']

    def __str__(self):
        return "%s %s %s" %(self.number, self.departure_city.name, self.arrival_city.name)


@python_2_unicode_compatible
class City(models.Model):
    name = models.TextField(verbose_name='Город')

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Airbus(models.Model):
    type_plane = models.TextField(verbose_name='Тип самолета')

    class Meta:
        verbose_name_plural = 'Типы самолетов'
        verbose_name = 'Тип самолета'

    def __str__(self):
        return self.type_plane
