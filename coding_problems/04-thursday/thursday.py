def best_friend(txt: str, a: str, b: str) -> bool:
    text = list(txt)

    if a not in text:
        return True
    if text[-1] == a or a == b:
        return False
    for i in range(len(text)-1):
        if text[i] == a and not text[i + 1] == b:
            return False
    return True
