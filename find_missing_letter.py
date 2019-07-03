def find_missing_letter(chars):
    for i in range(len(chars)+1):
        if chr(ord(chars[0])+i) not in chars:
            return chr(ord(chars[0])+i)