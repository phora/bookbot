import stats

def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def main():
    books = [
        "./books/frankenstein.txt"
    ]
    print("============== BOOKBOT ==============")
    for book in books:
        print(f"Analyzing book found at {book}...")
        book_text = get_book_text(book)
        wc = stats.word_count(book_text)
        cf = stats.sort_char_frequency(stats.char_frequency(book_text))
        print("--------- Word Count ---------")
        print(f"Found {wc} total words")
        print("------ Character Count -------")
        for entry in cf:
            if not entry['char'].isalpha():
                continue
            print(f"{entry['char']}: {entry['num']}")
    print("================ END ================")

if __name__ == "__main__":
    main()
