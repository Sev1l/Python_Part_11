## More comprehensions
# Task 5 (Most common words)


def most_common_words(filename: str, lower_limit: int):
    dict = {}
    with open (filename) as f:
        text = f.read()
        text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace("'", '')
        list = text.split()
        for i in list:
            if i not in dict and list.count(i) >= lower_limit:
                dict[i] = list.count(i)
        print(dict)
        


most_common_words("comprehensions.txt", 3)
