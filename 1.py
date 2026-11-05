def filter_valid_numbers_unoptimised(numbers, allowed):
    valid_numbers = []
    for num in numbers:
        if num in allowed:
            valid_numbers.append(num)
    return valid_numbers

numbers = list(range(10000))
allowed = list(range(5000, 10000))
filtered_numbers = filter_valid_numbers_unoptimised(numbers, allowed)
print(filtered_numbers[:10])