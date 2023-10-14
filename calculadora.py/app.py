def somar(a: float, b:float) -> float:
   return a + b
def subtracao(a: float, b:float) -> float:
   return a - b
def multiplicacao(a: float, b:float) -> float:
   return a * b
def divisao(a: float, b:float) -> float:
   return a / b

while True:
    operacao = input("""Digite a operação desejada [-]Subtraçao
                       [+] Adicao
                       [/] Divisao
                       [*] multiplicação: """).lower()
    
    valor1 = float(input("Digite um valor: "))
    valor2 = float(input("Digite outro valor: "))
    
    if operacao == "-":
        print(f"{valor1} - {valor2} = {subtracao(valor1,valor2)}")
    elif operacao == "+":
        print(f"{valor1} + {valor2} = {somar(valor1,valor2)}")
    elif operacao == "/":
            print(f"{valor1} / {valor2} = {divisao(valor1,valor2)}")
    elif operacao == "*":
        print(f"{valor1} * {valor2} = {multiplicacao(valor1,valor2)}")
    
    continuar = input("Deseja fazer outra operação [s]Sim: [n]Não:  ").lower()
    if continuar == "n":
        break