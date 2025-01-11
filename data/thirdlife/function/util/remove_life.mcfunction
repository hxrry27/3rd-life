# Remove a life by increasing the death count
execute as @a[scores={thirdlife.removelife=1..}] run scoreboard players add @s thirdlife.death 1

# Cap deaths at 3 (effectively stopping negative lives)
execute as @a[scores={thirdlife.death=4..}] run scoreboard players set @s thirdlife.death 3

# Notify the player
execute as @a[scores={thirdlife.removelife=1..}] run tellraw @s ["",{"text":"A life has been removed!","color":"red"}]

# Reset the trigger score
scoreboard players reset @a thirdlife.removelife
