#caeser cipher coe in python
def  encrypt(ox,b):
      count=0
      while(ox < b):
            ox+=1
            count=count+1
      ox=b-25
      count +=1
      while(count !=3):
            ox+=1
            count+=1
      return ox
def encryption(a):
    l=[]
    for i in a:
        x=i
        ox=ord(x)
        if(x==' '):
            continue

        if(  (x.islower() and ox>119) ) :   #119=w
            b=122
            l.append(chr(encrypt(ox,b)))
        elif (x.isupper() and (ox > 87 and ox <91 )):
            b=90
            l.append(chr(encrypt(ox,b)))
        else:
            l.append(  chr(ox+3) )
    return l

def  decrypt(ox,b):
      count=0
      while(ox > b):
            ox-=1
            count=count+1
      ox=b+25
      count +=1
      while(count !=3):
            ox-=1
            count+=1
      return ox
def decryption(ct):
        l=[]
        for i in ct:
            x=i
            ox=ord(x) 
            if(x==' '):
                continue
            if(  (x.islower() and ox<100) ) :
                b=97
                l.append(chr(decrypt(ox,b)))
            elif (x.isupper() and ox<68  ):   #C-Z  B-Y  A-X
                b=65
                l.append(chr(decrypt(ox,b)))
            else:
                l.append(  chr(ox-3) ) 
        return l

a=input("ENTER PLAIN TEXT: ")
ct=encryption(a)
str=""
for c in ct:
    str+=c
print(f"""
PLAIN TEXT IS:  {a}
CIPHER TEXT IS: {str}
""")
#for decryption
dec_ct=""
dec_ct_list=decryption(ct)
for c in dec_ct_list:
    dec_ct+=c
print(f"""
CIPHER TEST: {str}
PLAIN TEXT AFTER DECRYPTION: {dec_ct}
""")


