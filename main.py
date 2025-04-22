import sys
from stats import get_num_words, get_num_character, sorted_list_dictionnaries

def main():
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_char = get_num_character(text)
    sorted_char = sorted_list_dictionnaries(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionnary in sorted_char:
        letter = dictionnary['letter']
        count = dictionnary['count']
        print(f"{letter}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

    


main()