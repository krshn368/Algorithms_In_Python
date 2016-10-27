# Imagine we have an image where every pixel is white or black. We’ll represent this image as a simple 2D array (0 = black, 1 = white). The image you get is known to have a single black rectangle on a white background. Write a function that takes in the image and returns the coordinates of the rectangle -- either top-left and bottom-right; or top-left, width, and height.

image = [
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [0, 1, 1, 1, 1, 1, 0],
]



def findAllRectangles(image):
    
    
    imageMarked =[]
    rowSize = len(image)
    colSize = len(image[0])
    
    for i in range(rowSize):
        row=[]
        for j in range(colSize):
            row.append(1)
        
        imageMarked.append(row)    
    
    
    rowSize = len(image)
    colSize = len(image[0])
    RectanglePresent = True
    
    start = 0
    
    
    while RectanglePresent:
        
        RectanglePresent = False
        for i in range(start,rowSize):
            for j in range(colSize):
                
                if image[i][j] == 0:
                    if imageMarked[i][j] == 1:
                        RectanglePresent = True
                        
                        start = i
                        topLeft = [i,j]
                        
                        while image[i][j] == 0:
                            i= i+1
                            
                        i = i-1    
                        
                        while image[i][j] == 0:
                            j= j+1
                        
                        bottomRight=[i,j-1]
                        
                        print topLeft
                        print bottomRight
                        
                        #marking image
                        
                        for k in range(topLeft[0],bottomRight[0]+1):
                            for l in range(topLeft[1],bottomRight[1]+1):
                                
                                imageMarked[k][l] =0
                        
                        
                        
                        
                    
                        break;
            if RectanglePresent == True:
                print ''
                break
                
            
            
findAllRectangles(image)            
                        
    
        
    
    







def findRectangle(image):
    
    
    rowSize = len(image)
    colSize = len(image[0])
    
    
    topLeft = []
    
    
    for i in range(rowSize):
        
        for j in range(colSize):
            
            if(image[i][j] == 0):
                topLeft = [i,j]
                break
        
        if len(topLeft) == 2:
            break
    
    
    bottomRight = []
        
    for i in range(rowSize-1,-1,-1):
        
        for j in range(colSize-1 , -1 , -1):
            
            if image[i][j] == 0:
                bottomRight = [i,j]
                break
        if len(bottomRight) == 2:
            break
     
    
    return topLeft
                
    #findRectangle(image)