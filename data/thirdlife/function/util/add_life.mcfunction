# Add a life by reducing the death count
execute as @a[scores={thirdlife.addlife=1..}] run scoreboard players remove @s thirdlife.death 1

# Cap deaths at 0
execute as @a[scores={thirdlife.death=-1..}] run scoreboard players set @s thirdlife.death 0

# Notify the player
execute as @a[scores={thirdlife.addlife=1..}] run tellraw @s ["",{"text":"An extra life has been added!","color":"green"}]

# Reset the trigger score
scoreboard players reset @a thirdlife.addlife
