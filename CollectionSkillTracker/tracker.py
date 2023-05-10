import time
import requests
import json
from dhooks import Webhook, Embed


j = open('config.json')
config = json.load(j)
j.close()
hook = Webhook(config["trackerConfig"]["discord_webhook_url"])
if(config["trackerConfig"]["key"] == "key"):
    print("please enter your hypixel key into the config.json file! (Read the README)")
    quit()

if(config["trackerConfig"]["player"]["ign"] == "ign"):
    print("please enter your minecraft ign into the config.json file! (Read the README)")
    quit()

if(config["trackerConfig"]["player"]["profile"] == "profile"):
    print("please enter your hypixel profile name into the config.json file! (Read the README)")
    quit()
if(config["trackerConfig"]["skill"] == "" and config["trackerConfig"]["collection"] == ""):
    print("both skill and collection are blank in the config file! You must put a collection or skill into atleast one of them (Read the README)")
    quit()

def fetchSBProfile(playerName, profileName):
    uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/"+playerName).json()
    playerUUID = uuid["id"]
    data = requests.get("https://api.hypixel.net/player?uuid="+ playerUUID +"&key="+ config["trackerConfig"]["key"]).json()
    data = data["player"]["stats"]["SkyBlock"]["profiles"]
    
    data=data.values()
    data=list(data)
 
    for i in range(len(data)):
        cutename = config["trackerConfig"]["player"]["profile"]
        if profileName==data[i]["cute_name"]:
            a = data[i]["profile_id"]
    return playerUUID, a

playerInfo = fetchSBProfile(config["trackerConfig"]["player"]["ign"], config["trackerConfig"]["player"]["profile"])
playerUUID = playerInfo[0]
profileUUID = playerInfo[1]
collection = config["trackerConfig"]["collection"].upper()

def playerAPI():
    data = requests.get("https://api.hypixel.net/skyblock/profile?key="+ config["trackerConfig"]["key"] +"&uuid=" + playerUUID + "&profile=" + profileUUID).json()
    return data


def track():
    #Player 0
    a=playerAPI()
    if(config["trackerConfig"]["collection"] != ""):
        before0=a["profile"]["members"][playerUUID]["collection"][collection]
    if(config["trackerConfig"]["skill"] != ""):
        mxpBefore0=a["profile"]["members"][playerUUID]["experience_skill_" + config["trackerConfig"]["skill"]]
    while(True):
        if(config["trackerConfig"]["collection"] != ""):
            recentCollection=a["profile"]["members"][playerUUID]["collection"][collection]
        if(config["trackerConfig"]["skill"] != ""):
            lastmxpAmount0=a["profile"]["members"][playerUUID]["experience_skill_" + config["trackerConfig"]["skill"]]
        a=playerAPI()
        if(config["trackerConfig"]["collection"] != ""):
            var0=a["profile"]["members"][playerUUID]["collection"][collection]

            embed = Embed(
            description=config["trackerConfig"]["collection"].upper() + " Collection Tracker",
            color=0x5CDBF0,
            timestamp='now'  # sets the timestamp to current time
            )
            embed.set_author(name=config["trackerConfig"]["player"]["ign"])
            embed.add_field(name=config["trackerConfig"]["collection"].upper() + " Collection", value=str(f"{var0:,}") + ' :open_mouth:')
            embed.add_field(name='Since start of session', value=str(f"{var0-before0:,}"))
            embed.add_field(name='Since Last request', value= str(f"{var0-recentCollection:,}"))
            hourlyestimate = 3600 // config["trackerConfig"]["cooldown"] * (var0-recentCollection)
            embed.add_field(name='Estimated Per Hour', value=str(f"{hourlyestimate:,}"))

            hook.send(embed=embed)
        if(config["trackerConfig"]["skill"] != ""):
            mxp0=a["profile"]["members"][playerUUID]["experience_skill_" + config["trackerConfig"]["skill"]]

            embed = Embed(
            description=config["trackerConfig"]["skill"] + " Skill Tracker",
            color=0x5CDBF0,
            timestamp='now'  # sets the timestamp to current time
            )
            embed.set_author(name=config["trackerConfig"]["player"]["ign"])
            embed.add_field(name=config["trackerConfig"]["skill"] + " Skill Total", value=str(f"{round(mxp0, 2):,}") + ' :open_mouth:')
            embed.add_field(name='Since start of session', value=str(f"{round(mxp0-mxpBefore0, 2):,}"))
            embed.add_field(name='Since Last request', value=str(f"{round(mxp0-lastmxpAmount0, 2):,}"))
            hourlyestimate = 3600 // config["trackerConfig"]["cooldown"] * (round(mxp0-lastmxpAmount0, 2))
            embed.add_field(name='Estimated Per Hour', value=str(f"{hourlyestimate:,}"))

            hook.send(embed=embed)
 
        #Sleep for a reasonable time untill new API data is available (3-4 minutes)
        time.sleep(config["trackerConfig"]["cooldown"])
 
track()

#a=playerAPI()
#print(a["profile"]["members"][playerUUID]["stats"]["kills_old_wolf"])