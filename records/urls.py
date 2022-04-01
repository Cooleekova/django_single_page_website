from django.urls import path
from records.views import filter_view, film_view, film_list_view \
    # RecordView,

app_name = 'records'

urlpatterns = [
    # path('', RecordView.as_view(template_name='table.html'), name='table'),
    path('', film_view, name='films_table'),
    path('table', filter_view, name='table'),
    path('filter', film_list_view, name='films-list'),

]
