# Leaves all players from teams to prevent duplication or incorrect assignments
team leave @a

# Green Team: 0 deaths
execute as @a[scores={thirdlife.death=0}] run team join thirdlife.green

# Yellow Team: 1 deaths
execute as @a[scores={thirdlife.death=1}] run team join thirdlife.yellow

# Red Team: 2 deaths
execute as @a[scores={thirdlife.death=2}] run team join thirdlife.red

# Spectating Team: 3 deaths
execute as @a[scores={thirdlife.death=3}] run team join thirdlife.spectators

# Force gamemodes of teams
execute as @a[team=thirdlife.spectators, gamemode=!spectator, tag=!op] run gamemode spectator @s
execute as @a[team=!thirdlife.spectators, gamemode=!survival, tag=!op] run gamemode survival @s
