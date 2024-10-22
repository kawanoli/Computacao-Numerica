dicionário_bases = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    'g': 16,
    'h': 17,
    'i': 18,
    'j': 19,
    'k': 20,
    'l': 21,
    'm': 22,
    'n': 23,
    'o': 24,
    'p': 25,
    'q': 26,
    'r': 27,
    's': 28,
    't': 29,
    'u': 30,
    'v': 31,
    'w': 32,
    'x': 33,
    'y': 34,
    'z': 35
}

def pegaBase():
    base_inicial = int(input("Digite a base inicial (entre 2 e 36): "))
    while base_inicial < 2 or base_inicial > 36:
        print("Base inválida! Por favor, escolha uma base entre 2 e 36.")
        base_inicial = int(input("Digite uma base inicial válida (entre 2 e 36): "))

    num_inicial = input(f"Digite o número na base {base_inicial}: ")
    base_final = int(input("Digite a base para a qual deseja converter (entre 2 e 36): "))
    while base_final < 2 or base_final > 36:
        print("Base inválida! Por favor, escolha uma base entre 2 e 36.")
        base_final = int(input("Digite uma base para a qual deseja converter que seja válida (entre 2 e 36): "))

    return base_inicial, num_inicial, base_final

base_inicial, num_inicial, base_final = pegaBase()
print(f"Base inicial: {base_inicial}, Número: {num_inicial}, Base de destino: {base_final}")

def converteBase(num_inicial, base_inicial, base_final, dicionário_bases):
    current_value = []

    # Checa se o primeiro algarismo é zero e começa a conversão a partir do segundo
    for char in num_inicial:
        if char in dicionário_bases:
            current_value.append(dicionário_bases[char])

    result = []

    while current_value:
        next_value = []
        carry = 0

        for digit in current_value:
            carry = carry * base_inicial + digit
            if carry >= base_final:
                next_value.append(carry // base_final)
                carry = carry % base_final
            elif next_value:  # Adiciona 0 se houver dígitos já
                next_value.append(0)

        # Se o next_value estiver vazio, não adiciona carry ao result
        if not next_value and carry == 0:
            break

        if carry > 0:
            result.append(carry)
        if carry == 0:
            result.append(carry)

        current_value = next_value or [0]  # Garante que current_value não fique vazio

    # Converter a lista de resultados para a base correta
    result_str = []
    for value in reversed(result):
        if value < 10:
            result_str.append(str(value))
        else:
            result_str.append(chr(value - 10 + ord('a')))

    return ''.join(result_str)

result = converteBase(num_inicial, base_inicial, base_final, dicionário_bases)
print(f"O número {num_inicial} na base {base_inicial} é {result} na base {base_final}.")