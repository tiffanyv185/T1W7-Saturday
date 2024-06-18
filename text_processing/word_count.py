def count_words(text):
    words = text.split()
    return len(words)

def unique_words(text):
    words = text.lower().split()
    return set(words)

print(count_words("good morning hello your money hello such"))
print(unique_words("good morning hello your money hello such"))