def is_ana_pal(word):
    # Is the word an anagram of a palindrome?

    # A palindrome is a word that reads the same forward 
    # and backwards (eg, “racecar”, “tacocat”). An anagram 
    # is a rescrambling of a word (eg for “racecar”, you 
    # could rescramble this as “arceace”).
    # Determine if the given word is a re-scrambling of a palindrome.
    # The word will only contain lowercase letters, a-z.


    anagram_dict = {}
    if len(word) % 2 == 0:
        return False
    # construct the dictionary
    for char in word:
        # put char, count into dictionary
        if char not in anagram_dict:
            anagram_dict[char] = 1
        else:
            anagram_dict[char] = anagram_dict[char] + 1

    # find how many items in dictionary contain a count of 1
    count_count = 0
    for letter in anagram_dict:
        if anagram_dict[letter] == 1:
            count_count += 1
    if count_count > 1:
        return False
    return True

print is_ana_pal("hello")
print is_ana_pal("a")
print is_ana_pal("ab")
print is_ana_pal("aab")
print is_ana_pal("arceace")
print is_ana_pal("arceaceb")