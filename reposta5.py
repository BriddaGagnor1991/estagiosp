# Função para inverter a string
def inverter_string(s):
    # Inicializa uma variável para armazenar a string invertida
    string_invertida = ""
    
    # Loop que percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Testando a função
texto = input("Digite uma string: ")
resultado = inverter_string(texto)
print(f"String invertida: {resultado}")
