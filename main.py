import stats

def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    wc = stats.word_count(book_text)
    cf = stats.char_frequency(book_text)
    print(f"{wc} words found in the document")
    print(cf)

if __name__ == "__main__":
    main()
