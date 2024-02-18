# code to categorize clothing items into different categories
import os
import random
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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
        weather_clothes = ["T-shirt", "Trouser", "f_Trouser", "Dress", "Sandal", "Shirt", "Sneaker", "Bag"]
    elif weather == "Cold":
        weather_clothes = ["Trouser",  "Pullover", "f_Trouser", "Coat", "Shirt", "Bag",  "Boot"]
    elif weather == "Medium":
        weather_clothes = ["Trouser", "Pullover", "f_Trouser", "Coat", "Shirt", "Sneaker",  "Bag"]
    return weather_clothes

def occasion_input(occasion, weather_clothes): #narrows down the list of clothes based on the occasion
    for item in (weather_clothes):
        if occasion == "Casual":
            if item == "Shirt" or item == "Dress" or item == "f_Trouser":
                weather_clothes.remove(item)
        elif occasion == "Formal":
            if item == "Pullover" or item == "T-shirt" or item == "Sandal" or item == "Dress" or item == "Sneaker" or item == "Trouser" :
                weather_clothes.remove(item)
        elif occasion == "Event":
            if item == "T-shirt" or item == "Pullover" or item == "Trouser":
                weather_clothes.remove(item)
    
    return weather_clothes



    
#my_closet = [clothing_items("T-shirt") , clothing_items("Shirt"), clothing_items("Trouser"), clothing_items("Coat"), clothing_items("Dress"), clothing_items("Sandal"), clothing_items("Sneaker"), clothing_items("Ankle boot"), clothing_items("Bag")]
# mycloset has folders of each clothing item
# pull a random one from each folder

#my_closet[0].display()

outfit = weather_input("Warm")
print(outfit)
occasion_input("Formal", outfit)
print(outfit)

# enter the folder of the clothing item
# pull a random one from the folder
# display the clothing item

folder_name = "myCloset"
chosen_outfit = []
for item in outfit:
    folder_path = os.path.join(folder_name, item)
    # randomly select a file from the folder
    files = os.listdir(folder_path)
    files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
    random_file = random.choice(files)
    print("Randomly selected file:", random_file)
    chosen_outfit.append(random_file)

    # show image
    image_path = os.path.join(folder_path, random_file)
    print(image_path)
    image = Image.open(image_path)
    image.show()
    #image = mpimg.imread(image_path)
    #plt.imshow(image)
    #plt.show()

print(chosen_outfit)

'''
 # Open the selected PNG image
    image_path = os.path.join(folder_path, random_file)
    image = Image.open(image_path)

    # Display the image (optional)
    image.show()
    
    '''
