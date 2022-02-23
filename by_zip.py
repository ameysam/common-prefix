from data import words


def find_common_prefix(words):
    words_list = list(zip(*words))
    tmp = ''
    for i in words_list:
        if len(set(i)) != 1:
            break
        tmp += i[0]
    return tmp

print(find_common_prefix(words))