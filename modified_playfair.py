import string
import numpy as np
def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def diagram(pt):
    i=0
    list=[]
    while i<len(pt):
        if i == len(pt)-1:
            new_pt=pt[i]+'x'
            list.append(new_pt)
            break 
        
        if pt[i] == pt[i+1]:
            new_pt=pt[i]+'x'
            list.append(new_pt)
            i+=1
        else:
            new_pt=pt[i]+pt[i+1]
            list.append(new_pt)
            i=i+2
    return list

def update_key(key):
    new_key=[]
    for k in key:
        if k not in new_key:
            new_key.append(k)
    return new_key


def alphabet(str,new_key):
    
    list=[i for i in str]
    list.remove('j') 
    abc=list.copy()    #reference by value
    for l in list:
        if l in new_key:
            abc.remove(l)
    return(abc)

def change_row(m,p1):
            index=np.where(m==p1)
            i=index[0][0]
            if i < 4:
                return m[i+1]
            else:
                return m[0]

def change_column(c,key_matrix,p1,p2):
    for i in range(0,5):
        if key_matrix[i][c]  == p1:
            if i == 4:
                rp1=key_matrix[0][c]
            else:   
                rp1=key_matrix[i+1][c]
        elif key_matrix[i][c] == p2:
            if i == 4:
                rp2=key_matrix[0][c]
            else:   
                rp2=key_matrix[i+1][c]
    return rp1+rp2
def which_column(key_matrix,p1,p2,updated_pt):
                cc=0
                sc=0
                for c in range(0,5):
                    for r in range(0,5):
                        if key_matrix[r][c] == p1  or key_matrix[r][c] ==p2:
                            sc+=1
                            if sc == 2:
                                updated_pt.append(change_column(c,key_matrix,p1,p2))
                                cc=1
                                return updated_pt,cc
                                
                    sc = 0
                return updated_pt,cc
def rectangle_swap(p1,p2,key_matrix):
    for r in range(0,5):
        for c in range(0,5):
            if key_matrix[r][c] == p1:
                rp1=r
                cp1=c
            elif key_matrix[r][c] ==p2:
                rp2=r
                cp2=c
    p1=key_matrix[rp1][cp2]
    p2=key_matrix[rp2][cp1]
    return p1+p2
        
def update_matrix(key_matrix,new_pt):
    updated_pt=[]
    cr=0
    cc=0
    for p in new_pt:
        p1=p[0]
        p2=p[1]
        for m in key_matrix:
            if p1 in m and p2 in m:    #for row swapping
                p1=change_row(m,p1)
                p2=change_row(m,p2)
                updated_pt.append(p1+p2)
                cr=1
            #column swap
        if cr !=1:
            updated_pt,cc=which_column(key_matrix,p1,p2,updated_pt)
            #print(cc)
        #rectangle swap
        if cr !=1 and cc!=1:
            updated_pt.append(rectangle_swap(p1,p2,key_matrix))
        cr=0
        cc=0    
                
        

    return updated_pt
            


pt=input("enter plain text")
new_pt=diagram(removespace(pt))
key=input("ENTER KEY: ")
new_key=update_key(key) 
str=string.ascii_lowercase
atoz=alphabet(str,new_key)    #list of alphabets without key's letters

matrix=new_key+atoz
key_matrix=np.array(matrix).reshape(5,5)
print(key_matrix)

ct=update_matrix(key_matrix,new_pt)
print(f"""
PLAIN TEXT: {pt}
key: {key}
KEY MATRIX: {key_matrix}
CIPHER TEXT: {ct}
""")
