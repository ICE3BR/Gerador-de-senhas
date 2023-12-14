import random
import string

def gerar_senha(comprimento=12, use_minusculas=True, use_maiusculas=True, use_numeros=True, use_especiais=True):
    # Define os caracteres possíveis para cada categoria
    letras_minusculas = string.ascii_lowercase if use_minusculas else ''
    letras_maiusculas = string.ascii_uppercase if use_maiusculas else ''
    numeros = string.digits if use_numeros else ''
    especiais = string.punctuation if use_especiais else ''

    # Combina todos os caracteres possíveis
    caracteres = letras_minusculas + letras_maiusculas + numeros + especiais

    # Verifica se pelo menos um tipo de caractere está ativado
    if not caracteres:
        raise ValueError("Pelo menos uma categoria de caractere deve ser ativada")

    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

    return senha

# Exemplo de uso:
senha = gerar_senha(comprimento=12, use_minusculas=True, use_maiusculas=True, use_numeros=True, use_especiais=True)
print(senha)