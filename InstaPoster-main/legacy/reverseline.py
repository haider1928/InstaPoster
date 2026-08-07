def reverse_lines_in_string(text):
    lines = text.splitlines()  # لائنز کو الگ کریں
    reversed_text = "\n".join(lines[::-1])  # ریورس کر کے دوبارہ جوڑیں
    return reversed_text