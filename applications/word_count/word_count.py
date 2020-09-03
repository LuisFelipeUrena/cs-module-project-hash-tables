def word_count(s):
    d = {}
    # words = s.split()
    # ignore = ['"',':',';',',','.','-','+','=',
    # '/',"\n",'|','[',']','{','}','(',')','*','^','&']
    ignore = '":;,.-+=/\\|[]{}()*^&'
    for i in ignore:
        if i in s:
            s = s.replace(i,'')
        else:
            continue    
    words = s.split()        
    
    for w in words:
        # if w.isspace():
        #     continue
        
        w = w.lower()
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d          

    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))