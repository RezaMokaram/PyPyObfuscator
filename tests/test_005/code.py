def check_registration_rules(**kwargs):
    li = []
    for key, value in kwargs.items():
        if (key == "codecup" or key == "quera"): 
            continue
        if (len(key) < 4): 
            continue
        if (len(value) < 6): 
            continue
        if (value.isdigit()): 
            continue
        li.append(key)
    return li

# print (check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$'))
# print (check_registration_rules(saeed='1234567', ab='afj$L12'))