def get_num_words(text):
    words = text.split()
    return len(text.split())

def get_num_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):  
    return dict["num"]

def sort_report(chars_dict):
    chars_count = [] # make an empty list
    for char, count in chars_dict.items(): # loop through the dictionary
        chars_count.append({"char": char, "num": count}) # add a dictionary to the list
    chars_count.sort(key=sort_on, reverse=True) # sort the list
    return chars_count # return the sorted list