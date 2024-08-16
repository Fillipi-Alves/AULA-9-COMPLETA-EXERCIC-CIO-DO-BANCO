# # AULA 9 - Loop for | While | Funções

#  Funções
# Argumento
# Sem argumento
# [Com](http://4.3.3.com/) Retorno
# Sem retorno

# Loop For

# Loop while

# Laços  for  while

# É fundamental que o aluno compreenda com profundidade os conceitos dos laços de repetição em Python. Nesta lição, examinaremos os laços `for` e `while`, explorando suas funcionalidades e aplicações por meio de exemplos práticos. É crucial dominar tais ferramentas para processar grandes conjuntos de dados, tarefa essencial em análises quantitativas e ciência de dados. Algumas vezes, repetiremos operações simples em poucos elementos; outras, percorreremos milhares de registros em busca de respostas. Seja qual for o cenário, os laços nos permitem automatizar fluxos e obter resultados de maneira elegante. 

# ```python
# ### 1. Laço `for`

# # Estrutura Básica

# for i in range(5):
#     print(i)

# # Iterando Sobre Listas

# frutas = ["maçã", "banana", "cereja"]
# for fruta in frutas:
#     print(fruta)
# # iteração == percorrendo o código

# # Iterando com Índices Usando `enumerate()`

# frutas = ["maçã", "banana", "cereja"]
# for indice, fruta in enumerate(frutas):
#     print(indice, fruta)

# # Iterando Sobre Dicionários

# dados = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
# for chave, valor in dados.items():
#     print(f"{chave}: {valor}")
# time

# # List Comprehensions

# quadrados = [x**2 for x in range(10)]
# print(quadrados)

# # 2. Laço `while`

# # Estrutura Básica

# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1

# # Laço `while` com Condicional

# numero = 10
# while numero > 0:
#     print(numero)
#     numero -= 1
# print("Feliz Ano Novo!")

# ## 3. Controle de Fluxo em Laços

# #### `break`

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# #### `continue`

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# ## `else` em Laços

# for i in range(5):
#     print(i)
# else:
#     print("Laço concluído.")
    
# ## 4. Combinando `for` e `while` com Condicionais

# #### Filtrando Dados em List Comprehensions

# numeros = range(10)
# pares = [x for x in numeros if x % 2 == 0]
# print(pares)  # [0, 2, 4, 6, 8]

# ### Condicional em `while`

# numero = 10
# while numero > 0:
#     if numero == 5:
#         break
#     print(numero)
#     numero -= 1

# ### 6. Práticas Avançadas

# ## Usando `zip()` para Iterar em Paralelo

# nomes = ["Alice", "Bob", "Charlie"]
# idades = [25, 30, 35]
# for nome, idade in zip(nomes, idades):
#     print(f"{nome} tem {idade} anos")

# # Usando `itertools` para Iterações Complexas

# from itertools import product

# # Produto cartesiano de dois conjuntos
# for a, b in product([1, 2, 3], ['a', 'b']):
#     print(a, b)
# ---------------------------------------

# print('Sistema - E-commerce')
# print('Cadastre-se')
# senha =  input('cadastre sua senha:')
# login  =  input('Digite seu login')

# login_user = input('Login do usuário')
# senha_user = input('Digite a senha')

# carrinho = []
# preco = []

# for n in range(1,4):
#     if senha == senha_user and login_user == login :
#         print('Acesso autorizado')
#         produtos  = {
#           'aviao':150000.00,
#           'carro': 200.00,
#           'trator':15000.00
#         }
        
  
#         for n  in range(1,4): 
#             escolha  =  input('escolha o produto')
#             carrinho.append(escolha)
#             preco.append(produtos[escolha])
#             print(carrinho)
#             print('R$', preco)
    
        
#     else: 
#         print('Acesso negado, clique em esqueci minha senha ')    
#         break
 
#  sair  =  input('Enter para sair')
 
