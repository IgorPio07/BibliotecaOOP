from biblioteca.livro import LivroClass

livro_0 = LivroClass('Revista Sudoku')
livro_1 = LivroClass('Biblia')
livro_2 = LivroClass('Clean Code')
livro_3 = LivroClass('Heterônimos')
livro_4 = LivroClass('Algoritmos')
livro_5 = LivroClass('Fernando Pessoa')
livro_6 = LivroClass('Contos')
livro_7 = LivroClass('Machado de Assis')
livro_8 = LivroClass('Drácula')
livro_9 = LivroClass('Harry Potter')

print('Seja bem vindo à biblioteca!\nEssas são as opções de livros:'
      '''
          [0] - Revista Sudoku
          [1] - Bíblia
          [2] - Clean Code
          [3] - Heterônimos
          [4] - Fernando Pessoa
          [5] - Contos
          [6] - Machado de Assis
          [7] - Drácula
          [8] - Harry Potter     
      ''')

usuario_nome = input('Informe seu nome para começarmos: ')
selecao = int(input('Selecione um dos livros que deseja emprestar'))

lista_livros = [livro_0, livro_1, livro_2, livro_3, livro_4, livro_5, livro_6, livro_7, livro_8, livro_9]

opcao_selecionada = int(selecao)

for opcao in lista_livros:
    while opcao_selecionada >= 10 or opcao_selecionada < 0:
        print('Desculpe, não temos esta opção, por favor selecione outra')
        opcao_selecionada = int(input('Selecione um dos livros que deseja emprestar'))
    if 9 >= opcao_selecionada >= 0:
        print(f'O usuário {usuario_nome} emprestou o livro {lista_livros[opcao_selecionada].nome}')
        print('Volte Sempre!')
        break
