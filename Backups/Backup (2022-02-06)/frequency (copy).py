"""
Creates functions for analysing letter frequency and recommending words. 
"""


#Removes green & yellow letters from eligible words
def partial_words(word_list, green_yellow):
    partial_word_list = []
    for candidate in word_list:
        for letter in range(0, len(green_yellow)):
            if (green_yellow[letter] in candidate):
                x = green_yellow[letter]
                candidate = candidate.replace(x, "", 1) #removes the first instance of each green/yellow letter from the dictionary
        partial_word_list.append(candidate)
    return partial_word_list

#Calculates the frequency of each letter
def frequency(word_list):
    from collections import Counter #Used for freq analysis
    word_string = ''.join(word_list)
    counts=Counter(word_string)
    unsorted_perc = {k: v / total for total in (sum(counts.values()),) for k, v in counts.items()} #https://stackoverflow.com/a/30964597 - how does this work?
    sorted_perc = {k: v for k, v in sorted(unsorted_perc.items(), key=lambda item: item[1])}
    return sorted_perc


def best_letters(letter_dictionary, m):
    import heapq
    letters = []
    letter_freq = []
    m = 10
    for key in letter_dictionary.keys():
        letters.append(key)
    for value in letter_dictionary.values():
        letter_freq.append(round(value*100,2))
    best_m_index = heapq.nlargest(m, range(len(letter_freq)), letter_freq.__getitem__) #Gets indices for largest n frequency values
    accessed_mapping_letters = map(letters.__getitem__, best_m_index) #Gets words for indices of highest frequency
    accessed_mapping_scores = map(letter_freq.__getitem__, best_m_index)
    bestm_letters = list(accessed_mapping_letters)
    bestm_scores = list(accessed_mapping_scores)
    print(f"Excluding known Greens & Yellows,\nthe top {m} letters in frequency are:")
    for i in range(0, len(bestm_letters)):
        print(f"    {bestm_letters[i]} :  {bestm_scores[i]}%")


#Apply frequency to dictionary
#Create list of dictionary length where each value is the sum of the letter frequency
def scored_words(word_list, sorted_perc):
    word_frequency = []
    for word in word_list:
        word_score_values = []
        for letter in range(0, len(word)):
            word_score_values.append(sorted_perc.get(word[letter], 0))
        word_score = sum(word_score_values)
        word_frequency.append(word_score)
    return word_frequency

#Identifies the words with the highest frequency scores
def best_words (partial_word_list, word_frequency, n):
    import heapq
    n = 5 #Number of top words to return
    best_n_index = heapq.nlargest(n, range(len(word_frequency)), word_frequency.__getitem__) #Gets indices for largest five frequency values
    accessed_mapping_words = map(partial_word_list.__getitem__, best_n_index) #Gets words for indices of highest frequency
    accessed_mapping_scores = map(word_frequency.__getitem__, best_n_index)
    bestn_words = list(accessed_mapping_words)
    bestn_scores = list(accessed_mapping_scores)
    length = len(bestn_words)
    bestn_scores_100 = []
    for item in bestn_scores:
        bestn_scores_100.append(round(item*100,1))
    print(f"The top {length} highest scored words are:")
    for n in range(0, len(bestn_words)):
        print(f"    {bestn_words[n]} : {bestn_scores_100[n]}")


def frequecy_analysis(remaining_word_list, allowed_list, green_yellow, no_letters, no_words):
    part_words = partial_words(remaining_word_list, green_yellow)
    letter_frequency_dict = frequency(part_words)
    best_letters(letter_frequency_dict, 10)
    scored_words_var = scored_words(allowed_list, letter_frequency_dict)
    best_words(allowed_list, scored_words_var, 5)



# print(output)

# word_list = ["shark", "pants", "smart", "plate", "beech", "coins"]
# green_yellow = ["a", "e"]
# output = frequency.partial_words(word_list, green_yellow)
# print(output)
# freq = frequency.frequency(output)
# print(freq)
# frequency.best_letters(freq, 10)
# scored_words = frequency.scored_words(output, freq)
# print(scored_words)
# frequency.best_words(word_list, scored_words, 5)