import spacy

import en_core_web_lg
nlp = en_core_web_lg.load()




foods = nlp("honey orange milk flour meat bread steak yogurt sandwich spaghetti meatballs cottage-cheese blueberries pastrami butter onion garlic")

input = [
    "1 fresh baguette, sliced into strips",
    "1/4 cup unsalted butter",
    "1 orange (2 oranges for 2 salads)",
    "150g minced beef meat in the frying pan where you fried the onion and garlic",
    "1 large ribeye steak",
    "100g yogurt, 1/2 cup blueberries, 1 tablespoon honey",
]

for line in input:
    line_nlp = nlp(line)
    extracted = []
    for token in line_nlp:
        if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
            extracted.append({
                'word': token.lemma_,
                'sim': token.similarity(foods)
            })
    for i in range(0,2):
        print(sorted(extracted, key=lambda k: k['sim'], reverse=True)[i]['word'])

