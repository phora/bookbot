import argparse

import stats
import sys

def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def main():
    # TODO: This only exists because the book project wants exit code 1, not 2
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('books', nargs="+")
    args = parser.parse_args()

    print("============== BOOKBOT ==============")
    for book in args.books:
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
