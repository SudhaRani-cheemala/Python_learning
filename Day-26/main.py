import pandas
data=pandas.read_csv("nato_phonetic.csv")
print(data.to_dict())
phonetic_dic={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dic)
# create a list of the phonetic code  words from a word that the user inputs
word=input("Enter a word:").upper()
output_list=[phonetic_dic[letter] for letter  in word]
print(output_list)

