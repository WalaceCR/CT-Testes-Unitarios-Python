from src.leilao.dominio import Avaliador, Lance, Usuario, Leilao

#instanciando o objeto com o New como fazemos com java
walace = Usuario("Walace")
luana = Usuario("Luana")

lance_do_Walace = Lance(walace, 100.00)
lance_da_Luana = Lance(luana,150.00)

novoleilao = Leilao("Geladeira")

#criando novos objetos da classe
novoleilao.lances.append(lance_do_Walace)
novoleilao.lances.append(lance_da_Luana)


#percorrendo os lances da classe
for lance in novoleilao.lances:
    #exibindo os lances
    print(f' O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(novoleilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}.')





