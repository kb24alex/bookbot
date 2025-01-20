def main():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(word_count)
    
def count_words(text):
    words=text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

