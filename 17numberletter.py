letters_dict = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

def num_letters(integer):
    if integer == 1000:
        return 11
    
    global letters_dict
    need_and = 0

    hundreds = int(integer / 100)
    tens = int((integer % 100)/ 10) * 10
    ones = integer % 10
    if integer >= 100 and integer % 100 != 0:
        need_and = 3

    if tens == 10:
        tens_and_ones_letters = letters_dict[integer % 100]
    else:
        tens_and_ones_letters = letters_dict[tens] + letters_dict[ones]

    if integer < 100:
        return tens_and_ones_letters
    if integer >= 100:
        return letters_dict[hundreds] + 7 + need_and + tens_and_ones_letters

total_letters = 0
for i in range(1,1001):
    total_letters += num_letters(i)

print(total_letters)