#  ----------------------------------
 
 
#  for a in range(1,11):
#     n = int(input('Digite o multiplicador')) 
#     for x in range(0,11):
#         result = x * n
#         print(x, 'X',n, '=', result )
        
#      -------------------------------------
     
     
     
# c = 1
# quant_notas = int(input('--'))
# while  c <= quant_notas:
#        lista_portugues = []
#        lista_matematica = []
#        n1,n2,n3,n4,n5 = int(input('>>')), int(input('>>')), int(input('>>')), int(input('>>')),int(input('>>'))
#        lista_matematica.extend([n1,n2,n3,n4,n5])
#        lista_portugues.extend([n1,n2,n3,n4,n5])
#        print('mat', lista_matematica, 'port', lista_portugues, 'TRIMESTRE: ', c)
       
#        c += 1   
       
       
# lista =  [1,5,6,610,20]
# soma = 0
# for n in lista:
#     soma =  soma + n
# print('=',soma) 
        
# ```

# ```python
# Crie um sistema de banco, com as seguintes operações:

# # SISTEMA DE BANCO 

# - Acesso a conta
# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 

# # JOGO DE ADVINHAÇÃO

# import random

# numero_aleatorio = random.randint(1,20)

# lista =  [2,1,0]
# for chances in lista:
#     chute  =  int(input('Escolha um número:'))
#     print('Você tem ', chances, 'chances')
#     if chute ==  numero_aleatorio:
#         print('acertou' )
#         break
#     else:
#         print('tente novamente, vc tem: ', chances, 'chances')
#         if chances == 0:
#             print('Suas chances esgotaram ')
#             break

# ```

# ***Transforme seu sistema em Executável:***

# ***Vamos utilizar a biblioteca `auto-py-to-exe`***

# ***Acesse o `CMD` (tela preta)***

# ***Windows + r, digite `cmd`***

# ***Vamos utilizar o `pip`, que é o gerenciador de pacotes*** 

# ***1 - Instalar o `auto-py-to-exe`***

# ```python
# pip install auto-py-to-exe
# ```

# ***2 - Chama para funcionar no cmd mesmo***

# ```python
# auto-py-to-exe
# ```

# ***3  -  Clique no botão para encontrar a raiz do projeto***

# ***4 -   Clique em `file`***

# ***5 -   Clique em `Convert`***

# ***6 -   Projeto pronto***

# ***6.2 - Clique em Open***

# ***7 -  Clique `2 x` no arquivo para verificar se estar funcionando corretamente.***

# DOCUMENTAÇÃO RANDOM

# https://docs.python.org/pt-br/3/library/random.html

# # DEF → É A PALAVRINHA QUE USAMOS PARA CRIAR UMA FUNÇÃO

# # `DEF NOME DA FUNÇÃO():`

# # `AÇÃO AQUI`

# ### Funções em Python são blocos de código reutilizáveis que realizam uma tarefa específica. Elas permitem que você encapsule um conjunto de instruções em um único nome e a execute quando necessário. Funções em Python têm várias finalidades, desde a organização de código até a reutilização de lógica.

# ### Definindo uma função:

# Você pode definir uma função em Python usando a palavra-chave `def`, seguida do nome da função e parênteses `()`. Os parâmetros (argumentos) da função, se houver, são listados entre os parênteses. A definição da função é seguida por um bloco de código indentado que define o comportamento da função.

# ```jsx

# def display():
#     print('hello')

# display()

# def saudacao(nome):
#        """Esta função saúda o usuário pelo nome."""
#     print(f"Olá, {nome}!")

# saudacao("Pedro")
# #Resultado:  Olá,  Pedro 

# ```

# ### Chamando uma função:

# Para chamar uma função, basta usar o nome da função seguido pelos parênteses contendo os argumentos, se houver. No exemplo acima, podemos chamar a função `saudacao` da seguinte forma:

