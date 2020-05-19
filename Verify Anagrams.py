def verify_anagrams(first_word, second_word):
    # making the word to lower case for an easier comparison
    first_lower = first_word.lower()
    second_lower = second_word.lower()

    # made a list and then sorted the list in order of ascii values
    first_list = sorted(list(map(str, first_lower)))
    second_list = sorted(list(map(str, second_lower)))
    
    # removing the spaces
    new_first_list = [x for x in first_list if x != ' ']
    new_second_list = [y for y in second_list if y != ' ']

    # comparing the list: return true if two lists are identical
    if new_first_list == new_second_list:
        return True
    else:
        return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
