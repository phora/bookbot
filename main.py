from stats import word_count

def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def main():
    wc = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{wc} words found in the document")

if __name__ == "__main__":
    main()
