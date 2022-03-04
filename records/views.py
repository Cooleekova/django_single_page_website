from django.views.generic import ListView
from records.models import Record

# Create your views here.


class RecordView(ListView):
    model = Record
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        qs = Record.objects.all()
        context = super().get_context_data(**kwargs)
        title_contains_query = self.request.GET.get('title_contains')
        if title_contains_query != '' and title_contains_query is not None:
            qs = qs.filter(title__icontains=title_contains_query)
        context['queryset'] = qs
        return context




