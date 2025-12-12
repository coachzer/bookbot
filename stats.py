def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_unique_chars(text):
    new_text = text.lower()
    unique_chars = set(new_text)
    # k, v dict where k is char and v is count
    char_count_dict = {char: new_text.count(char) for char in unique_chars}
    return char_count_dict


def sort_on(items):
    return items["num"]


def sorted_char_count(char_count_dict):
    char_count_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_count_list.append({"char": char, "num": count})
    sorted_list = sorted(char_count_list, key=sort_on, reverse=True)
    return sorted_list
