
from colorama import Fore

def calcularadora ():
 return calcularadora
print(Fore.BLUE +'Olà seja bem vindo(a) a cauculadora')

while True:
 cauculos_feitos = 0 
 for numbers in range(2):
     numbers =    float( input(Fore.GREEN + f'Digite o { numbers+ 1}º numero:  '))

 print(Fore.BLUE + '''Digite o tipo de operaçäo que deseja fazer
           [+] Adiçäo
           [-] Subtraçäo
           [/] Divisäo
           [x] Multiplicaçäo
           
           ''')
 cauculo = input('-> ').upper()
 

 if cauculo == '+':
  print(Fore.GREEN +f'O resultado è {numbers + numbers:.2f}')
 elif cauculo == '-':
  print(Fore.GREEN +f'O resultado è {numbers - numbers:.2f}')
 elif cauculo == '/':
  print(Fore.GREEN +f'O resultado è {numbers / numbers:.2f}')

 elif cauculo == 'X':
  print(Fore.GREEN +F'O resultado è {numbers * numbers:.2f}')
 else:
  print('Operaçao invalida')

 print('Deseja continuar os cauculos? S/N').upper()
 opçao = input('-> ')

 if opçao == 'S'and opçao =='sim':
  print('Obrigado por ter usado')
  break
 else:
  cauculos_feitos +=1

