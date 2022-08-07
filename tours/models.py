class ResultsDirection:
    def __init__(self, tours):
        self.len_tours = len(tours)
        self.tours = tours

    def __str__(self):
        min_price = min(self.tours, key=lambda x: x['price'])
        mn_price = '{:,}'.format(min_price['price']).replace(',', ' ')
        max_price = max(self.tours, key=lambda x: x['price'])
        mx_price = '{:,}'.format(max_price['price']).replace(',', ' ')
        mn_night = min(self.tours, key=lambda x: x['nights'])['nights']
        mx_night = max(self.tours, key=lambda x: x['nights'])['nights']
        tour_ru = 'туров'
        if self.len_tours % 10 == 1 and self.len_tours % 100 != 11:
            tour_ru = 'тур'
        elif 2 <= self.len_tours % 10 <= 4 and (self.len_tours % 100 < 10 or self.len_tours % 100 >= 20):
            tour_ru = 'тура'
        results = f'Найдено {self.len_tours} {tour_ru}, от {mn_price} до {mx_price} и от {mn_night} до {mx_night} ночей'
        return results


def add_stars(title, stars, int_star=False, country=''):
    if country:
        country = country + ': '
    if int_star:
        return country + title + '  ' + stars + '★'
    return country + title + ' ' + '★' * int(stars)
