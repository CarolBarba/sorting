def sort_numbers(numbers, ascending=True):
    numbers.sort()
    if not ascending:
        numbers.reverse()
    return numbers

# Example usage
numbers = [5, 1, 4, 3, 2]
print("Ascending:", sort_numbers(numbers))
print("Descending:", sort_numbers(numbers, False))
