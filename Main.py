from main.FrequencyAnalysis import get_frequency_analysis_best_initial_guess
from main.TestData import test_data, frequency_english_letters
from main.TextModification import remove_non_letters, switch_letters, list_to_string

encrypted_text = list(test_data)

#tuples in this list will replace text as so [('old_letter','new_letter'),('a' : 'b')]
switch_these_letters = [('c','a'),('f','t'),('a','m'),('t','e'),('k','i'),('p','s'),('m','l'),('b','o'),('e','n'),('y','c'),('j','u'),('h','p'),('z','w')]

print(frequency_english_letters)

#If there are spaces, remove the spaces
encrypted_text_letters_only = remove_non_letters(encrypted_text)

#The encrypted text before using frequency analysis
print("before frequency analysis:",list_to_string(encrypted_text))
#The encrypted text after using frequency analysis (You can see some correct pairs found)
print("after frequency analysis:",list_to_string(get_frequency_analysis_best_initial_guess(encrypted_text)))

#Now you can use what you have to find pairs and add them to the switch_these_letters list above and slowly break the encryption
print("\n",list_to_string(switch_letters(encrypted_text, switch_these_letters)))

#NEXT: 1. Pattern recognition - Look for common patterns i.e. 'th', 'qu'
#Automate the entire process 