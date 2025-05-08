import sys 
from stats import word_count
from stats import character_count
from stats import sort_dictionary

def get_book_text(file_path):
    cad = ""
    with open(file_path) as f:
        cad = f.read()
    return cad

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text=get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book_text)} total words")
        print("--------- Character Count -------")
        for dictionary in sort_dictionary(character_count(book_text)):
            print(dictionary["char"]+ ": " +str(dictionary["num"]))
        print("============= END ===============")

main()