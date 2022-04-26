print('Bem-vindo a calculadora')
print('USE "/" para dividir')
print('USE "*" para multiplicar')
print('USE "+" para somar')
print('USE "-" para subtrair')
sair = False

while not sair:
      print()
      n1 = input('Digite o 1º Numero: ')
      operador = input('Digite o que deseja fazer: ')
      n2 = input('Digite o 2º Numero: ')

      try:
            n1 = int(n1)
            n2 = int(n2)

      except:
            print()
            print('Deve ser somente numeros')
            continue

      resultado = n1 / n2 if operador == '/' else print('Operador invalido')
      resultado = n1 * n2 if operador == '*' else print('Operador invalido')
      resultado = n1 + n2 if operador == '+' else print('Operador invalido')
      resultado = n1 - n2 if operador == '-' else print('Operador invalido')


      print(resultado)




