import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Next word: ").strip().upper()

decoded = [alphabet_dict.get(letter) for letter in word]


print(decoded)
