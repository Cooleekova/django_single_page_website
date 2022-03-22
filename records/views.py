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

    if chosen_field == 'title':
        if search_query != '' and search_query is not None:
            if chosen_option == 'contains':
                qs = qs.filter(title__icontains=search_query)
            elif chosen_option == 'equals to':
                qs = qs.filter(title__iexact=search_query)
        else:
            qs = None

    if chosen_field == 'quantity':
        if search_query != '' and search_query is not None:
            if chosen_option == 'contains':
                qs = qs.filter(quantity__icontains=search_query)
            elif chosen_option == 'equals to':
                qs = qs.filter(quantity__iexact=search_query)
            elif chosen_option == 'more than':
                qs = qs.filter(quantity__gte=search_query)
            elif chosen_option == 'less than':
                qs = qs.filter(quantity__lte=search_query)

    if chosen_field == 'distance':
        if search_query != '' and search_query is not None:
            if chosen_option == 'contains':
                qs = qs.filter(distance__icontains=search_query)
            elif chosen_option == 'equals to':
                qs = qs.filter(distance__iexact=search_query)
            elif chosen_option == 'more than':
                qs = qs.filter(distance__gte=search_query)
            elif chosen_option == 'less than':
                qs = qs.filter(distance__lte=search_query)

    context = {
        'queryset': qs,

    }
    return render(request, 'table.html', context)




