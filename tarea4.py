#1
def valores_ascendentes(dict):
    lista = list(dict.values())
    lista_ordenada = sorted(lista)
    for x in lista_ordenada:
        print(x)
#2
def comparar_dict(dict1,dict2):
    for x in dict1:
        if x in dict2:
            if dict1[x] == dict2[x]:
                print(f"llave del segundo diccionario = {x} valor = {dict1[x]}")
            else:
                print(f"La llave: {x} no corresponde al mismo valor que el primer diccionario")
        else:
            print(f"llave  = {x} no esta en el diccionario 2")
    for x in dict2:
        if x in dict1:
            None
        else:
            print(f"La llave {x} de valor {dict2[x]} no esta en el primer diccionario")
#3
def mezclar_diccionarios(dict1,dict2):
    dict3 = dict2
    for x in dict1:
            dict3[x] = dict1[x]
    print(dict3)
#4 def datos_personas(dict1, dict2, dict3)