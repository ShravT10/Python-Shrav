
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("C:/Users/Abhishek/OneDrive/Desktop/Kachra/CODING LANGs/PYTHON/Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# print(data)

new_dict = { row.letter:row.code for (index,row) in data.iterrows()}
# print(new_dict)
    
var = input("what is your name? : ").upper()

opt = [new_dict[letter] for letter in var]

print(opt)
