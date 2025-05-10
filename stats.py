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

def get_num_words(text):
    word_count = {}
    lower_text = text.lower().replace(",", "").split(" ")

    for w in lower_text:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    return word_count

def sort_word_count(word_dic):
    sorted_words = []
    for word in word_dic:
        sorted_words.append({"word": word, "count": word_dic[word]})

    sorted_words.sort(key=sort_by_count, reverse=True)

    return sorted_words[:10]

def sort_by_count(e):
    return e["count"]

def sort_character_count(char_dic):
    sorted_chars = []
    for char in char_dic:
        sorted_chars.append({"char": char, "count": char_dic[char]})

    sorted_chars.sort(key=sort_by_count, reverse=True)
    
    return sorted_chars
