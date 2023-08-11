import spacy 

nlp = spacy.load("/Users/conrom007/Documents/Rasa Projects/Extractor /trained_models/model-last")


#input = nlp(
#    "1 fresh baguette, sliced into strips, 1/4 cup unsalted butter, 1 orange (2 oranges for 2 salads), 150g minced beef meat in the frying pan where you fried the onion and garlic, 1 large ribeye steak, 100g yogurt, 1/2 cup blueberries, 1 tablespoon honey",
#)

input = [
    "1 fresh baguette, sliced into strips",
    "1/4 cup unsalted butter",
    "1 orange (2 oranges for 2 salads)",
    "150g minced beef meat in the frying pan where you fried the onion and garlic",
    "1 large ribeye steak",
    "100g yogurt, 1/2 cup blueberries, 1 tablespoon honey",
    "4 cups milk, 150g chocolate, 50g vanilla extract, 2 avocadoes, 2tsp sugar, 1 pinch salt",
    "1tbsp sugar, 1tbsp gogujang, 1 box rice cakes, 15ml sesame oil"
    "2 cup tomato, 1 tablespoon cinnammon"
    "2 cups lentils"
    "120g oats, 1 banana sliced, 35ml golden syrup, 1tbsp cinnamon, 1g salt, 25g kiwi, 5ml vanilla extract",
    "20 ml mirin, 1g salt, 20g sugar, 15g brown sugar, 1 spring onion, sliced, 200g pork meat",
]
for line in input:
    doc = nlp(line)
    for entity in doc.ents:
        print(entity.label_, ' | ', entity.text)

