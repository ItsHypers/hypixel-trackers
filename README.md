# Hypixel Stat Trackers


- This is a simple python script to track Collection and Skill XP.
- You can track yourself, or other users (if their API is public ofcourse)



- This requires you to have python and pip installed
- https://www.python.org/downloads/
- https://pip.pypa.io/en/stable/installation/
- (easy to do, looks scary but it isnt)

## How To Install:

- Download script file

- Create a virtual environment (recommended, not needed https://docs.python.org/3/library/venv.html)

- in a command promt, do
pip install -r requirements.txt

- then run 
tracker.py

## How to Use:
- After installation works, open up the config.json file

- put your Hypixel API key in the key section (type /api new in game)

- put your IGN and profile name into the player section

- change the collection to your selected collection

- change the skill to your selected skill

- Change the cooldown to what you want (in seconds) (anything above 100 is recommended)

If you dont want to track a collection, leave it blank.
If you dont want to track a skill, leave it blank.


## List of Collections:

(some collections are named differently in the API than in game, so here is a list of all collections)

----------------
FARMING

- CACTUS
- CARROT_ITEM - CARROT
- INK_SACK:3 - COCOA BEANS
- FEATHER
- LEATHER
- MELON
- MUSHROOM_COLLECTION - MUSHROOM
- MUTTON
- NETHER_STALK - NETHERWART
- POTATO_ITEM - POTATO
- PUMPKIN
- RAW_CHICKEN - CHICKEN
- PORK - PORKCHOP
- RABBIT
- SEEDS
- SUGAR_CANE
- WHEAT 
----------------
MINING

- COAL
- COBBLESTONE
- DIAMOND
- EMERALD
- ENDER_STONE - ENDSTONE 
- GEMSTONE_COLLECTION - GEMSTONES
- GLOWSTONE_DUST - GLOWSTONE 
- GOLD_INGOT - GOLD
- GRAVEL
- HARD_STONE 
- ICE
- IRON_INGOT
- INK_SACK-4 - LAPIS
- MITHRIL_ORE
- MYCEL - MYCELIUM 
- QUARTZ
- NETHERRACK
- OBSIDIAN
- SAND-1
- REDSTONE
- SAND
- SULPHUR_ORE
----------------
COMBAT

- BLAZE_ROD
- BONE
- CHILLI_PEPPER
- ENDER_PEARL
- GHAST_TEAR
- SULPHUR_ORE
- MAGMA_CREAM
- ROTTEN_FLESH
- SLIME_BALL
- SPIDER_EYE
- STRING
----------------
FORAGING 

- LOG - OAK
- LOG:2 - BIRCH
- LOG_2:1 - DARK OAK
- LOG:3 - JUNGLE
- LOG_2 - ACACIA
- LOG:1 - SPRUCE
----------------
FISHING

- CLAY_BALL
- RAW_FISH-2 - CLOWNFISH
- INK_SACK - INK_SACK
- WATER_LILY - LILY PADS
- MAGMA_FISH
- PRISMARINE_CRYSTALS
- PRISMARINE_SHARD
- RAW_FISH-3 - PUFFERFISH
- RAW_FISH
- RAW_FISH-1 - SALMON
- SPONGE

## SKILL EXAMPLES

- runecrafting
- mining
- alchemy
- taming 
- farming 
- combat 
- social 
