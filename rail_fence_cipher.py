import numpy as np
def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def no_of_cols(pt,dep):
    if len(pt) % dep != 0:
        return (len(pt)+1)//dep
    else:
        return (len(pt))//dep
def create_matrix(mat,pt,dep):
    if len(pt)% dep != 0:
        pt+='x'
    p=0
    r=np.shape(mat)[0]
    c=np.shape(mat)[1]
    for i in range(c):
        for j in range(r):
            mat[j][i]=pt[p]
            p+=1

    ct=""
    for x in range(r):
        c=mat[x]
        for i in c:
            ct+=i
    return ct
def decrypt(dec_mat,ct):
    p=0
    pt=""  
    r=np.shape(dec_mat)[0]
    c=np.shape(dec_mat)[1]
    for i in range(r):
        for j in range(c):
            dec_mat[i][j]=ct[p]
            p+=1

    for i in range(c):
        for j in range(r):
            pt+=dec_mat[j][i]
    return pt

pt=input("Enter Plain Text")  
new_pt=removespace(pt)
dep=int(input("Enter depth"))
col=no_of_cols(new_pt,dep)
mat=np.empty([dep,col],str)
ct=create_matrix(mat,new_pt,dep)
print(f"""
PLAIN TEXT: {pt}
DEPTH: {dep}
CIPHER TEXT: {ct}
""") 
#DECRYPTION
c=len(ct)//dep
dec_mat=np.empty([dep,c],str)
dec_pt=decrypt(dec_mat,ct)
print(f"""
CIPHER TEXT: {ct}
PLAIN TEXT: {dec_pt}
""")

