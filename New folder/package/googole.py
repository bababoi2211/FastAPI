from utilitis import yekan, dahgan

from setuptools
setup(
    name="adad_behorof"
    packages = find_packages()
)
def number_hrof(num: str) -> str:
    list_ = []
    if len(num) <= 3:
        list_ = []
        for i in range(len(num)):
            # region devide by ten
            ten = 10 ** (len(num)-i-1)
            letter = int(num[i])*ten
            letter = str(letter)
            # endregion
            if i == 1:
                list_.append(yekan[num[1:3]])
                break
            else:
                list_.append(yekan[letter])
                list_.append("و")

        if list_.count("و") != len(list_)-2 or "" in list_:
            list_.remove("و")

    else:

        if len(num) % 3 != 0:
            left_over = 3-(len(num) % 3)
            num = num.zfill(len(num)+left_over)
        while num != "":
            num_third = num[:3]
            ten = 10**(len(num)-1)
            for i in range(len(num_third)):
                ten_third = 10 ** (len(num_third)-i-1)
                letter = int(num_third[i])*ten_third
                letter = str(letter)

                if i == 1 and len(num) > 3:
                    list_.append(yekan[num_third[1:3]])
                    list_.append(dahgan[str(ten)])
                    break

                elif len(num) <= 3:
                    if i == 1:
                        list_.append(yekan[num[1:3]])
                        break
                    else:
                        list_.append(yekan[letter])
                        list_.append("و")
                else:
                    list_.append(yekan[letter])
                    list_.append("و")
            num = num.removeprefix(num_third)

    if list_.count("و") != len(list_)-2 or "" in list_:
        list_.remove("و")
    return " ".join(list_)


if __name__ == "__main__":
    number_hrof("344")
