def words_check(text):
    lsd = text.split()
    vect = []
    res = {}
    for i in lsd:
        badchars = 0
        allchars = len(i) / 2
        goodword = ""
        for j in i:
            if j.isalpha():
                char = j.lower()
                goodword = goodword + char
            else:
                badchars = badchars + 1
        if len(goodword)>0:
            goodword = goodword.capitalize()
        if badchars < allchars:
            vect.append(goodword)
    # end of loop
    for i in vect:
        res[i] = 0
    for i in vect:
        res[i] = res[i] + 1
    return res


# print(words_check("""hEllO My FriEnDs!!!
# thIS is A tEsT For your #p#r#o#b#l#e#m a"""))

# {'A': 2, 'For': 1, 'Friends': 1, 'Hello': 1, 'Is': 1, 'My': 1, 'Test': 1, 'This': 1, 'Your': 1}