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

    #ligne 1
    coins.append((1,1))
    coins.append((2.1))
    coins.append((3,1))
    coins.append((4,1))
    coins.append((5,1))
    coins.append((6,1))
    coins.append((7,1))
    coins.append((8,1))
    coins.append((9,1))
    coins.append((10,1))
    coins.append((11,1))
    coins.append((12,1))
    coins.append((13,1))
    coins.append((14,1))

    #ligne 1 2
    coins.append((1,2))
    coins.append((4,2))
    coins.append((7,2))
    coins.append((11,2))
    coins.append((14,2))

    #ligne 3
    coins.append((1,3))
    coins.append((2,3))
    coins.append((3,3))
    coins.append((4,3))
    coins.append((5,3))
    coins.append((7,3))
    coins.append((9,3))
    coins.append((10,3))
    coins.append((11,3))
    coins.append((12,3))
    coins.append((13,3))
    coins.append((14,3))

    #ligne 4 
    coins.append((1,4))
    coins.append((3,4))
    coins.append((5,4))
    coins.append((6,4))
    coins.append((7,4))
    coins.append((9,4))
    coins.append((11,4))
    coins.append((14,4))

    #ligne 5
    coins.append((1,5))
    coins.append((2,5))
    coins.append((3,5))
    coins.append((5,5))
    coins.append((7,5))
    coins.append((8,5))
    coins.append((9,5))
    coins.append((10,5))
    coins.append((11,5))
    coins.append((12,5))
    coins.append((14,5))

    #ligne 6
    coins.append((1,6))
    coins.append((3,6))
    coins.append((4,6))
    coins.append((5,6))
    coins.append((8,6))
    coins.append((12.6))
    coins.append((14,6))

    #ligne 7
    coins.append((1,7))
    coins.append((3,7))
    coins.append((5,7))
    coins.append((6,7))
    coins.append((7,7))
    coins.append((8,7))
    coins.append((9,7))
    coins.append((10,7))
    coins.append((12,7))
    coins.append((13,7))
    coins.append((14,7))

    #ligne 8
    coins.append((1,8))
    coins.append((3,8))
    coins.append((6,8))
    coins.append((8,8))
    coins.append((10,8))
    coins.append((12,8))
    coins.append((14,8))

    #ligne 9 
    coins.append((1,9))
    coins.append((2,9))
    coins.append((3,9))
    coins.append((5,9))
    coins.append((6,9))
    coins.append((7,9))
    coins.append((8,9))
    coins.append((9,9))
    coins.append((10,9))
    coins.append((11,0))
    coins.append((12,9))
    coins.append((13,9))
    coins.append((14,9))

    #ligne 10 
    coins.append((1,10))
    coins.append((3,10))
    coins.append((5,10))
    coins.append((10,10))
    coins.append((14,10))

    #ligne 11 
    coins.append((1,11))
    coins.append((2,11))
    coins.append((3,11))
    coins.append((4,11))
    coins.append((5,11))
    coins.append((7,11))
    coins.append((8,11))
    coins.append((9,11))
    coins.append((10,11))
    coins.append((12,11))
    coins.append((13,11))
    coins.append((14,11))

    #ligne 12
    coins.append((1,12))
    coins.append((4,121))
    coins.append((7,12))
    coins.append((10,12))
    coins.append((12,12))
    coins.append((14,12))

    #ligne 13
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
    coins.append((14,13))
    
    return coins


def remove_coins(board):
    special_coin_pos=[]

    special_coins_pos.remove((1,1))
    special_coins_pos.remove((1,13))
    special_coins_pos.remove((14,1))
    special_coins_pos.remove((14,13))
    return special_coins_pos

def remove_coins(board):
    center_pos = []
    center_pos.remove((5, 7))
    center_pos.remove((6, 7))
    center_pos.remove((7, 7))
    center_pos.remove((8, 7))
    center_pos.remove((9, 7))
    center_pos.remobe((10, 7))
    return center_pos
   

def create_special_(board):
    special_coins= []
    special_coins.append((1,1))
    special_coins.append((1,13))
    special_coins.append((14,1))
    special_coins.append((14,13))
    return special_coins
