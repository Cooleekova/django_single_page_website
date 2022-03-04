
from django.db import models

# Create your models here.


class Record(models.Model):

    date = models.DateTimeField(
        auto_now_add=False,
        verbose_name='Дата',
    )

    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )

    quantity = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Количество'
    )

    distance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name='Расстояние'
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title

