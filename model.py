import requests
import math
import http.client
import json
from pprint import pprint
from firebase import firebase,FirebaseAuthentication
from nba_functions import *



firebase_db = firebase.FirebaseApplication('https://nbasort.firebaseio.com/', authentication=None)


#stats= get_player_stat_list("points", '583ec5fd-fb46-11e1-82cb-f4ce4684ea4c', "036f914a-aad0-4ff1-9771-54f9e963d1b8")
#print stats


[away_team_id, home_team_id,away_team_name, home_team_name] = get_team_ids(1209)

#print away_team_id
#print home_team_id

print "------------- "+ away_team_name + " @ " + home_team_name + "-----"


final_score = run_game(10,away_team_id, home_team_id,away_team_name, home_team_name)


















#returns player stats in dictionary {player:[stats]}

##    get_string = "/Names/Players/"+shooter
##    
##    result = firebase_db.get(get_string,None)
##    data_str = json.dumps(result)
##    player_outer = json.loads(data_str)
##    if player_outer is None:
##        shooter_name = shooter
##    else:
##        shooter_name = player_outer[player_outer.keys()[0]]
##    
##    #print "Shooter is: "+str(shooter)
##
