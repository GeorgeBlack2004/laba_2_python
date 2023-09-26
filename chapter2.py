def checking(x):
    answer = 1
    if isinstance(x, list):
        print(f"List: {x}")
        most = 0
        for i in range(len(x)):
            if i % 2 != 0:
                answer *= x[i]
        for j in x:
            if j > most:
                most = j
        x.remove(most)
        print(f"Answer: {answer}")
        print(f"List: {x}")
    elif isinstance(x, dict):
        sorted_dict = dict(sorted(x.items(), key=lambda y: y[1], reverse=True))
        count = 0
        for key, value in sorted_dict.items():
            print(key, ':', value)
            count += 1
            if count == 3:
                break
    elif isinstance(x, int):
        suma = 0
        while x > 0:
            digit = x % 10
            suma = suma + digit
            x = x // 10
        print(f"Sum: {suma}")
    elif isinstance(x, str):
        vowels = ['a', 'e', 'i', 'u', 'o']
        total_vowels = 0
        total_un_vowels = 0
        for i in x:
            if i in vowels:
                total_vowels += 1
            else:
                total_un_vowels += 1
        words = x.split()
        count_words = len(words)

        print(f"Total vowels: {total_vowels}")
        print(f"Total un vowels: {total_un_vowels}")
        print(f"Amount words: {count_words}")


list_ = [1, 5, 3, 8, 2, -3, -1, 6, -4]
str_ = "My name is George and im from London"
int_ = 44
dict_ = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 1}

checking(list_)
checking(str_)
checking(int_)
checking(dict_)
