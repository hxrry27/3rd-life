# Reset lives and deaths for all players
scoreboard players set @a thirdlife.death 0

# Reassign players to teams
team leave @a
execute as @a run team join thirdlife.green

# Notify players
tellraw @a ["",{"text":"Game has been reset! All lives and deaths cleared.","color":"red"}]

scoreboard players reset hxrry27 thirdlife.reset

scoreboard players enable hxrry27 thirdlife.reset

