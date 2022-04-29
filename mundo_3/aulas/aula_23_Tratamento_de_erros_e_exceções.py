"""
 Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
 Aprenda como usar a estrutura try except no Python de uma forma simples.
"""

"""
execption

"""
#comando try, except
"""
try:
    operação
    
except:
    falhou
    
else:
    se deu certo

finally:
    certo/falha
    
 Um try pode ter varios exceptions, assim como um if pode ter vários elifs
"""
try:
    a = int(input('Numerador: '))
    b = int(input('denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero! ')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrador foi {erro.__cause__}')
except:
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')