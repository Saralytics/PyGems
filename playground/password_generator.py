import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['@', '#', '$', '%', '&', '(', ')', '*', '+', '!']

# Ask user preference of password
print("Let's generate a secure password for you!")
len_total = int(input("How long do you want your password to be?"))
nbr_digits = int(input("How many digits do you want in your password?"))
nbr_letters = int(input("How many letters do you want in your password?"))
# the rest will be symbols
nbr_symbols = len_total - nbr_digits - nbr_letters

# Create a pool of candidates to fill in the password

# randomly pick from digits nbr_digits
digit_candidates = []
for i in range(nbr_digits):
    idx = random.randint(0, len(digits) - 1)
    digit_candidates.append(digits[idx])

# randomly pick from letters nbr_letters
letter_candidates = []
for i in range(nbr_letters):
    idx = random.randint(0, len(letters) - 1)
    letter_candidates.append(letters[idx])

# randomly pick from symbols nbr_symbols
symbols_candidates = []
for i in range(nbr_symbols):
    idx = random.randint(0, len(symbols) - 1)
    symbols_candidates.append(symbols[idx])

candidates = []
candidates.extend(digit_candidates)
candidates.extend(letter_candidates)
candidates.extend(symbols_candidates)

# replace the placeholders of password at random index

random.shuffle(candidates)
password = ''.join(candidates)

print(f"Here is your password: {password}")
