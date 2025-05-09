def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    character_count = {}
    lower_text = text.lower()

    for c in lower_text:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1

    return character_count

def sort_char(e):
    return e["count"]

def sort_character_count(char_dic):
    sorted_chars = []
    for char in char_dic:
        sorted_chars.append({"char": char, "count": char_dic[char]})

    sorted_chars.sort(key=sort_char, reverse=True)
    
    return sorted_chars
