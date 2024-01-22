import random


from lista_de_nomes import lista_de_nomes
palavra_escolhida = random.choice(lista_de_nomes)
comprimento_palavra_escolhida = len(palavra_escolhida)

final_do_jogo = False
vidas = 6

from artes import logo
print(logo)


display = []
for _ in range(comprimento_palavra_escolhida):
    display += "_"

while not final_do_jogo:
    letra_escolhida = input("Escolha uma letra: ").lower()
  
    
  
    if letra_escolhida in display:
      print(f"Você já escolheu a letra {letra_escolhida}! ")

  
    for posicao in range(comprimento_palavra_escolhida):
        letra = palavra_escolhida[posicao]
      
        
        if letra == letra_escolhida:
            display[posicao] = letra
        
    

    if letra_escolhida not in palavra_escolhida:
      print(f"A letra {letra_escolhida} não está na palavra. Você perdeu uma vida... ")
      
      vidas -= 1
      if vidas == 0:
          final_do_jogo = True
          print("Você perdeu.")

   
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        final_do_jogo = True
        print("Você ganhou!")

    
    from artes import etapas
    print(etapas[vidas])