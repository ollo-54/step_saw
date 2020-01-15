import json


class Data:
    def __init__(self):
        with open("data.json", "r") as data_file:
            self.data = json.load(data_file)

    def get_tours(self, departure):
        filtered_tours = []
        for tour in self.data["tours"]:
            if tour["departure"] == departure:
                filtered_tours.append(tour)
        return filtered_tours

    def get_tour_prices(self, departure):
        tours = self.get_tours(departure)
        tour_prices = []
        for tour in tours:
            tour_prices.append(tour['price'])
        return tour_prices

    def print_data(self):
        print(self.data)
