from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from records.models import Record, Film
from . import filters

# Create your views here.


# from django.views.generic import ListView


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
                    return HttpResponse(
                        f'<h1 style="color:red" align="center">'
                        f'ERROR: distance value must not contain symbols like ","</h1>'
                    )

        else:
            qs = None

    context = {
        'queryset': qs,
    }
    return render(request, 'table.html', context)


def film_view(request):

    qs = Film.objects.all()

    chosen_field = request.GET.get('select_field')
    chosen_option = request.GET.get('select_filter')
    search_query = request.GET.get('search_field')
    ordering = request.GET.get('ordering')

    if search_query != '' and search_query is not None:
        if chosen_option != '' and chosen_option is not None:
            if chosen_field == 'title':
                qs = Film.objects.filter_title(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'subject':
                qs = Film.objects.filter_subject(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'actor':
                qs = Film.objects.filter_actor(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'actress':
                qs = Film.objects.filter_actress(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'director':
                qs = Film.objects.filter_director(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'year':
                qs = Film.objects.filter_year(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'length':
                qs = Film.objects.filter_length(search_query=search_query, chosen_option=chosen_option)
            if chosen_field == 'popularity':
                qs = Film.objects.filter_popularity(search_query=search_query, chosen_option=chosen_option)
        else:
            qs = None


    if ordering != '' and ordering is not None and ordering != 'Order by...':
        qs = qs.order_by(ordering)


    paginator = Paginator(qs, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    print(request.get_full_path)

    context = {
        'queryset': page.object_list,
        'ordering': ordering,
        'select_field': chosen_field,
        'select_filter': chosen_option,
        'search_field': search_query,
        'page': page,

    }
    return render(request, 'films_table.html', context)



def filter_film_view(request):

    filtered_qs = filters.FilmFilter(
        request.GET,
        queryset=Film.objects.all()
    ).qs
    paginator = Paginator(filtered_qs, 8)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(
        request,
        'filtered_films_table.html',
        {'response': response}
    )


def film_list_view(request):
    f = filters.FilmFilter(request.GET)
    paginator = Paginator(f.qs, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request, 'films_list.html', {'filter': f, 'page': page})

