def remove_non_letters(text):
    return ''.join(char for char in text if char.isalpha()).lower()

#text is the original text, letters is a list of letter pairs. letters[0] replaced by letters[1]
def switch_letters(text, letters):
    final_text = []

    for letter in text:
        if letter == " ":
            final_text.append(" ")
        else:
            for old_letter, new_letter in letters:
                if letter == old_letter:
                    final_text.append(new_letter)

    return final_text

def list_to_string(list_of_characters):
    return ''.join(list_of_characters)

