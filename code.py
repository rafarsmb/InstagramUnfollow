import json

# Carga tus archivos JSON desde la carpeta extraída del ZIP
with open("followers_1.json", "r", encoding="utf-8") as f:
    followers_data = json.load(f)
with open("following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)

# Extrae los usernames
followers = {entry["string_list_data"][0]["value"] for entry in followers_data}
following = {entry["string_list_data"][0]["value"] for entry in following_data["relationships_following"]}

# Calcula los que no te siguen de vuelta
no_me_siguen = sorted(following - followers)

# Muestra la lista
for user in no_me_siguen:
    print(user)
