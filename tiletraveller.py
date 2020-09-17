# The Tile Traveller - GAME
# -----------------------------
# Segja notanda [1,1] hvert hann getur farið.
# Biðja notanda um að velja átt.
# Sýna notanda hvert hann geti farið.
    # Ef notandi velur ranga átt, sýna villumeldingu.
# Notandi settur í viðkomandi "Tile".

# Búa til if-setningu sem leyfir eftirfarandi útgönguleiðir fyrir hvert "Tile"

# Tile [1,1]    Tile [1,2]  Tile [1,3]
    # North     # North     # South
                # South     # East
                # East

# Tile [2,1]    Tile [2,2]  Tile [2,3]
    # North     # West      # East
                # South     # West

# Tile [3,1]   Tile [3,2]   Tile [3,3]
    # North     # North     # West
                # South     # South

# Þegar notandi lendir á "Tile" [3,1] prentast út "Victory!"


def tile_1_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    
    if direction == "N" or direction == "n":
        return tile_1_2()
    else:
        print("Not a valid direction!")
        return tile_1_1()
    

def tile_1_2():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    
    if direction == "N" or direction == "n":
        return tile_1_3()
    elif direction == "E" or direction == "e":
        return tile_2_2()
    elif direction == "S" or direction == "s":
        return tile_1_1()
    else:
        print("Not a valid direction!")
        return tile_1_2()

def tile_1_3():
    print("You can travel: (E)ast or (S)outh.")
    direction = input("Direction: ")

    if direction == "E" or direction == "e":
        return tile_2_3()
    elif direction == "S" or direction == "s":
        return tile_1_2()
    else:
        print("Not a valid direction!")
        return tile_1_3()

def tile_2_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")

    if direction == "N" or direction == "n":
        return tile_2_2()
    else:
        print("Not a valid direction!")
        return tile_2_1()

def tile_2_2():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")

    if direction == "S" or direction == "s":
        return tile_2_1()
    elif direction == "W" or direction == "w":
        return tile_1_2()
    else:
        print("Not a valid direction!")
        return tile_2_2()

def tile_2_3():
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ")

    if direction == "E" or direction == "e":
        return tile_3_3()
    elif direction == "W" or direction == "w":
        return tile_1_3()
    else:
        print("Not a valid direction!")
        return tile_2_3()

def tile_3_1():
    print("Victory!")
    

def tile_3_2():
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")

    if direction == "N" or direction == "n":
        return tile_3_3()
    elif direction == "S" or direction == "s":
        return tile_3_1()
    else:
        print("Not a valid direction!")
        return tile_3_2()

def tile_3_3():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")

    if direction == "S" or direction == "s":
        return tile_3_2()
    elif direction == "W" or direction == "w":
        return tile_2_3()
    else:
        print("Not a valid direction!")
        return tile_3_3()

byrjun_reitur = tile_1_1()


    

