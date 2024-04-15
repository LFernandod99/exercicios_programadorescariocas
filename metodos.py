#Estrutura de um dicionario
estudante = {
    'Nome' : 'Luiz Fernando',
    'Idade': 25,
    'Matriculado': True,
    'Matricula': 'ab023',
    'Endereco': [
        {
            'Rua': 'Santa Luzia',
            'numero': 790,
            'cidade': 'Rio de Janeiro',
        }
    ]
}
# #Acessar o elemento pela chave
# print(estudante['Idade'])
# # Adicionar e atualizar valores

# estudante['Idade'] = 22
# print(estudante['Idade'])

# estudante['Cpf'] = 17758898857
# print(estudante)

# #Removendo elementos

# del estudante ['Cpf']
# print(estudante)

#Len
# print(len(estudante))

# print(estudante.keys())

# #Retornar todos os itens
# print(estudante.values())

                    # Metodos
#UPDATE
# estudante.update({'Nome': 'José'}) 
# print(estudante['Nome'])

#POP

# estudante.pop('Idade')
# print(estudante)

# estudante.clear()
# print(estudante)