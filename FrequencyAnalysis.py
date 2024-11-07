from collections import Counter

from main.TestData import frequency_english_letters
from main.TextModification import remove_non_letters, switch_letters, list_to_string


#Returns the frequency of the letters in order of most common
def get_letter_frequency(text):
    frequency_raw = Counter(text)
    return frequency_raw.most_common()

def get_letter_frequency_letters_only(text):
    frequency_raw = Counter(text)
    most_common = frequency_raw.most_common()
    letters_only_list = []

    for letter, number in most_common:
        letters_only_list.append(letter)

    return letters_only_list

#Uses the most common english frequency to make a strong initial guess
def get_frequency_analysis_best_initial_guess(encrypted_text):
    encrypted_text_without_non_letters = remove_non_letters(encrypted_text)

    #Frequency of encrypted letters
    encrypted_text_frequency = get_letter_frequency_letters_only(encrypted_text_without_non_letters)

    #tuple list of (most common letter... , 'alphabet_frequency')
    most_common_and_frequency_tuple_list = []
    i = 0

    for letter in encrypted_text_frequency:
        frequency_letter = frequency_english_letters[i]
        most_common_and_frequency_tuple = (letter, frequency_letter)
        most_common_and_frequency_tuple_list.append(most_common_and_frequency_tuple)
        i = i + 1

    return switch_letters(encrypted_text, most_common_and_frequency_tuple_list)