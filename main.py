import numpy as np
def assign_alphabets(): #creates a dictionary with all the alphabets A-Z and assigns them a value from 1 to 26
    a=ord("A")
    alphatonum = dict()
    for key in range(1,27):
        keys=chr(a)
        values=key
        a += 1
        alphatonum.__setitem__(keys,values)
    return alphatonum
def assign_numeric_value(userinput): #Encodes the given string into a numeric list 
    ml=[]
    listuser = list(userinput)
    for i in range(len(listuser)):
        for j in assign_alphabets().keys():
            if listuser[i].upper()==j:
                ml.append(assign_alphabets().__getitem__(j))
            elif listuser[i]==' ':
                ml.append(0)
                break
    if len(ml)%3!=0: # making sure that the list is a multiple of 3 
        ml.append(0)
        if len(ml)%3!=0:
            ml.append(0)
    return ml

def get_nonsingular_matrix(): # generates a random non singular matrix
    flag=False
    while flag==False:
        arr = np.random.randint(10, size=(3, 3))
        if np.linalg.det(arr) != 0:
            flag=True
        else:
            flag=False
    return arr.astype(int)
def msg_encoder(): #Encodes the message into a matrix (row,3)
    global array1
    global userinput
    userinput=input("Please enter a message to encode: ")
    array1 =np.array(assign_numeric_value(userinput))
    row=len(array1)//3
    originalmsg=(array1.reshape(row,3)).astype(int)
    return originalmsg

def decoded_msg(): #Decodes the matrix generated in the previous function and gets the original user input
    ml=[]
    g = get_nonsingular_matrix()
    encoded_matrix = np.matmul(msg_encoder(), g)
    decoded_matrix = np.matmul(encoded_matrix, np.linalg.inv(g))
    decoded_matrix2 = (decoded_matrix.round()).astype(int)
    decoded_matrix3 = decoded_matrix2.reshape(1, len(array1))
    decoded_matrix3.tolist()
    val_list=list(assign_alphabets().values())
    keys_list=list(assign_alphabets().keys())
    for i in range(len(decoded_matrix3[0])):
        for j in assign_alphabets().values():
            if decoded_matrix3[0][i]==j:
                val=val_list.index(j)
                ml.append(keys_list[val])
            elif decoded_matrix3[0][i]==0:
                ml.append(" ")
                break
    return ("".join(ml)).capitalize()

print(f"Decoded Message: {decoded_msg()}")
