# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(numbers):
    # Ensure the input is a list f 10 digits
    if len(numbers) != 10 or any(not isinstance(n, int) or n < 0 or n > 9 for n in numbers):
        raise ValueError("Input must be a list of 10 integers between 0 and 9.")
    
    area_code = ''.join(map(str, numbers[:3]))
    first_part = ''.join(map(str, numbers[3:6]))
    second_part = ''.join(map(str, numbers[6:]))

    return f"({area_code}) {first_part}={second_part}"