from data import words

def zip_alternative(words):
    
    # get minimum length of words
    min_length = min(len(i) for i in words)

    # split words into a list of tuples (like zip function)
    words_list = []
    for i in range(min_length):
        tmp = []
        for word in words:
            tmp.append(word[i])
        words_list.append(tuple(tmp))
    
    return words_list

# find common prefix
def find_common_prefix(words):
    words_list = zip_alternative(words)
    tmp = ''
    for i in words_list:
        if len(set(i)) != 1:
            break
        tmp += i[0]
    return tmp


print(find_common_prefix(words))