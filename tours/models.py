class ResultsDirection:
    def __init__(self, tours):
        self.len_tours = len(tours)
        self.tours = tours

    def __str__(self):
        min_price = min(self.tours, key=lambda x: x['price'])
        min_price = '{:,}'.format(min_price['price']).replace(',', ' ')
        max_price = max(self.tours, key=lambda x: x['price'])
        max_price = '{:,}'.format(max_price['price']).replace(',', ' ')
        min_night = min(self.tours, key=lambda x: x['nights'])['nights']
        max_night = max(self.tours, key=lambda x: x['nights'])['nights']
        results = f'Найдено {self.len_tours} туров, от {min_price} до {max_price} и от {min_night} до {max_night} ночей'
        return results


def add_stars(title, stars, int_star=False, country=''):
    if country:
        country = country + ': '
    if int_star:
        return country + title + '  ' + stars + '★'
    return country + title + ' ' + '★' * int(stars)
