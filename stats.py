def word_counter(word_string):
    word_count = 0
    word_list = word_string.split()
    for word in word_list:
        word_count += 1
    print(f"Found {word_count} total words")

def num_of_letters(word_string):
    character_dictionary = {}
    for character in word_string:
        character = character.lower()
        if character in character_dictionary: 
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    char_list = list(character_dictionary.items())
    char_list.sort(key=lambda item: item[1], reverse=True)
    for char, count in char_list:
        print(f"{char}: {count}")    




    
    
