from stats import get_word_amount, get_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    wc = get_word_amount(book_text)
    cd = get_char_dict(book_text)
    print(f"{wc} words found in the document, {cd}")

main()
