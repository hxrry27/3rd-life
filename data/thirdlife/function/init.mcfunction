#game reset trigger
scoreboard objectives add thirdlife.reset trigger

#game live management system counters
scoreboard objectives add thirdlife.death deathCount "Deaths"
scoreboard objectives add thirdlife.kill playerKillCount "Players Killed"

#manual adjustment triggers (just in case)
scoreboard objectives add thirdlife.addlife trigger
scoreboard objectives add thirdlife.removelife trigger

#team creation assignment and colouring
team add thirdlife.red
team modify thirdlife.red color red
team add thirdlife.yellow
team modify thirdlife.yellow color yellow
team add thirdlife.green
team modify thirdlife.green color green
team add thirdlife.spectators
team modify thirdlife.spectators color gray

gamerule commandBlockOutput false
gamerule sendCommandFeedback false

#tags for handling offline players and admin perms
tag @a add initialized
tag hxrry27 add op

#allowing only hxrry27 to use the triggers
scoreboard players enable hxrry27 thirdlife.reset
scoreboard players enable hxrry27 thirdlife.addlife
scoreboard players enable hxrry27 thirdlife.removelife
