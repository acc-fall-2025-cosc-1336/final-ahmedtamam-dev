from question_b import get_stock_list, display_stock_list


def main():
    while True:
        # Step 1: Get the stock list
        stock_list = get_stock_list()

        # Step 2: Display menu
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        option = input("Enter your choice: ")

        if option == "1":
            display_stock_list(stock_list)
        elif option == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
