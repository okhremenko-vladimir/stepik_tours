from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError

from tours.data import departures, tours


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request, tour_id):
    title = tours[tour_id]['title'] + ' ' + '★' * int(tours[tour_id]['stars'])
    from_city = departures[tours[tour_id]['departure']]
    info = '{} {} {} ночей'.format(tours[tour_id]['country'], from_city, tours[tour_id]['nights'])
    about = tours[tour_id]['description']
    price = tours[tour_id]['price']
    link_picture = tours[tour_id]['picture']
    context = {'title': title, 'info': info, 'about': about,
               'price': price, 'link_picture': link_picture}
    return render(request, 'tours/tour.html', context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
