from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from records.models import Record

# Create your views here.

# 3. Таблица должна иметь сортировку по всем полям кроме даты.

# class RecordView(ListView):
#     model = Record
#     template_name = 'table.html'
#
#     def get_context_data(self, **kwargs):
#         qs = Record.objects.all()
#         context = super().get_context_data(**kwargs)
#         title_contains_query = self.request.GET.get('search_field')
#         if title_contains_query != '' and title_contains_query is not None:
#             qs = qs.filter(title__icontains=title_contains_query)
#         context['queryset'] = qs
#         return context


def filter_view(request):

    qs = Record.objects.all()
    chosen_field = request.GET.get('select_field')
    chosen_option = request.GET.get('select_filter')
    search_query = request.GET.get('search_field')

    if search_query != '' and search_query is not None:
        if chosen_option != '' and chosen_option is not None:
            if chosen_field == 'title':
                qs = Record.objects.filter_title(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'quantity':
                qs = Record.objects.filter_quantity(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'distance':
                try:
                    qs = Record.objects.filter_distance(search_query=search_query, chosen_option=chosen_option)
                except ValidationError:
                    return HttpResponse(f'<h1 style="color:red" align="center">ERROR: distance value must not contain symbols like ","</h1>')

        else:
            qs = None

    context = {
        'queryset': qs,

    }
    return render(request, 'table.html', context)