# ```jsx
# saudacao("Alice")  # Saída: Olá, Alice!
# ```

# [Calculadora básica](https://www.notion.so/Calculadora-b-sica-91930d96c2cb4d7d8f217cf5b7a55149?pvs=21)

# [Desafio caixa](https://www.notion.so/Desafio-caixa-a75a569791214324849b92fb53f98b5d?pvs=21)

# ```python

# def soma(a, b):
#     """Esta função retorna a soma de dois números."""

#     resultado = a + b
#     return resultado

# #Você pode chamar a função `soma` e atribuir seu resultado a uma variável:

# resultado_soma = soma(5, 3)  # resultado_soma agora contém 8

# ****************************************************

# **ATIVIDADE:**

# CRIE UM SISTEMA DE UM BANCO.
# OPERAÇÕES DO BANCO: 

# *SAQUE()
# DEPOSITO()
# VISUALIZAR_STATUS()

# BOCA_DO_CAIXA()*

# ***************************************************

# **FUNÇÕES COM RETORNO

# Em Python as funções com retorno são aquelas que executam 
# uma determinada 
# operação e retornam um valor específico após o processamento. 

# def soma(a, b):
#     resultado = a + b
#     return resultado

# Chamando a função e atribuindo o resultado a uma variável
# resultado_soma = soma(3, 5)
# print("O resultado da soma é:", resultado_soma)

# Neste exemplo, a função `soma` recebe dois argumentos A E B, calcula sua soma,
# e retorna o resultado. O valor retornado é então atribuído a uma variável resultado_soma 
# e é impresso na tela.

# As funções com retorno são úteis quando você precisa calcular algo e usar esse 
# resultado em outro lugar do seu código.

# FUNÇÕES EM RETORNO

# Uma função sem retorno em Python é uma função que realiza uma tarefa sem retornar 
# um valor específico. Em vez disso, ela pode apenas realizar operações, 
# processamento de dados ou outras tarefas e, em seguida, terminar sua execução. 

# Aqui está um exemplo simples de uma função sem retorno em Python:

# def saudacao(nome):
#     print("Olá, " + nome + "! Bem-vindo.")

# saudacao("João")

# Neste exemplo, a função saudacao, recebe um nome como argumento e imprime uma 
# saudação na tela. No entanto, ela não retorna nenhum valor específico.

# As funções sem retorno são úteis quando você precisa realizar tarefas específicas: 
# como imprimir na tela, atualizar variáveis globais, modificar estruturas de dados, 
# entre outras coisas, sem necessariamente precisar de um valor de retorno.**

# ```

# [Resolução ](https://www.notion.so/Resolu-o-2e2dd7ef3f584a9e9b2d6a791a06d270?pvs=21)





# for n in range(1,11):
#   print(n)

# # LISTAS 
# # variaveis do tipo string texto
# # conjuntos
# # tuplas
# # dicionarios
# # estruturas compostas


#   python= 'PYTHON'
#   numero = 12123123
# numero_float= 1.32222

# for n2 in python:
#      print(n2) 

# for n2 in numero:
#     print(n2)

# lista= ['a','b','c']
# for var in lista: 
#     print(var)


# for variavel_vazia in list(range(1,11))
#     print(variavel_vazia)

# for n in range(1,4):
#     nome= innput(f'digite seu nome N´{n}')
    
# for numero2 in range(1,22,10):
#     print(numero2)

# lista= [1,2,3,6,6]

# soma= 0
# for numero2 in lista:
#   soma = soma + numero2
#   print('total=', soma)



# dicionario = {
#     "menino" : "Fillipi",
#     "idade" : 16,
#     "endereço" : "Rua Andorinha305",}

# print(dicionario["idade"])

# for valor in dicionario.keys():
#      print(valor)

# #ATIVIDADE BANCO

