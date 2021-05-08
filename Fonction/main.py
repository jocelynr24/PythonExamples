# Définition de la fonction calculatrice
def calculatrice(param1, param2, operation):
    if(operation == "+"):
        resultat = param1 + param2
    elif(operation == "-"):
        resultat = param1 - param2
    elif(operation == "*"):
        resultat = param1 * param2
    elif(operation == "/"):
        resultat = param1 / param2
    return " ".join([str(param1), operation, str(param2), "=", str(resultat)]) 

# Appels de la fonction calculatrice
# 10 + 10 = 20
print(calculatrice(10, 10, "+"))
input()
# 50 - 10 = 40
print(calculatrice(50, 10, "-"))
input()
# 10 * 10 = 100
print(calculatrice(10, 10, "*"))
input()
# 40 / 2 = 20.0
print(calculatrice(40, 2, "/"))