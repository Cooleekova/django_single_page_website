from django.urls import path
from records.views import filter_view\
    # RecordView,

app_name = 'records'

urlpatterns = [
    # path('', RecordView.as_view(template_name='table.html'), name='table'),
    path('', filter_view, name='table'),
]
