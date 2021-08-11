def translate (i: int) -> str: 
    if i in numbers: 
        return numbers[i] 
    else: 
        combined_letter = numbers[int(str(i)[1])]+numbers[int(str(i)[0])*10]
        return combined_letter

numbers = {
    1: "één",
    2: "twee",
    3: "drie",
    4: "vier",
    5: "vijf",
    6: "zes",
    7: "zeven",
    8: "acht",
    9: "negen",
    10: "tien",
    11: "elf",
    12: "twaalf",
    13: "dertien",
    14: "veertien",  
}

# test driven development: 
# - write a test - resulting red test 
# - Change the code minimally to get all test green
# - Do again