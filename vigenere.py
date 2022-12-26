def generate_fullkey(pt,key):
    if len(pt)== len(key):
        return key
    else:
        i=0
        while len(key) != len(pt):
            key+=key[i]
            i+=1
            if i == len(key):
                i=0
    return key

def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def encryption(pt,full_key):
    pt=removespace(pt)
    ct=""
    mapping={}
    for i in range(97,97+26):
        mapping[chr(i)]=i-97
    reverse_mapping={}
    for i in range(97,97+26):
        reverse_mapping[i-97]=chr(i)
    for i in range(len(pt)):
        value=(mapping[pt[i]] + mapping[full_key[i]]) % 26
        ct+=reverse_mapping[value]
    return ct
def decryption(ct,full_key):
    dec_ct=""
    mapping={}
    for i in range(97,97+26):
        mapping[chr(i)]=i-97
    reverse_mapping={}
    for i in range(97,97+26):
        reverse_mapping[i-97]=chr(i)
    for i in range(len(ct)):
        value=(mapping[ct[i]] - mapping[full_key[i]]) % 26
        dec_ct+=reverse_mapping[value]
    return dec_ct


pt=input("ENTER PLAIN TEXT:\t")
key=input("ENTER KEY:\t")
full_key=generate_fullkey(pt,key)
ct=encryption(pt,full_key)
print(f"""
PLAIN TEXT:{pt}
CIPHET TEST: {ct}
""")
dec_ct=decryption(ct,full_key)
print(f"""
CIPHER TEXT: {ct}
DECRYPT CIPHER TEXT: {dec_ct}
""")