#dd55f
def choice_operator():
    acepted_operator = False
    while not acepted_operator:
        operator = input('selecione a operação... 1 para adição; 2 para subtração; 3 para divisão; 4 para multiplicação: ')
        if operator in ('1','2','3','4'):
            return operator
            acepted_operator = True
        else:
            print('Você digitou um numero errado, tente novamente')


def choice_numbers():
    acepted_numbers = False
    while not acepted_numbers:
        num1 = input('primeiro numero: ')
        num2 = input('segundo numero: ')
        if num1.isnumeric() and num2.isnumeric():
            return num1, num2
            
            acepted_numbers = True
        else:
            print('você não digitou numeros tente novamente')


def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multipli(x, y):
    return x * y



finished = False
while not finished:
    result = 0
    operator = choice_operator()
    num1, num2 = choice_numbers()
    if operator == '1':
        print('o resultado é: ', add(int(num1),int(num2)))
    elif operator == '2':
        print('o resultado é: ', substract(int(num1), int(num2)))
    elif operator == '3':
        print('o resultado é: ', divide(int(num1), int(num2)))
    elif operator == '4':
        print('o resultado é: ', multipli(int(num1), int(num2)))
    
    print('fim')
    finished = True


