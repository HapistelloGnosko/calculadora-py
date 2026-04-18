def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

operacoes = {
    "1": ("Somar",       somar),
    "2": ("Subtrair",    subtrair),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir",     dividir),
}

def main():
    print("=== Calculadora ===")
    while True:
        print("\n1. Somar\n2. Subtrair\n3. Multiplicar\n4. Dividir\n0. Sair")
        escolha = input("\nEscolha: ").strip()

        if escolha == "0":
            print("Saindo...")
            break

        if escolha not in operacoes:
            print("Opção inválida.")
            continue

        try:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        nome, func = operacoes[escolha]
        resultado = func(a, b)
        print(f"\nResultado: {resultado}")

if __name__ == "__main__":
    main()
