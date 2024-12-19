def number_of_vowels(word: str):
    """
    Counts the number of vowels in a word

    Arguments:
    - word (str): the word to count the vowels in

    Returns:
    - Integer: the number of vowels in a given word
    """
    vowels = 'aeiuoy' 

    count_v = 0
    for v in vowels:        
        count_v += word.count(v)
    
    return count_v



# Convert text to a list of words
text = "Een stukje tekst met allemaal klinkers"
list_of_words = text.lower().replace(',','').replace('.', '').split()

print(sorted(list_of_words))
print(sorted(list_of_words, key=number_of_vowels)) # Sort text on the function number_of_vowels


n_o_v = lambda word: sum(word.count(v) for v in 'aeiuoy')
print(sorted(list_of_words, key=n_o_v)) # Sort text on the function number_of_vowels

