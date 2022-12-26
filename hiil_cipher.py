def removespace(pt):
    new_pt=""
    for i in pt:
        if i==" ":
           continue
        else:
            new_pt=new_pt+i
    return new_pt
def filler(pt):
    while len(pt) %3 !=0:
        pt+='x'
    return pt
def build_kmatrix(key,mapping):
    #build 3*3 matrix
    num_key=[]
    for k in key:
        num_key.append(mapping[k])
    key_matrix=np.array(num_key).reshape(3,3)   
    return key_matrix
def encryption(pt,mapping,key_matrix):
    pt=filler(pt)
    #plaintext into matrix form
    num_pt=[]
    for p in pt:
        num_pt.append(mapping[p])
    pt_array=np.array(num_pt)
    pt_split=np.split(pt_array,len(pt_array)//3)    #split into rows..
    
    #for multiplication
    multi=[]
    for i in range(len(pt_split)):
        multi.append(np.matmul(pt_split[i],key_matrix) % 26)

    #multi = [array([ 1, 24, 14], dtype=int32), array([14, 13, 14], dtype=int32)]
    #for conactinating all indices into one list [1,24,14,14,13,14]
    ct_list=[]
    conact_array=np.concatenate(multi)

    for c in conact_array:
        ct_list.append(reverse_mapping[c])
    #list to string
    ct=""
    for c in ct_list:
        ct+=c
    print(f"""
    PLAIN TEXT: {pt}
    NUMBERED PLAIN TEXT: {num_pt}
    KEY: {key}
    KEY MATRIX: {key_matrix}
    CIPHER TEXT: {ct}

    """)
    return ct
def decryption(ct,key_matrix,mapping,reverse_mapping):
    #we have to find inverese of key matrix
 
    det=round(np.linalg.det(key_matrix))
 
    adj=np.linalg.inv(key_matrix) * det

    key_inverse=(pow(det,-1,26)*adj) %26

    num_ct=[]
    for c in ct:
        num_ct.append(mapping[c])
    ct_array=np.array(num_ct)
    ct_split=np.split(ct_array,len(ct)//3)
    multi=[]
    for i in range(len(ct_split)):
        multi.append(np.matmul(ct_split[i],key_inverse) % 26)
    concat_array=np.concatenate(multi)
    new_pt=[]
    for i in concat_array:
        new_pt.append(reverse_mapping[round(i)])
    print(f"""
    CIPHER TEXT: {ct}
    NUMBERED CIPHER TEXT: {num_ct}
    INVERSE OF KEY: {key_inverse}
    DECRYPT PLAIN TEXT:{new_pt}
    """)

       

import numpy as np

pt=input("ENTER PLAIN TEXT:\t")
pt=pt.lower()
pt=removespace(pt)
key=input("ENTER KEY:\t")
mapping={}
for i in range(97,97+26):
    mapping[chr(i)]=i-97
reverse_mapping={}
for i in range(97,97+26):
    reverse_mapping[i-97]=chr(i)
key_matrix=build_kmatrix(key,mapping)
ct=encryption(pt,mapping,key_matrix)
#fro decryption
decryption(ct,key_matrix,mapping,reverse_mapping)
