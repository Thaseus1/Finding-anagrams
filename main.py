def find_anagram(word,anagram):
    word_list = list(word.replace(' ', ''))
    anagram_list = list(anagram.replace(' ', ''))
    i = 0
    nl = 0
    if len(word) == len(anagram):
        while i < len(word_list):
            number1 = word_list.count(word_list[i])
            number2 = anagram_list.count(word_list[i])
            if number1 == number2:
                i += 1
                nl += 1
            else:
                i += 1
        if nl == i:
            return True
        else:
            return False
    else:
        return False

