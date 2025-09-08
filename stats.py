def get_word_amount(text):
    word_count = len(text.split())
    return word_count    

def get_char_dict(text):
    char_dict = {}

    for c in text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:      
            char_dict[c] = 1
    return char_dict