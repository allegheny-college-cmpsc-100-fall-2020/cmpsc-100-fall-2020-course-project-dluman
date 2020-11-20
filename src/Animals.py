import random

class Cat:
    
    def __init__(self):
        self.name = self.get_name()
        self.color = self.get_color()
        self.pattern = self.get_pattern()
        
    def __str__(self):
        return f"{self.name} is a(n) {self.color} {self.pattern} cat."
        
    def get_name(self):
        # Open the names file
        name_list = open("cat_names.txt","r")
        # Get contents as a list
        names = name_list.readlines()
        # Returning a random entry from that list
        return random.choice(names).strip()
    
    def get_color(self):
        colors = [
            "orange",
            "brown",
            "black",
            "white",
            "gray",
            "calico",
            "black and white",
            "orange and white",
            "gray and white"
        ]
        return random.choice(colors)
    
    def get_pattern(self):
        tabbies = [
            "torbie",
            "tabby",
            "tortoise shell",
            "non-tabby"
        ]
        return random.choice(tabbies)