from django.urls import path
from records.views import RecordView

app_name = 'records'

urlpatterns = [
    path('table/', RecordView.as_view(template_name='table.html'), name='table'),
]
