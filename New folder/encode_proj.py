from package import 
from string import ascii_uppercase, ascii_lowercase

lower_letter = [i for i in ascii_lowercase]
upper_letter = [i for i in ascii_uppercase]

num = "acd"
encode = 2

list_ = []

for index in range(len(num)):
    if num[index] in lower_letter:
        index_encode = lower_letter.index(num[index])
        index_encode = index+encode
        if index_encode > 26:
            new_index = (index+encode)-26
            lower_letter[new_index]
        result = lower_letter[index+encode]
        list_.append(result)
    elif num[index] in upper_letter:
        index_encode = upper_letter.index(num[index])
        index_encode = index+encode
        if index_encode > 26:
            new_index = (index+encode)-26
            upper_letter[new_index]
        result = upper_letter[index+encode]
        list_.append(result)



print("".join(list_))


# +2 va -2
