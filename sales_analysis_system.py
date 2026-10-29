def record_sales():
    sales = []
    print("Enter sales for 7 days")
    for i in range(1, 8):
        amount = float(input(f"Day {i} Sales:"))
        sales.append(amount)
    return sales


def calculate_total(sales_list):
    total = 0
    for sale in sales_list:
        total += sale
    return total


def calculate_average(sales_list):
    total = calculate_total(sales_list)
    average = total / len(sales_list)
    return average


def find_highest_lowest(sales_list):
    highest = sales_list[0]
    lowest = sales_list[0]
    for sale in sales_list:
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
    return highest, lowest


def show_report():
    daily_sales = record_sales()
    total = calculate_total(daily_sales)
    average = calculate_average(daily_sales)
    highest, lowest = find_highest_lowest(daily_sales)

    print("\n---Sales Analysis Report---")
    print(f"Daily Sales: {daily_sales}")
    print(f"Total Weekly Sales: {total}")
    print(f"Average Daily Sales: {average:.2f}")
    print(f"Highest sale: {highest}")
    print(f"Lowest sale: {lowest}")


if __name__ == "__main__":
    show_report()
