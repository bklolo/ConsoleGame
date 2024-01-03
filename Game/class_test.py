from classes import *

player = Character(100, 100)
currentHealth = player.get_health()
currentStamina = player.get_stamina()
print("Player stats:")
print(currentHealth, currentStamina)

stdEnemy = Enemy(100, 100, 30)
stdEnemy_Health = stdEnemy.get_health()
stdEnemy_Stamina = stdEnemy.get_stamina()
stdEnemy_Aggro = stdEnemy.get_aggro()
print("Std Enemy stats:")
print("Health: " , stdEnemy_Health, ' Stamina: ',stdEnemy_Stamina, ' Aggro: ',stdEnemy_Aggro)
stdEnemy_Aggro = stdEnemy.reduce_agrro()
print("Aggro reduced!")
print('Health: ' , stdEnemy_Health , ' Stamina: ' , stdEnemy_Stamina , ' Aggro: ' , stdEnemy_Aggro)

