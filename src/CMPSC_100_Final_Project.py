import random

from Animals import Cat

REGISTRY = {}

def register(cat):
    if cat.name not in REGISTRY.keys():
        REGISTRY[cat.name] = cat
        print(f"There's a new cat on the scene! {cat}")
        
def talk():
    cats = random.sample(REGISTRY.keys(),2)
    # I have two cat objects which have the same attributes
    if REGISTRY[cats[0]].pattern == REGISTRY[cats[1]].pattern:
        print(f"{REGISTRY[cats[0]].name} says 'Meow!' to {REGISTRY[cats[1]].name}")

while len(REGISTRY) < 100:
    new_cat = Cat()
    register(new_cat)
    if len(REGISTRY) > 1:
        talk()