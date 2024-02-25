# code to categorize clothing items into different categories
import os
import random
from PIL import Image
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg


class clothing_items:
    def __init__(self, name):
        self.name = name
        self.componet = 0
        self.weather = 0
        self.occasion = 0

    #def set_name(self, name):
        #self.name = name
    
    #def set_componet(self): 
        if self.name == "T-shirt" or self.name == "T-Pullover" or self.name == "Shirt":
            self.component = "Top"
        elif self.name == "Trouser":
            self.component = "Bottom"
        elif self.name == "Coat":
            self.component = "Outer"
        elif self.name == "Dress":
            self.component = "Full-body"
        elif self.name == "Sandal" or self.name == "Sneaker" or self.name == "Boot":
            self.component = "Shoes"
        elif self.name == "Bag":
            self.component = "Accessories"
    
    #def set_weather(self):
        if self.name == "T-shirt" or self.name == "T-Pullover" or self.name == "Shirt":
            self.weather = "Summer"
        elif self.name == "Trouser":
            self.weather = "All"
        elif self.name == "Coat":
            self.weather = "Winter"
        elif self.name == "Dress":
            self.weather = "Summer"
        elif self.name == "Sandal" or self.name == "Sneaker" or self.name == "Boot":
            self.weather = "All"
        elif self.name == "Bag":
            self.weather = "All"

    #def set_occasion(self):
        if self.name == "T-shirt" or self.name == "T-Pullover" or self.name == "Shirt":
            self.occasion = "Casual"
        elif self.name == "Trouser":
            self.occasion = "Casual"
        elif self.name == "Coat":
            self.occasion = "Formal"
        elif self.name == "Dress":
            self.occasion = "Formal"
        elif self.name == "Sandal" or self.name == "Sneaker" or self.name == "Boot":
            self.occasion = "Casual"
        elif self.name == "Bag":
            self.occasion = "Casual"

    def display(self):
        print("Name: ", self.name)
        print("Component: ", self.component)
        print("Weather: ", self.weather)
        print("Occasion: ", self.occasion)
    
def weather_input(weather):
    weather_clothes = []
    if weather == "Warm":
        weather_clothes = ["T-shirt", "Trouser", "f_Trouser", "Dress", "Sandal", "Shirt", "Sneaker", "Bag", "Boot"]
    elif weather == "Cold":
        weather_clothes = ["Trouser",  "Pullover", "f_Trouser", "Coat", "Shirt", "Bag",  "Boot"]
    elif weather == "Medium":
        weather_clothes = ["Trouser", "Pullover", "f_Trouser", "Coat", "Shirt", "Sneaker",  "Bag"]
    return weather_clothes

def occasion_input(occasion, weather_clothes): #narrows down the list of clothes based on the occasion
    return_list = []
    for item in (weather_clothes):
        return_list.append(item)

    for item in (weather_clothes):
        if occasion == "Casual":
            if item == "Shirt" or item == "Dress" or item == "f_Trouser":
                return_list.remove(item)
            else:
                continue
        elif occasion == "Formal":
            if (item == "Pullover" or item == "Sandal" or item == "T-shirt" or item == "Dress" or item == "Sneaker" or item == "Trouser" ):
                return_list.remove(item)
            else:
                continue
        elif occasion == "Event":
            if item == "T-shirt" or item == "Pullover" or item == "Trouser":
                return_list.remove(item)
            else:
                continue
    
    return return_list

    
#my_closet = [clothing_items("T-shirt") , clothing_items("Shirt"), clothing_items("Trouser"), clothing_items("Coat"), clothing_items("Dress"), clothing_items("Sandal"), clothing_items("Sneaker"), clothing_items("Ankle boot"), clothing_items("Bag")]
# mycloset has folders of each clothing item
# pull a random one from each folder

#my_closet[0].display()

def get_outfit(weather, occasion):
    outfit = weather_input(weather)
    print(outfit)
    outfit = occasion_input(occasion, outfit)
    print(outfit)

    shoe_list = [thing for thing in outfit if thing in ["Sandal", "Sneaker", "Boot"]]
    outfit = [thing for thing in outfit if thing not in ["Sandal", "Sneaker", "Boot"]]
    outfit.append(random.choice(shoe_list))

    # enter the folder of the clothing item
    # pull a random one from the folder
    # display the clothing item

    folder_name = "static\images\myCloset"
    chosen_outfit = []
    for item in outfit:
        folder_path = os.path.join(folder_name, item)
        # randomly select a file from the folder
        files = os.listdir(folder_path)
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        random_file = random.choice(files)
        print("Randomly selected file:", random_file)

        # show image
        image_path = os.path.join(folder_path, random_file)
        chosen_outfit.append(image_path)
        # image = Image.open(image_path)
        # image.show()
        #image = mpimg.imread(image_path)
        #plt.imshow(image)
        #plt.show()

    print(chosen_outfit)
    return chosen_outfit

'''
 # Open the selected PNG image
    image_path = os.path.join(folder_path, random_file)
    image = Image.open(image_path)

    # Display the image (optional)
    image.show()
    
    '''
