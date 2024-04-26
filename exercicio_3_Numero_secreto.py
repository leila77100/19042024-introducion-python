#juego para encontrar el numero secreto 
import random

numero_secreto = random.randint(1,20)

print("el numero secreto es", numero_secreto)

n=int(input("devina el numero secreto"))

while n!=numero_secreto:
    
    if (n!=numero_secreto):
        n=int(input("Intenta otra vez devina el numero secreto"))
   
print("bravoooo, el numero era", numero_secreto)
        