def main():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count= count_characters(text)
    #print(word_count)
    print(character_count)
    
def count_words(text):
    words=text.split()
    return len(words)

def count_characters(text):
    char_count={}
    for char in text:
        char=char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

