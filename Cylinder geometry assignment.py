class Cylinder():
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        print (3.142*self.radius*self.radius*self.height)
    
