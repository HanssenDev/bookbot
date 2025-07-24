# split the book content into a list of words and return the number of words
def count_words(book_text):
    words_list = book_text.split()
    return len(words_list)

# converts all characters from the book text into lowercase and returns the number of times each character appears in the book
def get_character_count(book_text):
    char_count = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_by_count(items):
    return items["num"]

def sort_characters(characters):
    char_list = []
    for char, num in characters.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(key=sort_by_count, reverse=True)
        
    return char_list