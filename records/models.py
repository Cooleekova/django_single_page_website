
from django.db import models

# Create your models here.


class RecordQuerySet(models.QuerySet):

    def filter_title(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(title__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(title__iexact=search_query)
        else:
            return self.none()

    def filter_quantity(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(quantity__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(quantity__iexact=search_query)
        elif chosen_option == 'more than':
            return self.filter(quantity__gte=search_query)
        elif chosen_option == 'less than':
            return self.filter(quantity__lte=search_query)
        else:
            return self.none()

    def filter_distance(self, chosen_option, search_query):
        if chosen_option == 'contains':
            return self.filter(distance__icontains=search_query)
        elif chosen_option == 'equals to':
            return self.filter(distance__iexact=search_query)
        elif chosen_option == 'more than':
            return self.filter(distance__gte=search_query)
        elif chosen_option == 'less than':
            return self.filter(distance__lte=search_query)
        else:
            return self.none()


class Record(models.Model):

    date = models.DateField(
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

    objects = RecordQuerySet.as_manager()

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title

