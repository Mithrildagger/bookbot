def main():
    name_of_book = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
            
    # print(file_contents)
    word_count = count_words(words)
    chars_dict = get_chars_dict(file_contents)
    
    get_report(name_of_book, word_count, chars_dict)


def count_words(words):
    word_counter = 0
    for word in words:
        word_counter+=1
    return word_counter 

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_report(name_of_book, word_count, chars_dict):
    print (f"--- Begin report of {name_of_book} ---")
    print (f"    {word_count} words found in document")
    for char in chars_dict:
        print(f"The '{char}' character was found {chars_dict[char]} times")
    print("--- End report ---")
    


main()