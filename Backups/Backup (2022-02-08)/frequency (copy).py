"""
Creates functions for analysing letter frequency and recommending words. It takes the remaining dictionary of valid words, and ranks them by letter frequency (excluding known Greens and Yellows).
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

#Creates a list of the m most frequently occuring letters.
def best_letters(letter_dictionary, m_letters):
    import heapq
    letters = []
    letter_freq = []

    for key in letter_dictionary.keys():
        letters.append(key)
    for value in letter_dictionary.values():
        letter_freq.append(round(value*100,1))
    
    best_m_index = heapq.nlargest(m_letters, range(len(letter_freq)), letter_freq.__getitem__) #Gets indices for largest n frequency values
    accessed_mapping_letters = map(letters.__getitem__, best_m_index) #Gets words for indices of highest frequency
    accessed_mapping_scores = map(letter_freq.__getitem__, best_m_index)
    bestm_letters = list(accessed_mapping_letters)
    bestm_scores = list(accessed_mapping_scores)

    print(f"\nExcluding known Greens & Yellows, the top {len(bestm_letters)} letters in frequency are:")
    n = int(len(bestm_letters)/2 + (len(bestm_letters) % 2 > 0))

    for i in range(0, n):
        j = i + n
        if j < len(bestm_letters):
            print(f"    {bestm_letters[i]}   : {bestm_scores[i]:4.1f}%        {bestm_letters[j]}   : {bestm_scores[j]:4.1f}%")
        else:
            print(f"    {bestm_letters[i]}   : {bestm_scores[i]:4.1f}%")


#Apply frequency to dictionary
#Create list of dictionary length where each value is the sum of the letter frequency
def scored_words(word_list, sorted_perc):
    word_frequency = []
    for word in word_list:
        word_score_values = []
        used_letters = []

        for letter in range(0, len(word)):
            if word[letter] not in used_letters:
                word_score_values.append(sorted_perc.get(word[letter], 0))
            used_letters.append(word[letter])

        word_score = sum(word_score_values)
        word_frequency.append(word_score)
    return word_frequency

#Identifies the words with the highest frequency scores
def best_words (partial_word_list, word_frequency, n):
    import heapq
    best_n_index = heapq.nlargest(n, range(len(word_frequency)), word_frequency.__getitem__) #Gets indices for largest five frequency values
    accessed_mapping_words = map(partial_word_list.__getitem__, best_n_index) #Gets words for indices of highest frequency
    accessed_mapping_scores = map(word_frequency.__getitem__, best_n_index)
    bestn_words = list(accessed_mapping_words)
    bestn_scores = list(accessed_mapping_scores)
    bestn_scores_100 = []
    for item in bestn_scores:
        bestn_scores_100.append(round(item*100,1))
    length = len(bestn_words)

    l = int(length/2 + (length % 2 > 0))
    for n in range(0, l):
        m = n + l
        if m < length:
            print(f"  {bestn_words[n]} :  {bestn_scores_100[n]:4.1f}      {bestn_words[m]} :  {bestn_scores_100[m]:4.1f}")
        else:
            print(f"  {bestn_words[n]} :  {bestn_scores_100[n]:4.1f}")

#These functions of functions combine the above for use in the main code:
#Frequency analysis of letters
def frequecy_analysis(remaining_word_list, green_yellow, no_letters):
    part_words = partial_words(remaining_word_list, green_yellow)
    letter_frequency_dict = frequency(part_words)
    best_letters(letter_frequency_dict, no_letters)
    return letter_frequency_dict

#Recommended words based on given dictionary and letter frequency
def recommended_words(word_list, letter_frequency_dict, no_words):
    scored_words_var = scored_words(word_list, letter_frequency_dict)
    best_words(word_list, scored_words_var, no_words)
