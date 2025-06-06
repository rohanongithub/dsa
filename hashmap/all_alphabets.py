test_alphabets = "asdjzzkasswoz&&"

q = ["a","b","i","z","k","&"]

hash_list = [0]*128

for letter in test_alphabets:
    ascii_value = ord(letter)
    index = ascii_value  #bcoz ascii value of lowecase start from 97 to 122
    hash_list[index] += 1

for check_letter in q:
    ascii_value = ord(check_letter)
    index = ascii_value
    print(f"{check_letter} : {hash_list[index]}")
