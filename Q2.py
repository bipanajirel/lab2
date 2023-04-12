def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(e)

def calculate_species(start_count, percentage_increase, days):
    count = start_count
    print("Day Approximate          Population")
    for i in range(1, days + 1):
        print(f"{i:2d}                         {count:.2f}")
        count *= (1 + percentage_increase / 100)

starting_count = get_positive_input(" Starting number of organisms: ")
average_increase = get_positive_input("Average daily percentage increase: ")
num_days = int(get_positive_input("Enter the number of days to display the final data: "))

calculate_species(starting_count, average_increase, num_days)