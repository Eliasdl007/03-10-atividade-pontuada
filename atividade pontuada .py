import os
import time
""""
Jonatas Fernandes Dos Santos
Jose Elias lima Pereira
"""
# Limpar a tela
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    genero: str
    salario: float  


nome_do_arquivo = "pesquisa_de_abitantes.txt"  
lista_pessoa = []

while True:
    opcao = int(input("""
====digite a opção====                 

|1|adicionar pessoas
|2|exibir resultado
|3|sair 
"""))

    match opcao:
        case 1:
            
            pessoa = Pessoa(
                nome=input("digite seu nome: "),
                idade=int(input("digite sua idade: ")),
                genero=input("digite seu genero: "),
                salario=float(input("digite seu salario: "))  # Convertendo para float
            )

            lista_pessoa.append(pessoa)

            
            with open(nome_do_arquivo, "a") as arquivo_de_pessoa:
                arquivo_de_pessoa.write(f"nome:{pessoa.nome},idade:{pessoa.idade},genero:{pessoa.genero},renda mensal:{pessoa.salario}\n")  # Adicionando nova linha
            
            print("Dados salvos.")

        case 2:
            print("\n=== Exibindo resultado===")
            try:
                with open(nome_do_arquivo, "r") as arquivo_de_origem:
                    for linha in arquivo_de_origem:
                        
                        nome, idade, genero, salario = linha.strip().split(",")
                     
                        print(f"Nome: {nome.split(':')[1]}, Idade: {idade.split(':')[1]}, Gênero: {genero.split(':')[1]}, Salário: {salario.split(':')[1]}")
            except FileNotFoundError:
                print("Arquivo não encontrado. Adicione pessoas primeiro.")
        
        case 3:
            break


