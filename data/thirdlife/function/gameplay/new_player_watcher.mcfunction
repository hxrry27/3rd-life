# Detect and process new players
execute as @a[tag=!initialized] run function thirdlife:gameplay/initialize_new_player

# Tag them as initialized
tag @a[tag=!initialized] add initialized
