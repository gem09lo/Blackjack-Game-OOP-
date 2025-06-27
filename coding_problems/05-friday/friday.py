def is_anagram(s: str, t: str) -> bool:
    string_1 = sorted(list(s))
    string_2 = sorted(list(t))

    if string_1 == string_2:
        return True
    return False


#
print(is_anagram("aabc", "abbc"))
