import requests
import json

class ApexLegendsAPI:
    def __init__(self, username, platform, uid, api_key):
        self.username = username
        self.platform = platform
        self.uid = uid
        self.headers = {
            f"Authorization": api_key
        }

    def get(self, url):
        return requests.get(url, headers=self.headers, timeout=5)

    def get_player_stats_by_username(self):
        url = f"https://api.mozambiquehe.re/bridge?player={self.username}&platform={self.platform}"
        return self.get(url)
    
    def get_player_stats_by_uid(self):
        url = f"https://api.mozambiquehe.re/bridge?uid={self.uid}&platform={self.platform}"
        return self.get(url)
    
    def get_player_history_by_uid(self, mode=None):
        # You must be whitelisted to use this API. To do so, open a ticket on the Discord server by https://discord.gg/qd9cZQm. This API is currently unavailable to new users.
        """
            Parameter	Required	Description
            --------------------------------
            uid         true	    The player's UID
            mode        false	    Only return matches made in a given game mode. Values can be BATTLE_ROYALE, ARENAS or UNKNOWN.
            start       false	    Only return games made after a given epoch timestamp. Value must be an int.
            end         false	    Only return games made before a given epoch timestamp. Value must be an int.
            limit       false	    Only return a maximum of X matches. Value must be an int.
        """
        url = f"https://api.mozambiquehe.re/games?uid={self.uid}&platform={self.platform}"
        if mode:
            url += f"&mode={mode}"
        return self.get(url)

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    apexlegendsapi = os.getenv("APEXLEGENDSAPI", None)
    if not apexlegendsapi:
        raise Exception("You must provide an API key for the Apex Legends API.")
    username = os.getenv("APEX_USERNAME", "hiswattson")
    id = os.getenv("APEX_UID", "1009067960369")
    platform = os.getenv("APEX_PLATFORM", "PC")
    hisWattson = ApexLegendsAPI(username, platform, id, apexlegendsapi)
    history = hisWattson.get_player_history_by_uid()
    print(json.dumps(history.json(), indent=4))
    stats = hisWattson.get_player_stats_by_uid()
    print(json.dumps(stats.json(), indent=4))