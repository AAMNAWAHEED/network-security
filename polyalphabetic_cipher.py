def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def encryption(pt):
    pt=removespace(pt)
    ct=""
    m1={'a':'k','b':'d','c':'n','d':'h','e':'p','f':'a','g':'w','h':'x','i':'c','j':'z','k':'i','l':'m','m':'q','n':'j','o':'b','p':'y','q':'e','r':'t','s':'u','t':'g','u':'v','v':'r','w':'f','x':'o','y':'s','z':'l'}
    m2={'a':'p','b':'a','c':'g','d':'u','e':'k','f':'h','g':'j','h':'b','i':'y','j':'d','k':'s','l':'o','m':'e','n':'m','o':'q','p':'n','q':'w','r':'f','s':'z','t':'i','u':'t','v':'c','w':'v','x':'l','y':'x','z':'r'}
    m3={'a':'j','b':'m','c':'f','d':'z','e':'r','f':'n','g':'l','h':'d','i':'o','j':'w','k':'g','l':'i','m':'a','n':'k','o':'e','p':'s','q':'u','r':'c','s':'q','t':'v','u':'h','v':'y','w':'x','x':'t','y':'p','z':'b'}
    i=1
    for p in pt:
        if i==1:
            ct+=m1[p]
        elif i==2:
            ct+=m2[p]
        else:
            ct+=m3[p]
        i+=1
        if i>3:
            i=1
    return ct
def decryption(ct):
    dec_ct=""
    m1={'k':'a','d':'b','n':'c','h':'d','p':'e','a':'f','w':'g','x':'h','c':'i','z':'j','i':'k','m':'l','q':'m','j':'n','b':'o','y':'p','e':'q','t':'r','u':'s','g':'t','v':'u','r':'v','f':'w','o':'x','s':'y','l':'z'}       
    m2={'p':'a','a':'b','g':'c','u':'d','k':'e','h':'f','j':'g','b':'h','y':'i','d':'j','s':'k','o':'l','e':'m','m':'n','q':'o','n':'p','w':'q','f':'r','z':'s','i':'t','t':'u','c':'v','v':'w','l':'x','x':'y','r':'z'}  
    m3={'j':'a','m':'b','f':'c','z':'d','r':'e','n':'f','l':'g','d':'h','o':'i','w':'j','g':'k','i':'l','a':'m','k':'n','e':'o','s':'p','u':'q','c':'r','q':'s','v':'t','h':'u','y':'v','x':'w','t':'x','p':'y','b':'z'}  
    i=1
    for c in ct:
        if i==1:
            dec_ct+=m1[c]
        elif i==2:
            dec_ct+=m2[c]
        else:
            dec_ct+=m3[c]
        i+=1
        if i>3:
            i=1
    return dec_ct
pt=input("ENTER PLAIN TEXT: ")
ct=encryption(pt)
print(f"""
PLAIN TEXT IS: {pt}
CIPHER TEXT IS: {ct}
""")
dec_ct=decryption(ct)
print(f"""
CIPHER TEXT: {ct}
DECRYPT CIPHER TEXT: {dec_ct}
""")