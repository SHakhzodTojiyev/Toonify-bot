import requests

API_TOKIN = "Qovuncha"

async def api_req(photo_url):
    r = requests.post(
    "https://api.deepai.org/api/toonify",
    data={
        'image': photo_url,
    },
    headers={'api-key': API_TOKIN}
    )
    data = r.json()

    if data:
        return data["output_url"]
        
    return None
