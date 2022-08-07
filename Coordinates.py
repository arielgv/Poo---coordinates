# This code is intended to show the distance between two coordinates.

#Definition
class coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #This is the function / method which teach how to calculate 
    def distance(self,other_coordinate):
        newx = (self.x - other_coordinate.x)**2
        newy = (self.y - other_coordinate.y)**2
        difference = (newx + newy)**0.5
        return f'The distance between coordinates is {difference}'

#Entry point
if __name__=='__main__':
    #instances:
    Argentina = coordinate(3,30)
    Brasil = coordinate(4,8)
    print(Argentina.distance(Brasil))
    #prints the distance between coordinates.
