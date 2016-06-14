#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
"""
Dicionário dos principais tipos de Música eletrônica
Developed by Dan

Algoritmo que mostra alguns tipos de música eletrônica.
Pesquisa dos tipos em: 
http://musiartes.com.br/2015/11/os-principais-tipos-de-musica-eletronica/

"""

tiposmuselectro = {'Techno': 'estilo de música eletrônica essencialmente dançante, de ritmo acelerado e melodia monótona. Surgiu na década de 1980 e se assemelha ao estilo house. O nome “techno”, identificava todas as músicas que eram feitas exclusivamente por computador, e assim, sem fazer uso de instrumentos musicais tradicionais, imenso espectro de sons artificiais.',
'Break-beat': 'é uma vertente da música eletrônica criada pelo DJ Kool Herc na década de 1970, no Bronx, com a técnica do back-to-back, dois discos iguais e um mixer. É mais conhecido como uma música que se caracteriza pelos samplers de ritmos hip-hop, funk e electro e que logo se modificam e alteram para criar os denominados “breaks”.',
'House Music': 'é um estilo musical surgido em Chicago, nos Estados Unidos, na primeira metade da década de 1980. Possui batidas bem rápidas variando entre 118 e 135bpm, apesar de apresentar batidas mais lentas no seu surgimento. A batida 4/4 é um dos elementos mais comuns no house, que geralmente é gerado por uma caixa de ritmos ou um sampler. Diversas fontes de som são utilizadas, normalmente contínuos que se repetem eletronicamente com linhas de sequência geradas por um sintetizador.',
'Trance': '(também abreviado como D&B, DnB) é um estilo de música eletrônica que se originou a partir do jungle. Surgiu na metade dos anos 90 na Inglaterra. O gênero é caracterizado por batidas rápidas, próximas a 170 BPM. Incorporou elementos de culturas musicais como o dancehall, electro, funk, Hip-Hop, house, jazz, metal, pop, reggae, rock, techno e trance.',
'Drum and bass': 'Uma das principais vertentes da música eletrônica, que emergiu no início da década de 1990. O gênero é caracterizado pelo tempo entre 130 e 190 bpm, com partes melódicas de sintetizador e uma forma musical progressiva durante a composição (de forma crescente ou apresentando quebras). Algumas vezes vocais também são utilizados. Estilo é derivado do house e do techno, com seus sons industriais, parecerem menos melódicos.',
'Chill Out': '(chill out rooms, termo inglês que significa “quartos para relaxar”). Surgiu nos inícios e meios da década de 1990 como um termo geral para vários estilos de música de relativa melodia e baixo tempo feitas por produtores contemporâneos na música eletrônica.',
'Minimal': 'Como o próprio nome diz, é uma vertente minimalista que segue aquele ditado “less is more” (menos é mais). Este estilo também está ligado ao movimento e a arte minimalista.',
'Dubstep': 'Se originou no Sul de Londres, Inglaterra no início da década de 2000. O gênero é marcado pelo uso intenso de sub graves, sendo quase que como uma adoração aos sons de frequências baixas e também marcados pelos “bass drops” ao fim da introdução da música, em geral aos 16 ou 32 compassos, onde os elementos mais dominantes na estrutura da música são introduzidos de forma impactante.'}

#Limpa a tela ao iniciar o script
clear = lambda: os.system('clear')
clear()

#Mostra as palavras que foram definidas no dicionário.

print("=================================================")
print("===             Dict Music electro            ===")
print("===   Principais tipos de música eletrônica   ===")
print("===   Escolha um e descubra como é o estilo!  ===")
# O que será mostrado abaixo com o laço for (exceto a numeração):
#print("=== 1: Techno                5: Drum and bass ===")
#print("=== 2: Break-beat            6: Chill Out     ===")
#print("=== 3: House Music           7: Minimal       ===")
#print("=== 4: Trance                8: Dubstep       ===")
#print("=================================================")
print("===                                           ===")
for tipos in tiposmuselectro:
	print("===   %s" %tipos)
print("===                                           ===")	
print("=================================================")

selected_word = ''
while selected_word != 'sair':
    #Permite que o usuário escolha uma palavra e, em seguida, exiba o significado da mesma.
    selected_word = input("\nQual tipo de música eletônica você deseja conhecer? (ou 'sair') ")
    if selected_word in tiposmuselectro.keys():
        # Busca a palavra que o dicionário saiba.
        print("\n  %s: %s" % (selected_word, tiposmuselectro[selected_word]))
        print("")
        print("")
        print("More!\n=== Techno / Break-beat / House Music / Trance    ===")
        print("=== Drum and bass / Chill Out / Minimal / Dubstep ===")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    elif selected_word != 'sair':
        # Se a palavra não estiver em tiposmuselectro, ele dá o ninja.
        print("- Is it too late now to say sorry? SORRY YEAH ;( ")
        print(" Bieber, Justin ")
    else:
        # Sai do programa.
        print("And the hardest thing to do is say \n Bye bye")
        print(" Carey, Mariah ")
        print("TOMORROWLAAAAANDDDD!!! <3")
