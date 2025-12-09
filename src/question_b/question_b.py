class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol            # private attribute
        self.__company_name = company_name  # private attribute

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    """Creates and returns a list of Stock objects."""
    stock_data = [
        ("AAPL", "Apple Inc"),
        ("CAT", "Caterpillar"),
        ("EK", "Eastman Kodak"),
        ("GOOG", "Google"),
        ("MSFT", "Microsoft")
    ]

    stock_list = []

    for symbol, company in stock_data:
        stock_list.append(Stock(symbol, company))

    return stock_list


def display_stock_list(stock_list):
    print("\nStock Report")
    print("Company              Symbol")
    print("--------------------------------")

    for stock in stock_list:
        print(f"{stock.get_company_name():20} {stock.get_symbol()}")
        