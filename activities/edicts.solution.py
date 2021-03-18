def no_vowels(word):
    if len(word) == 0:
        return word
    else:
        result = ""
        if word[0] not in ['a', 'e', 'i', 'o', 'u']:
            result += word[0]
        result += no_vowels(word[1:])
        return result


def no_double_letters(word):
    if len(word) == 0 or len(word) == 1:
        return word
    else:
        if word[0] == word[1]:
            return no_double_letters(word[1:])
        else:
            return word[0] + no_double_letters(word[1:])
