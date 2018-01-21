from lxml import html
import requests
import math
import http.client
import json
from pprint import pprint
from firebase import firebase,FirebaseAuthentication



## Pull game summary from nba sportsradar --------------
conn = http.client.HTTPSConnection("api.sportradar.us")
#conn.request("GET", "/nba-t3/games/0da78f13-73ac-4465-8e31-ecc3029a5dc6/summary.json?api_key=hgyfkttkdsepmvvap9rddce9")
#res = conn.getresponse()
#data = json.load(res)
#pprint(data)


##secret = 'Heatlifer.1'
##dsn = 'https://nbasort.firebaseio.com'
##email = 'mrod642@gmail.com'
##new_user = "Michael"

firebase_db = firebase.FirebaseApplication('https://nbasort.firebaseio.com/', authentication=None)

result = firebase_db.get('/Schedule/-KnFSyixTJlx59nX6C1C/games',None)
#result = firebase_db.post('/Schedule',data)
data_str = json.dumps(result)
game_list = json.loads(data_str)

for game in game_list[0:400]:

    game_id = game["id"]
    get_string ="/nba-t3/games/"+game_id+"/summary.json?api_key=hgyfkttkdsepmvvap9rddce9"


    conn.request("GET", get_string)
    res = conn.getresponse()
    data = json.load(res)
    #pprint(data)

    post_string = "/Games/Game"+str(game_list.index(game))
    print post_string
    result = firebase_db.post(post_string,data)


    


#for game in game_list:
#    game_id = 
#    print game["away"]["name"]

#result = firebase_db.get('/Game1',None)
#data_str = json.dumps(result)

#data = json.loads(data_str)

#pprint(data)
#print result






