from stats import get_num_words, get_num_unique_chars, sorted_char_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    import sys

    if sys.argv and len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_text = get_book_text(book_path)
    # print(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_word_count = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    unique_char_count = get_num_unique_chars(book_text)
    print("--------- Character Count -------")
    sorted_char_count_list = sorted_char_count(unique_char_count)
    for char_count in sorted_char_count_list:
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
