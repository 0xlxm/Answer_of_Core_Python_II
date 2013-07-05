def like():
    import strin
    import random
    Letter = string.ascii_uppercase 
    letter = string.ascii_lowercase
    name = raw_input('Input string: ')
    newname = ''
    for i in name:
        if i in Letter:
            newname += random.choice(letter)
            continue
        if i in letter:
            newname += random.choice(Letter)
            continue
        newname +=i
    return newname

print like()
