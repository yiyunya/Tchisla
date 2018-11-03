sup = 1000  #上限

def factorial(n):

    if n>10: return sup+1
    m = 1
    for i in range(1,n+1):
        m *= i
    return m

digit = input('digit=')
quantity = input('quantity=')

dig = int(digit)
quantity = int(quantity)
if dig in {2,3,4,5,6,7,8,9}:
    dic = {dig:1,1:2,dig*11:2,dig*111:3,dig*1111:4,dig*11111:5}
    ch = str(dig)
    word = {dig:'{}'.format(dig),1:'(({}-{})!)'.format(dig,dig),
            dig*11:ch*2,dig*111:ch*3,dig*1111:ch*4,dig*11111:ch*5}
    new = [dig]
elif dig in {1}:
    dic = {dig:1,dig*11:2,dig*111:3,dig*1111:4,dig*11111:5}
    ch = str(dig)
    word = {dig:'{}'.format(dig),
            dig*11:ch*2,dig*111:ch*3,dig*1111:ch*4,dig*11111:ch*5}
    new = [dig]
else:
    raise ValueError

print(dic,word)


for num in range(quantity-1):
    while new:
        #print('new=',new)
        for i in new:
            fac = factorial(i)
            if fac < sup and fac != i:
                di = dic[i]
                try:
                    if dic[fac] > di:
                        dic[fac] = di
                        word[fac] = '('+word[i]+'!)'
                        new.append(fac)
                except:
                    dic[fac] = di
                    word[fac] = '('+word[i]+'!)'
                    new.append(fac)
            sqrt = int(i**0.5)
            if i**0.5 % 1 == 0 and sqrt!= i:        
                di = dic[i]
                try:
                    if dic[sqrt] > di:
                        dic[sqrt] = di
                        word[sqrt] = '(√'+word[i]+')'
                        new.append(sqrt)
                except:
                    dic[sqrt] = di
                    word[sqrt] = '(√'+word[i]+')'
                    new.append(sqrt)
            new.remove(i)
    #print('1-dic=',dic)

    newdic = dic.copy()
    l = len(dic)
    cycles = l*(l-1)/2
    #print(l,cycles)
    complete = 0
    for i in dic:
        for j in dic:
            di = dic[i]
            dj = dic[j]
            if j >= i and (di+dj==num+2):
                def sim(x,wrd):
                    if 0 < x < sup and x%1 == 0:
                        x = int(x)
                        try:
                            if dic[x] > di + dj:
                                newdic[x] = di + dj
                                word[x] = wrd.format(word[i],word[j])
                                new.append(x)
                        except:
                            newdic[x] = di + dj
                            word[x] = wrd.format(word[i],word[j])
                            new.append(x)
                sim(i+j,'({0}+{1})')
                sim(j-i,'({1}-{0})')
                sim(i*j,'({0}*{1})')
                sim(j/i,'({1}/{0})')
                if i*j < 70000:
                    sim(i**j,'({0}^{1})')
                    sim(j**i,'({1}^{0})')
                    
                complete += 1
                # print(complete,'/',cycles)
    ##                if i+j < sup:
    ##                    try:
    ##                        if dic[i+j] > dic[i]+dic[j]:
    ##                            newdic[i+j] = dic[i]+dic[j]
    ##                            new.append(i+j)
    ##                    except:
    ##                        newdic[i+j] = dic[i]+dic[j]
    ##                        new.append(i+j)
    ##
    ##                if j-i < sup:
    ##                    try:
    ##                        if dic[j-i] > dic[i]+dic[j]:
    ##                            newdic[j-i] = dic[i]+dic[j]
    ##                            new.append(j-i)
    ##                    except:
    ##                        newdic[j-i] = dic[i]+dic[j]
    ##                        new.append(j-i)
    ##
    ##                if i*j < sup:
    ##                    try:
    ##                        if dic[i*j] > dic[i]+dic[j]:
    ##                            newdic[i*j] = dic[i]+dic[j]
    ##                            new.append(i*j)
    ##                    except:
    ##                        newdic[i*j] = dic[i]+dic[j]
    ##                        new.append(i*j)
    ##
    ##                if j/i < sup and (j/i)% 1 == 0:
    ##                    quote = int(j/i)
    ##                    try:
    ##                        if dic[quote] > dic[i]+dic[j]:
    ##                            newdic[quote] = dic[i]+dic[j]
    ##                            new.append(quote)
    ##                    except:
    ##                        newdic[quote] = dic[i]+dic[j]
    ##                        new.append(quote)
    ##
    ##                if i**j < sup:
    ##                    try:
    ##                        if dic[i**j] > dic[i]+dic[j]:
    ##                            newdic[i**j] = dic[i]+dic[j]
    ##                            new.append(i**j)
    ##                    except:
    ##                        newdic[i**j] = dic[i]+dic[j]
    ##                        new.append(i**j)
    ##
    ##                if j**i < sup:
    ##                    try:
    ##                        if dic[j**i] > dic[i]+dic[j]:
    ##                            newdic[j**i] = dic[i]+dic[j]
    ##                            new.append(j**i)
    ##                    except:
    ##                        newdic[j**i] = dic[i]+dic[j]
    ##                        new.append(j**i)

    dic = newdic
    #print('2-dic=',dic)
    if num == quantity-2:
        for i in sorted(dic):
            print(i,dic[i],word[i])


         
                    
                    
