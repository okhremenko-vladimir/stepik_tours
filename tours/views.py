from random import sample

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from tours.data import departures, description, tours, subtitle
from tours.models import add_stars, ResultsDirection


def main_view(request):
    random_six_tour = sample(range(1, len(tours) + 1), 6)
    contents = []
    for tour_id in random_six_tour:
        title = add_stars(tours[tour_id]['title'], tours[tour_id]['stars'], False, tours[tour_id]['country'])
        contents.append({'tour_id': tour_id,
                         'link_picture': tours[tour_id]['picture'],
                         'title': title,
                         'about': tours[tour_id]['description']})
    context = {'subtitle': subtitle,
               'description': description,
               'contents': contents,
               'departures': departures,
               'page_title': 'Stepik Travel'}
    return render(request, 'tours/index.html', context)


def departure_view(request, departure):
    page_title = departures[departure] + ': Stepik Travel'
    tours_departure = []
    for tour_id, tour in tours.items():
        if tour['departure'] == departure:
            title = add_stars(tours[tour_id]['title'], tours[tour_id]['stars'], True)
            tours_departure.append({'tour_id': tour_id,
                                    'title': title,
                                    'price': tours[tour_id]['price'],
                                    'about': tours[tour_id]['description'],
                                    'nights': tours[tour_id]['nights'],
                                    'link_picture': tours[tour_id]['picture']})
    results_direction = ResultsDirection(tours_departure)
    context = {"results_direction": results_direction,
               'tours_departure': tours_departure,
               "departure": departures[departure],
               'departures': departures,
               'page_title': page_title}
    return render(request, 'tours/departure.html', context)


def tour_view(request, tour_id):
    title = add_stars(tours[tour_id]['title'], tours[tour_id]['stars'])
    from_city = departures[tours[tour_id]['departure']]
    info = '{} {} {} ночей'.format(tours[tour_id]['country'], from_city, tours[tour_id]['nights'])
    about = tours[tour_id]['description']
    price = '{:,}'.format(tours[tour_id]['price']).replace(',', ' ')
    link_picture = tours[tour_id]['picture']
    page_title = tours[tour_id]['title'] + ': Stepik Travel'
    context = {'title': title,
               'info': info,
               'about': about,
               'price': price,
               'link_picture': link_picture,
               'departures': departures,
               'page_title': page_title}
    return render(request, 'tours/tour.html', context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
