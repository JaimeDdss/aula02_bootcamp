#Crie um dicionário para armazenar infos de um livro
# Incluindo título, autor e ano de publicação. Imprima cada info.

from typing import Dict, Any

livro: Dict[str, Any] = {
    'Título': 'Finders Keepers',
    'Autor': 'Stephen King',
    'Ano publicacao': 2015
}

lista_de_elementos: list = livro.items()
for elemento in lista_de_elementos:
    print(elemento)
    