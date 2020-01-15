from data_handler import Data

def test_smth():
    data = Data()
    data.print_data()
    msk_tours = data.get_tours(departure="msk")
    print(msk_tours)
    print(len(msk_tours))
    print(f"Min msk prices: {min(data.get_tour_prices(departure='msk'))}")
    print(f"Max msk prices: {max(data.get_tour_prices(departure='msk'))}")
