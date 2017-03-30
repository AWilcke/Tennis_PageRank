import numpy as np
import csv

def get_players(f):
    
    ret = {}

    with open(f) as data:
        reader = csv.DictReader(data)
        count = 0
        for row in reader:
            w = row['winner_name']
            l = row['loser_name']

            if w not in ret.keys():
                ret[w] = count
                count += 1
            if l not in ret.keys():
                ret[l] = count
                count += 1
    return ret

def get_matrix(f):

    players = get_players(f)
    ret = np.zeros((len(players),len(players)))
    with open(f) as data:
        reader = csv.DictReader(data)
        for row in reader:
            w = row['winner_name']
            l = row['loser_name']

            ret[players[w]][players[l]] += 1
    return ret
