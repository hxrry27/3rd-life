# Set death count to 0 for players not yet tracked
execute as @a unless score @s thirdlife.death matches 1.. run scoreboard players set @s thirdlife.death 0
