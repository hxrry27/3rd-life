# Check if a player triggered reset
execute as @a[scores={thirdlife.reset=1..}] run function thirdlife:util/reset_game
