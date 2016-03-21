#!/usr/env/python -tt

basicnum = """one
two
three
four
five
six
seven
eight
nine""".split("\n")

teennum ="""ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen""".split("\n")

tynum ="""twenty
thirty
forty
fifty
sixty
seventy
eighty
ninety""".split("\n")

def get_numcount(i):
    l = [int(s) for s in "%04d" % i]
    r = ""

    if l[-4]:
        r = "onethousand"
    else:
        if l[-3]:
            r += basicnum[l[-3]-1] + "hundred"
            if l[-2] or l[-1]:
                r += "and"
        if l[-2] == 1:
            r += teennum[l[-1]]
        else:
            if l[-2]:
                r += tynum[l[-2]-2]
            if l[-1]:
                r += basicnum[l[-1]-1]

    return r
    
if __name__ == '__main__':
    r = 0
    
    for i in xrange(1, 1000+1):
        s = get_numcount(i)
        print i, s, len(s)
        r += len(s)
    print r
