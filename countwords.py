def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words=file_contents.split()
    return len(words)

word_count=count_words()

print (word_count)