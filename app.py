import imp
from colorama import Fore

def caucularadora ():
 return caucularadora
print(Fore.BLUE +'Olà seja bem vindo(a) a cauculadora')
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
 print( Fore.RED+'operaçäo INVALIDA ')
