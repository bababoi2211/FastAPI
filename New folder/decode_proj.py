

from string import ascii_uppercase, ascii_lowercase

lower_letter = [i for i in ascii_lowercase]
upper_letter = [i for i in ascii_uppercase]

num = "cde"  # acd
decode = 2

list_ = []

for index in range(len(num)):
    if num[index] in lower_letter:
        index_encode = lower_letter.index(num[index])
        index_encode = index_encode-decode
        if index_encode < 0:
            new_index = (index_encode)+26
            result = lower_letter[new_index]
        else:
            result = lower_letter[index_encode]
        list_.append(result)
    elif num[index] in upper_letter:
        index_encode = upper_letter.index(num[index])
        index_encode = index-decode
        if index_encode < 0:
            new_index = (index-decode)+26
            upper_letter[new_index]
        result = upper_letter[index-decode]
        list_.append(result)

print("".join(list_))


# +2 va -2
