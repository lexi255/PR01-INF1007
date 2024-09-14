special_coins_pos = [(1, 1), (14, 1), (1, 13), (14, 13)]
center_pos = [(12, 7), (11, 7), (13, 7), (14, 7)]

def create_board():
    # TODO Create a board with the following structure
    # 1 -> Wall
    # 0 -> Path
    
    maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # Top boundary
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Path
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1], # Internal walls
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1], # Paths
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1], # Complex paths
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1], # Open path area
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1], # Narrow passage
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], # Large open path
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], # Solid wall section
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Path
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], # Complex wall structure
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], # More paths
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], # Internal walls
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Open path
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # Extra boundary row
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # Extra boundary row
    ]

    return maze

def create_coins(board):
    coins = []

    #ligne 0
    coins.append((0,0))
    coins.append((1,0))
    coins.append((2,0))
    coins.append((3,0))
    coins.append((4,0))
    coins.append((5,0))
    coins.append((6,0))
    coins.append((7,0))
    coins.append((8,0))
    coins.append((9,0))
    coins.append((10,0))
    coins.append((11,0))
    coins.append((12,0))
    coins.append((13,0))

    #ligne 1  
    coins.append((0,1))
    coins.append((3,1))
    coins.append((6,1))
    coins.append((10,1))
    coins.append((13,1))

    #ligne 2 
    coins.append((0,2))
    coins.append((1,2))
    coins.append((2,2))
    coins.append((3,2))
    coins.append((4,2))
    coins.append((6,2))
    coins.append((8,2))
    coins.append((9,2))
    coins.append((10,2))
    coins.append((11,2))
    coins.append((12,2))
    coins.append((13,2))

    #ligne 3 
    coins.append((0,3))
    coins.append((2,3))
    coins.append((4,3))
    coins.append((5,3))
    coins.append((6,3))
    coins.append((8,3))
    coins.append((10,3))
    coins.append((13,3))

    #ligne 
    coins.append((0, 4))
    coins.append((1, 4))
    coins.append((1, 4))
    coins.append((4, 4))
    coins.append((6, 4))
    coins.append((7, 4))
    coins.append((8, 4))
    coins.append((9, 4))
    coins.append((10, 4))
    coins.append((11, 4))
    coins.append((13, 4))

    #ligne 5
    coins.append((0, 5))
    coins.append((2, 5))
    coins.append((3, 5))
    coins.append((4, 5))
    coins.append((7, 5))
    coins.append((11, 5))
    coins.append((13, 5))

    #ligne 6 
    coins.append((0,6))
    coins.append((2,6))
    coins.append((4,6))
    coins.append((5,6))
    coins.append((6,6))
    coins.append((7,6))
    coins.append((8,6))
    coins.append((9,6))
    coins.append((11,6))
    coins.append((12,6))
    coins.append((13,6))

    #ligne 7 
    coins.append((0, 7))
    coins.append((2, 7))
    coins.append((5, 7))
    coins.append((7, 7))
    coins.append((9, 7))
    coins.append((11, 7))
    coins.append((13, 7))

    #ligne 8 
    coins.append((0, 8))
    coins.append((1, 8))
    coins.append((2, 8))
    coins.append((4, 8))
    coins.append((5, 8))
    coins.append((6, 8))
    coins.append((7, 8))
    coins.append((8, 8))
    coins.append((9, 8))
    coins.append((10, 8))
    coins.append((11, 8))
    coins.append((12, 8))
    coins.append((13, 8))

    #ligne 9 
    coins.append((0, 9))
    coins.append((2, 9))
    coins.append((4, 9))
    coins.append((9, 9))
    coins.append((13, 9))

    #ligne 10 
    coins.append((0,10))
    coins.append((1,10))
    coins.append((2,10))
    coins.append((3,10))
    coins.append((4,10))
    coins.append((6,10))
    coins.append((7,10))
    coins.append((8,10))
    coins.append((9,10))
    coins.append((11,10))
    coins.append((12, 10))
    coins.append((13 ,10))

    #ligne 11 
    coins.append((0, 11))
    coins.append((3, 11))
    coins.append((6, 11))
    coins.append((9, 11))
    coins.append((11, 11))
    coins.append((13, 11))

    #ligne 13
    coins.append((0,13))
    coins.append((1,13))
    coins.append((2,13))
    coins.append((3,13))
    coins.append((4,13))
    coins.append((5,13))
    coins.append((6,13))
    coins.append((7,13))
    coins.append((8,13))
    coins.append((9,13))
    coins.append((10,13))
    coins.append((11,13))
    coins.append((12,13))
    coins.append((13,13))
    
    return coins

def remove(board):
    special_coin_pos=[]
    special_coins_pos.pop((0,0))
    special_coins_pos.pop((0,12))
    special_coins_pos.pop((13,0))
    special_coins_pos.pop((13,12))
    return special_coins_pos

def remove(board):
    center_pos = []
    center_pos.pop((4, 7))
    center_pos.pop((5, 7))
    center_pos.pop((6, 7))
    center_pos.pop((7, 7))
    center_pos.pop((8, 7))
    center_pos.pop((9, 7))
    return center_pos
   

def create_special_(board):
    special_coins= []
    special_coins.append((0,0))
    special_coins.append((0,12))
    special_coins.append((13,0))
    special_coins.append((13,12))
    return special_coins
