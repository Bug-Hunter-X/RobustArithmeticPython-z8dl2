def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will return 0, which is correct

my_list_with_string = [10,20,"hello",40,50]
average_string = calculate_average(my_list_with_string) #This will throw an error
print(f"The average of a list with a string is: {average_string}")