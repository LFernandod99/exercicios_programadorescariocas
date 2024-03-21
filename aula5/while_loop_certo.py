# se digitar 1 - sacar
# se digitar 2 extrato
# se digitar 3 sair

# break => vai parar (quebrar)

# continue => ira pular o valor atual e irà exibir o seguinte.

# Crie uma estrutua de repetição(loop) 
# utilizando o laço while onde a repetição digitada pelo usuario só é quebrada caso a opção digitada pelo usuario seja 0

opcaoEscolhida = -1

while(opcaoEscolhida != 0):
    opcaoEscolhida = int(input(f'''
=================== BANCO AZUL ===================
          Inform uma das opções a baixo:
                [1] - S A C A R
                [2] - E X R A T O
                [0] - S A I R
==================================================
:'''))
    if (opcaoEscolhida == 1):
        print("@@@ S A C A N D O @@@")
    elif(opcaoEscolhida == 2):
        print("@@@ E X I B I N D O   E X T R A T O @@@")
    elif(opcaoEscolhida == 0):
        print("O B R I G A D O!   V O L T E S E M P R E")
        break
    else:
        print("O P Ç Ã O    I N V A L I D A")