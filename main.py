def main():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count= count_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document")
    print()
    
    for item in character_count:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['count']} times")
    print("---End report---")
    
def count_words(text):
    words=text.split()
    return len(words)

def sort_on(char_dict):
     return char_dict["count"]

def count_characters(text):
    char_count={}
    for char in text:
        if char.isalpha():
            char=char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_list = [{'character':key, 'count':value} for key,value in char_count.items()]
    char_list.sort(reverse = True, key=sort_on)
    return char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

