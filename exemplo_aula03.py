#Crie um dicionário para armazenar infos de um livro
# Incluindo título, autor e ano de publicação. Imprima cada info.

from typing import Dict, Any
#
#livro: Dict[str, Any] = {
#    'Título': 'Finders Keepers',
#    'Autor': 'Stephen King',
#    'Ano publicacao': 2015
#}
#
#lista_de_elementos: list = livro.items()
#for elemento in lista_de_elementos:
#    print(elemento)

## Criando uma lista de livros
#livro_01: Dict[str, Any] = {
#    'Título': 'Finders Keepers',
#    'Autor': 'Stephen King',
#    'Ano publicacao': 2015
#}
#
#livro_02: Dict[str, Any] = {
#    'Título': 'The Shining',
#    'Autor': 'Stephen King',
#    'Ano publicacao': 1977
#}
#
#lista_livros = []
#
#lista_livros.append(livro_01)
#lista_livros.append(livro_02)
#
#print(lista_livros)
#
# Dicionários aninhados

lista_de_livros_usando_dict: Dict = {
     'livro_01': {'Título': 'Finders Keepers',
                 'Autor': 'Stephen King',
                 'Ano publicacao': 2015},
                 'livro_02': {'Título': 'The Shining',
                 'Autor': 'Stephen King',
                 'Ano publicacao': 1977}
}


print(lista_de_livros_usando_dict['livro_01'])