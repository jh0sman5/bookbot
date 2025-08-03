import sys

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()
    return file_contents

from stats import word_counter

from stats import num_of_letters

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        word_string = get_book_text(filepath)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        word_counter(word_string)
        print("--------- Character Count -------")
        num_of_letters(word_string)
        print("============= END ===============")
    
main()

