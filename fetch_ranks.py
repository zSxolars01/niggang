import os, json, urllib.request, urllib.parse
from datetime import datetime, timezone

API_KEY = os.environ["RIOT_API_KEY"]
HEADERS = {"X-Riot-Token": API_KEY}
REGIONAL = "https://americas.api.riotgames.com"
PLATFORM = "https://la1.api.riotgames.com"

PLAYERS = [
    {"id": "juanYF",        "game": "crybaby",       "tag": "616SS"},
    {"id": "hwidban",       "game": "Checo",          "tag": "Jgler"},
    {"id": "zSxolars",      "game": "zSxolars",       "tag": "MTLSA"},
    {"id": "DizzyL",        "game": "DizzyL",         "tag": "nlgan"},
    {"id": "PykeTyson",     "game": "Pyke Tyson",     "tag": "1389"},
    {"id": "stately",       "game": "stately",        "tag": "LAN"},
    {"id": "Risardo",       "game": "Risardo",        "tag": "LAN"},
    {"id": "T1Tocino",      "game": "T1 Ťocino", "tag": "God"},
    {"id": "DjChurches",    "game": "DjChurches",     "tag": "nigan"},
    {"id": "Cangreburgito", "game": "Cangreburgito69","tag": "6969"},
]

TIER_LABEL = {
    "IRON": "Iron", "BRONZE": "Bronze", "SILVER": "Silver",
    "GOLD": "Gold", "PLATINUM": "Platinum", "EMERALD": "Emerald",
    "DIAMOND": "Diamond", "MASTER": "Master", "GRANDMASTER": "Grandmaster",
    "CHALLENGER": "Challenger",
}
RANK_LABEL = {"I": "1", "II": "2", "III": "3", "IV": "4"}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())

def get_display(tier, rank, lp):
    t = TIER_LABEL.get(tier, tier.capitalize())
    if tier in ("MASTER", "GRANDMASTER", "CHALLENGER"):
        return f"{t} · {lp} LP"
    return f"{t} {RANK_LABEL.get(rank, rank)} · {lp} LP"

def main():
    try:
        with open("ranks.json") as f:
            data = json.load(f)
    except Exception:
        data = {"players": {}}

    for p in PLAYERS:
        pid = p["id"]
        try:
            game_enc = urllib.parse.quote(p["game"])
            tag_enc  = urllib.parse.quote(p["tag"])

            # 1. PUUID
            acc = fetch(f"{REGIONAL}/riot/account/v1/accounts/by-riot-id/{game_enc}/{tag_enc}")
            puuid = acc["puuid"]

            # 2. Summoner ID
            summ = fetch(f"{PLATFORM}/lol/summoner/v4/summoners/by-puuid/{puuid}")
            sid = summ["id"]

            # 3. Rank entries
            entries = fetch(f"{PLATFORM}/lol/league/v4/entriesBySummoner/{sid}")
            solo = next((e for e in entries if e["queueType"] == "RANKED_SOLO_5x5"), None)

            if solo:
                wins   = solo["wins"]
                losses = solo["losses"]
                total  = wins + losses
                wr     = f"{round(wins/total*100, 1)}%" if total > 0 else "-"
                data["players"][pid] = {
                    "display": get_display(solo["tier"], solo["rank"], solo["leaguePoints"]),
                    "wr": wr,
                }
            else:
                data["players"][pid] = {"display": "Unranked", "wr": "-"}

            print(f"OK  {pid}: {data['players'][pid]['display']}")

        except Exception as e:
            print(f"ERR {pid}: {e}")

    data["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    with open("ranks.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
