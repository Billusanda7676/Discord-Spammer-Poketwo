from webserver import keep_alive
import requests

channelID =  1316441193940385795
headers = {
    "authorization":
    "MTI5NDcwMzk4ODg4MDQ0MTM3Ng.GppMHx.A7NoT-itBUuqvlkI1KBWnfyJI-C_KGzEXjIJvg"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
