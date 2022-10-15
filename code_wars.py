# String experiments
str1 = "the-weak-say-i-am-strong"

def change_string(stg):
    list_ch = []
    for i, c in enumerate(stg):
        list_ch.append(c)

    for j, d in enumerate(list_ch):
        if d == '-':
            list_ch[j+1] = list_ch[j+1].upper()
            list_ch.remove(d) # remove the dashes (-)
    # converts a list to a string
    my_string = ''.join(list_ch)

    return my_string


print(change_string(str1))

------------------------------------------------------------------






