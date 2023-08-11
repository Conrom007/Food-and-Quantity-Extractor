#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process
import pandas as pd
from difflib import get_close_matches

def lev_dist_calc(word):
    n = 1
    cutoff = 0.7
    food_names = pd.read_csv('nutrition.csv')[['name']].values.tolist()
    match = get_close_matches(word, food_names, n, cutoff)
    
    return print(match)
    
#lev_dist_calc('Chicken')


food_names = pd.read_csv('nutrition.csv')
print(food_names)
