## More comprehensions
# Task 1 (Filter forbidden)

def filter_forbidden(string: str, forbidden: str):
    new_str = ''.join([word for word in string if word not in forbidden])
    return new_str


sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)
