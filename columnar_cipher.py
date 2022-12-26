import string
import numpy as np
def key_strtoint(key,num_key):
    count=0
    atoz=string.ascii_lowercase
    for i in range(len(atoz)):
        for j in range(len(key)):
            if atoz[i] == key[j]:
                count+=1
                num_key[j]=count

    return num_key
def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def reset_pt(pt,length):
    filler_char=string.ascii_lowercase
    f=0
    while len(pt)% len(key) !=0:
        pt+=filler_char[f]
        f+=1
    return pt
def generate_matrix(pt,length):
    r=len(pt) // length
    c=length
    mat=np.empty([r,c],str)
    p=0
    for i in range(0,r):
        for j in range(0,c):
            mat[i][j]=pt[p]
            p+=1
    return mat

def read_mat(num_key,mat,len_of_pt):
    r=len_of_pt // len(num_key)
    ct=""
    k=1
    while k <=len(num_key):
        c=num_key.index(k)
        for i in range(r):#r
            ct+=mat[i][c]
        k+=1
    return ct
def encryption(pt,key,num_key):
    pt=removespace(pt)
    pt=reset_pt(pt,len(key))
    mat=generate_matrix(pt,len(key))
    ct=read_mat(num_key,mat,len(pt))
    return ct

def decrypt(num_key,ct):
    pt=""
    r=len(ct)//len(num_key)
    c=len(num_key)
    mat=np.empty([r,c],str)
    n=0
    p=0
    col_pt=ct[n:n+5]
    n+=5
    i=1
    while i <= len(num_key):
        col_no=num_key.index(i)
    #for i in range(0,c):  #column  
        for j in range(0,r):  #row
            mat[j][col_no]=col_pt[p]
            p+=1
        p=0
        col_pt=ct[n:n+5]
        n=n+5
        i+=1
    for i in range(r):
       for j in range(c):
         pt+=mat[i][j]
    return pt

key=input("ENTER KEY:\t")
if type(key) != 'int':
    num_key=list(range(len(key)))
    num_key=key_strtoint(key,num_key)
pt=input("ENTER PLAIN TEXT\t")
ct=encryption(pt,key,num_key)
#decryption
dec_pt=decrypt(num_key,ct)

p = f"""
KEY:
    {key},{num_key}
ENCRYPTION
    plain-text {pt}
    cipher-text {ct}
DECRYPTION:
    text {dec_pt}

"""
print(p)
