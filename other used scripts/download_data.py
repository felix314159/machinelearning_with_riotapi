from riotwatcher import LolWatcher, ApiError

import pandas as pd


api_key = 'PASTE-YOUR-KEY-HERE'
watcher = LolWatcher(api_key)


def check_string(string):
    if all(x.isalnum() or x.isspace() for x in string) and string.isascii():
        return True

    else:
        return False


def get_names(rank, mode):

    result = []
    regions = ["na1", "oc1", "tr1", "ru", "br1", "eun1", "euw1", "jp1", "kr", "la1", "la2"]
    for j in regions:


        dia1 = watcher.league.entries(j, mode, rank, "I")
        for i in dia1:
            if check_string(i["summonerName"]):
                result.append(i["summonerName"])


        dia2 = watcher.league.entries(j, mode, rank, "II")
        for i in dia1:
            if check_string(i["summonerName"]):
                result.append(i["summonerName"])

        dia3 = watcher.league.entries(j, mode, rank, "III")
        for i in dia3:
            if check_string(i["summonerName"]):
                result.append(i["summonerName"])

        dia4 = watcher.league.entries(j, mode, rank, "IV")
        for i in dia4:
            if check_string(i["summonerName"]):
                result.append(i["summonerName"])
                


    result.sort()
    return result

# modes = ["RANKED_FLEX_SR", "RANKED_SOLO_5x5"]
# options = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
print("Program is now running..")
final = get_names("GOLD", "RANKED_SOLO_5x5")
with open('gold_names_clean.txt', 'w') as f:
    for i in final:
        f.write("%s\n" % i)
