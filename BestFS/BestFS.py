import math

#        1,2,3,4,5,6,7,8,9,10

from math import sqrt


grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

def giveCost(x):
    return x[2]


def Manhattan(Ax,Ay,Bx,By):
    return abs(Ax-Bx)+abs(Ay-By)

def Euclidian(Ax,Ay,Bx,By):
    return math.sqrt((Ax-Bx)**2 + (Ay-By)**2)



def BestFirstManhattan(Sx , Sy , Gx , Gy , grid) :
    OL = []
    CL = []
    OL.append([Sx,Sy,Manhattan(Sx,Sy,Gx,Gy)])


    while(len(OL)!=0):

        OL.sort(key=giveCost)
        print("OL : ",OL)

        ele = OL.pop(0)
        x = ele[0]
        y = ele[1]
        c = ele[2]
        
        if(grid[x][y]!=0):
            print("Already marked")
            print("-------------------------------------------")
            continue

        grid[x][y] = 2 # mark as visited

        print("N  = ",x,",",y)

        CL.append([x,y])
        print("CL : ",CL)

        if(x==Gx and y==Gy):
            print("GT = True")
            break
        else:
            print("GT = False")


        print("Successors : ")

        if(x-1>=0 and grid[x-1][y]==0 and OL.count([x-1,y,Manhattan(x-1,y,Gx,Gy)])==0): # up
            OL.append([x-1,y,Manhattan(x-1,y,Gx,Gy)])
            print(x-1,y,Manhattan(x-1,y,Gx,Gy))

        if(y+1<=9 and grid[x][y+1]==0 and OL.count([x,y+1,Manhattan(x,y+1,Gx,Gy)])==0): # right
            OL.append([x,y+1,Manhattan(x,y+1,Gx,Gy)])
            print(x,y+1,Manhattan(x,y+1,Gx,Gy))
        
        if(x+1<=9 and grid[x+1][y]==0 and OL.count([x+1,y,Manhattan(x+1,y,Gx,Gy)])==0): # down
            OL.append([x+1,y,Manhattan(x+1,y,Gx,Gy)])
            print(x+1,y,Manhattan(x+1,y,Gx,Gy))
        
        if(y-1>=0 and grid[x][y-1]==0 and OL.count([x,y-1,Manhattan(x,y-1,Gx,Gy)])==0): # left
            OL.append([x,y-1,Manhattan(x,y-1,Gx,Gy)])
            print(x,y-1,Manhattan(x,y-1,Gx,Gy))
        
        

        print("-------------------------------------------")



def BestFirstEuclidian(Sx , Sy , Gx , Gy , grid) :
    OL = []
    CL = []
    OL.append([Sx,Sy,Euclidian(Sx,Sy,Gx,Gy)])


    while(len(OL)!=0):

        OL.sort(key=giveCost)
        print("OL : ",OL)

        ele = OL.pop(0)
        x = ele[0]
        y = ele[1]
        c = ele[2]
        
        if(grid[x][y]!=0):
            print("Already marked")
            print("-------------------------------------------")
            continue

        grid[x][y] = 2 # mark as visited

        print("N  = ",x,",",y)

        CL.append([x,y])
        print("CL : ",CL)

        if(x==Gx and y==Gy):
            print("GT = True")
            break
        else:
            print("GT = False")


        print("Successors : ")

        if(x-1>=0 and grid[x-1][y]==0 and OL.count([x-1,y,Euclidian(x-1,y,Gx,Gy)])==0): # up
            OL.append([x-1,y,Euclidian(x-1,y,Gx,Gy)])
            print(x-1,y,Euclidian(x-1,y,Gx,Gy))

        if(y+1<=9 and grid[x][y+1]==0 and OL.count([x,y+1,Euclidian(x,y+1,Gx,Gy)])==0): # right
            OL.append([x,y+1,Euclidian(x,y+1,Gx,Gy)])
            print(x,y+1,Euclidian(x,y+1,Gx,Gy))
        
        if(x+1<=9 and grid[x+1][y]==0 and OL.count([x+1,y,Euclidian(x+1,y,Gx,Gy)])==0): # down
            OL.append([x+1,y,Euclidian(x+1,y,Gx,Gy)])
            print(x+1,y,Euclidian(x+1,y,Gx,Gy))
        
        if(y-1>=0 and grid[x][y-1]==0 and OL.count([x,y-1,Euclidian(x,y-1,Gx,Gy)])==0): # left
            OL.append([x,y-1,Euclidian(x,y-1,Gx,Gy)])
            print(x,y-1,Euclidian(x,y-1,Gx,Gy))
        
        

        print("-------------------------------------------")



# BestFirstManhattan(0,0,1,3,grid)

BestFirstEuclidian(0,0,1,3,grid)
