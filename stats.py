def get_word_amount(book_text):
    word_count = len(book_text.split())
    return word_count    

def get_char_dict(book_text):
    char_dict = {}

    for c in book_text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:      
            char_dict[c] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorting_items(char_dict):
    sorted_list = []
    for ch, count in char_dict.items():
        if ch.isalpha():
            sorted_list.append({"char":ch, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list