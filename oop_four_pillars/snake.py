from reptile import  Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forker_tongue = True # It's important to set them
        self.cold_blooded =True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice?")

sidney = Snake()
# sidney.seek_heat() #