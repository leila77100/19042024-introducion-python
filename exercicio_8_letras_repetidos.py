
frase= input("dime un texto")
letra_dict= dict()


for i in frase:
    
    if i in letra_dict:
        letra_dict[i] = letra_dict[i]+1
    else:
        letra_dict[i] = 1

print(letra_dict)