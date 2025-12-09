def create_multiplication_table():
    table = []  # a - empty list

    # b - nested loop for rows 1–10
    for row in range(1, 6):  # based on your example (1–5)
        row_list = []
        for col in range(1, 11):  # columns 1–10
            row_list.append(row * col)
        table.append(row_list)

    return table  # c - return the list


def display_multiplication_table(table):
    # Loop through the list and print rows
    for row in table:
        for val in row:
            print(f"{val:4}", end="")  # formatting for alignment
        print()  # new line after each row

def test_config():
    return True