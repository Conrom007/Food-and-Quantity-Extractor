from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
from levenshtein_distance_calculator import lev_dist_calc


food_database = pd.read_csv('nutrition.csv').set_index('name')





def breakfast_calories(search):
    result = str(lev_dist_calc(search))
    food_database = pd.read_csv('nutrition.csv').set_index('name')
    food_database = food_database[result:result].head()
    print(food_database)
    breakfast_calories = int(food_database['calories'])
    print(breakfast_calories)
    
    return breakfast_calories 

breakfast_calories('Chicken')

def breakfast_protein(search):
    food_database = pd.read_csv('nutrition.csv').set_index('name')
    food_database = food_database[lev_dist_calc(search):lev_dist_calc(search)].head()
    print(food_database)
    breakfast_protein = str(food_database['protein']).replace(search, "").replace("g","").replace(" ","")
    print(breakfast_protein)
    
    return breakfast_protein 

breakfast_protein('Chicken, raw, meat only, boneless, skinless, breast, broiler or fryers')