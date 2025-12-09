from question_a import create_multiplication_table, display_multiplication_table
def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        choice = input("\nDo you want to run again? (y/n): ").lower()
        if choice != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()