# for numero in range(1,4):
#     print('Digite o nome de usuário')
#     nome = input ('Nome Do Usuário >>> ')
#     idade = input ('Idade >>> ')
#     endereço = input ('Endereço >>> ')
#     profissão = input ('Profissão >>> ')

#     print(f'''

#      NOME - {nome}
#      IDADE - {idade}
#      ENDEREÇO -{endereço}
#      PROFISSÃO - {profissão}
# ''')
    

# #SISTEMA DE CADASTRO
#     import random


# numero_aleatorio = random.randint(0,3)

# listta - [,3,2,1]
# for chances in lista
# chute = input("Escolha um número:")
# print("Voce tem", chances, "chances")
#     if chute == numero_aleatorio
#         print("Acertou")
#         break
# else:
# for chances in range(1,5):


# #SISTEMA DE BANCO USANDO VARIAVEIS
# print('Sistema - Itaú')
# print('Cadastre-se')
# senha =  input('cadastre sua senha:')
# login  =  input('Digite seu login')


# login_user = input('Login do usuário')
# senha_user = input('Digite a senha')


# import random


# valor_em_conta = random.randint(100,2000)
# valores = [valor_em_conta]
# def saque():

#     valor_de_saque = float(input('Digite o valor de saque: '))
#     saldo = valor_em_conta - valor_de_saque
#     print('você sacou R$ ', valor_de_saque,'Saldo é R$', saldo)

# def deposito():

#     valor_de_saque = float(input('Digite o valor de saque: '))
#     saldo = valor_em_conta + valor_de_saque
#     valores[0] = saldo
#     print('você sacou R$ ', valor_de_saque,'Saldo é R$', valores)

# def visualizar():
#     print(f'''
#     Seu saldo é R$:
#     {valor_em_conta}

#     ''')

# def banco():

#     print(f'''
#     Digite 1 para visualizar o saldo
#     Digite 2 para saque
#     Digite 3 para deposito
#     ''')
#     escolha  =  input('escolha a operação: ')
#     if escolha == '1':
#      visualizar()
#     elif escolha  == '2':
#        saque()
#     elif escolha  == '3':
#          deposito()
   
#     else:
#         print('Digite algo valido')

# while True:
    #   banco()
 
# #EXERCICÍO DO BANCO CORRETO

# import random

# SENHA = 12
# CONTA = 1
# VALOR = random.randint(100,1000)

# for n in range(0,3):
#     print('Digite seu acesso:')
#     conta = int(input('Conta:'))
#     senha = int(input('senha:'))
#     if senha ==  SENHA and conta  == CONTA:
#        print('Acesso autorizado')
#        print('''
#             (1) deposito
#             (2) saque
#             (3) ver extrato  
       
#        ''') 
#        opcao = input('>>')   
#        if  opcao == '1':
#            valor_depositado = float(input('R$ >>'))
#            VALOR =  VALOR + valor_depositado
#            print('O valor foi depositado - R$', float(VALOR))
#            for n in range(2):
#                print('deseja voltar ao sistema? s/n')
#                s_n = input('>>')
#                if s_n == 's':
#                   print('Até logo') 

#        elif opcao == '2':
#            valor_sacado = float(input('R$ >>'))
#            if VALOR < valor_sacado:
#               print('SALDO INSUFICIENTE')
#               for n in range(2):
#                   print('deseja voltar ao sistema? s/n')
#                   s_n = input('>>')
#                   if s_n == 's':
#                      print('Até logo') 
#            else:     
#               VALOR =  VALOR - valor_sacado
#               print('O valor foi sacado - R$', float(VALOR))  
#               for n in range(2):
#                   print('deseja voltar ao sistema? s/n')
#                   s_n = input('>>')
#                   if s_n == 's':
#                      print('Até logo')                     
           
#        elif opcao == '3':
#             print('R$', float(VALOR)) 
#        break

#     else:
#         print('Não autorizado')

# n = input('clique enter sair')
