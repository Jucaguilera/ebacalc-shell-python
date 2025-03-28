def calcular():
    while True:
        print("Bem vindo à Ebacalc, a calculadora do aluno Lucas! \nSelecione a operação:")
        print("Digite + para Adição")
        print("Digite - para Subtração")
        print("Digite * para Multiplicação")
        print("Digite / para Divisão")
        print("Para sair, digite 'sair'.")

        operacao = input("Digite a operação desejada: ")

        if operacao == 'sair':
            print("Obrigado por usar a calculadora do Lucas! Saindo..")
            break



        if operacao not in ('+', '-', '*', '/'):
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira um número válido!")
            continue

        if operacao == '+':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif operacao == '-':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif operacao == '*':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")

        print("-")

if __name__ == "__main__":
    calcular()