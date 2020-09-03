def no_dups(s):
    # identify each word in the string
    # count each word
    # add it to the dictionary
    # print out a string with each individual word
    d = {}
    s = s.split()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    word = ' '        
    # for key,value in d.items():
    #    word = word.join(str(key))
    return word.join(d.keys()) 

        






if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))