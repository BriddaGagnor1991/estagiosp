def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Inicia a sequência com 0 e 1
    while fib_sequence[-1] < n:  # Gera a sequência até o número informado
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def check_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Entrada do usuário
numero = int(input("Informe um número: "))
resultado = check_fibonacci(numero)
print(resultado)
