import json

with open('data/music.json') as music_json:
  music_data = json.load(music_json)

print(json.dumps(music_data, indent=1))