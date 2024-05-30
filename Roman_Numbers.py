def is_valid_roman(roman):
    # Validating Roman numbers
    import re
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if not re.match(pattern, roman):
        return False
    return True

def roman_to_int(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    i = 0
    num = 0
    while i < len(roman):
        # Check for two-character numerals first (IV, IX, etc.)
        if i+1 < len(roman) and roman[i:i+2] in roman_values:
            num += roman_values[roman[i:i+2]]
            i += 2
        else:
            num += roman_values[roman[i]]
            i += 1
    return num

def main():
    while True:
        roman = input("Enter a Roman numeral: ").upper()
        if is_valid_roman(roman):
            number = roman_to_int(roman)
            print(f"The integer value of the Roman numeral {roman} is {number}.")
            break
        else:
            print("Invalid Roman numeral. Please try again.")

if __name__ == "__main__":
    main()
