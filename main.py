from text_processing import count_words, count_characters, count_unique_characters, reverse_string, unique_words

test_string = "Hello world hello"

# using word count module
print("Word count is: ", count_words(test_string))
print("Unique words are: ", unique_words(test_string))

# using character count module
print("The character count is: ", count_characters(test_string))
print("The unique character count is: ", count_unique_characters(test_string) )

# using reverse module
print("Reversed string: ", reverse_string(test_string))