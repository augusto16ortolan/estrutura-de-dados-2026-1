from Pilha import Pilha

pilha = Pilha()         # []
pilha.push("Vermelho")  # [Vermelho]
pilha.push("Amarelo")  # [Vermelho, Amarelo]
pilha.pop()       # [Vermelho]
pilha.push("Amarelo") # [Vermelho, Amarelo]
pilha.peek() # [Vermelho, Amarelo]
pilha.push("Rosa") # [Vermelho, Amarelo, Rosa]
pilha.push("Rosa") # [Vermelho, Amarelo, Rosa, Rosa]
pilha.peek() # [Vermelho, Amarelo, Rosa, Rosa]
pilha.pop() # [Vermelho, Amarelo, Rosa]
pilha.pop() # [Vermelho, Amarelo]
print(pilha.peek()) # Amarelo
