import random
import string
def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def random_key(length):
    #random choice() pick a single character from the string constant 
    letters = string.ascii_lowercase
    key = ''.join(random.choice(letters) for i in range(length)) 
    return key
def encryption(pt,key):
    mapping={}
    for i in range(97,97+26):
        mapping[chr(i)]=i-97
    map_pt=[]
    for p in pt:
        map_pt.append(mapping[p])
    map_key=[]
    for k in key:
        map_key.append(mapping[k])
    #addition
    add=[]
    for p in range(len(pt)):
        x=map_pt[p]+map_key[p]
        if x >25:
            x=x-26
        add.append(x)
    
    
    reverse_mapping={}
    for i in range(97,97+26):
        reverse_mapping[i-97]=chr(i)
    ct=""
    for a in add:
        ct+=reverse_mapping[a]
    
    print(f"""
    ENCRYPTION:
    PLAIN TEXT IS:{pt}
    NUMBERED PLAIN TEXT IS: {map_pt}
    RANDOM KEY IS: {key}
    NUMBERED KEY IS: {map_key}
    PLAIN TEXT + KEY IS: {add}
    CIPHER TEXT: {ct}
    """)
    return ct
def decryption(ct,key):
    mapping={}
    for i in range(97,97+26):
        mapping[chr(i)]=i-97
    map_ct=[]
    for c in ct:
        map_ct.append(mapping[c])
    map_key=[]
    for k in key:
        map_key.append(mapping[k])
    sub=[]
    for c in range(len(ct)):
        x=map_ct[c]-map_key[c]
        if x <0:
            x=x+26
        sub.append(x)
    reverse_mapping={}
    for i in range(97,97+26):
        reverse_mapping[i-97]=chr(i)
    dec_ct=""
    for a in sub:
        dec_ct+=reverse_mapping[a]
    print(f"""
    CIPHET TEXT: {ct}
    NUMBERED CIPHER TEXT: {map_ct}
    KEY: {key}
    NUMBERED KEY: {map_key}
    CIPHER TEXT - KEY: {sub}
    PLAIN TEXT: {dec_ct}
    """)

pt=input("ENTE PLAIN TEXT:\t")
pt=removespace(pt)
key=random_key(len(pt))
ct=encryption(pt,key)
decryption(ct,key)
