# Star Treck

# To-do:
# def ins()
# max_Date
# need to sort out issue when Enterprise is at edge of universe


#Modules
import random

# Game parametrs (constants:- should not be programtiacally modified)
universeSize = 60           # Universe size is a square (60)
Kprob=65                    # Probability of Universe cord having a Klingon (20)
Sprob=15                     # Probability of Universe cord having a space station (8)
Wprob=5                     # Probability of Universe cord having a worm hole (5)
srsRange = 3                # Short range scan range

# Variable initilisation
K_inUniverse = 0;           # Number of Klingons in universe
S_inUniverse = 0;	    # Space Stations in universe

# Global variables
#global K_inSector
#global S_inSector
#global W_inSector

global srsFlag
srsFlag = 1
global lrsFlag
lrsFlag = 1
global squadFlag
squadFlag = 1
global phaserFlag
phaserFlag = 1
global ptFlag
ptFlag = 1
global warpFlag
warpFlag = 1
global impulseFlag
impulseFlag = 1
global starDate
starDate = 1000

global energy

# Functions

# Clear screen
def clears():
    for i in range(60):
        print("")
    return

# Print lines
def lines(nl):
    for i in range(nl):
        print("")
    return

# Return a random number between 0 and 100
def rand(n):
    return random.randint(0,n)

# Short range scan with no print to get sector stats simular to srs but no display
# ssx, ssy :- Short Range Scan cords
def srs_noprint():
    K_inSector = 0;
    S_inSector = 0;
    W_inSector = 0;

    for ssx in range(ex-srsRange, ex+srsRange):
       for ssy in range(ey-srsRange, ey+srsRange):
          # To-do need to sort out issue when Enterprise is at edge of universe
          #  if ( ssx>0 and ssx<universeSize and ssy>0 and ssy<universeSize):
                if (Universe[ssx][ssy] == "K"):
                    K_inSector +=1
                elif (Universe[ssx][ssy] == "S"):
                    S_inSector +=1
                elif (Universe[ssx][ssy] == "W"):
                    W_inSector +=1
    return

# Short range scan 
# ssx, ssy :- Short Range Scan cords
def srs():
    K_inSector = 0;
    S_inSector = 0;
    W_inSector = 0;
    global energy
    energy -=1

    if srsFlag <=0:
        clears()
        print("Short Range Scan not available")
        return
    else:
        print(" "*12 + "8" + " "*(srsRange+3) + "  1" + " "*(srsRange+3) + "  2")
        for ssx in range(ex-srsRange, ex+srsRange+1):
            if ssx==ex:
                print(" "*12 + "7 ", end=" ")
            else:
                print(" "*14, end =" ")            
    
            for ssy in range(ey-srsRange, ey+srsRange+1):
                if ssx<0 or ssx > universeSize-1:
                    print("  ", end =" ")
                elif ssy<0 or ssy > universeSize-1:
                    print("  ", end =" ")
                else:
                    print(Universe[ssx][ssy], end=" ")
                    if (Universe[ssx][ssy] == "K"):
                        K_inSector +=1
                    if (Universe[ssx][ssy] == "S"):
                        S_inSector +=1
                    if (Universe[ssx][ssy] == "W"):
                        W_inSector +=1                 
                if ssy==ey+srsRange and ssx==ex:
                    print(" 3", end=" ")
            print("")
        print(" "*12 + "6" + " "*(srsRange+3) + "  5" + " "*(srsRange+3) + "  4")                             
    return

# Status report
def strpt():
    global srsFlag
    global lrsFlag
    global squadFlag
    global phaserFlag
    global ptFlag
    global warpFlag
    global impulseFlag

    srs_noprint()

    print("Status Report: STAR DATE: xxx. Life support systems available until: xxx")
    print("--------------------------------------------------------------------------")
    print("Position: " + str(ex) +":" + str(ey))
    print("Energy:            ")
    print("Shields:           ")
    print("Phasers:           ")
    print("Photon torpedoes:  ")

    if (srsFlag > 0):
        print("SRS operational")
    else:
        print("SRS unavailable")
    if (lrsFlag > 0):
        print("LRS operational")
    else:
        printf("LRS unavailable")
    if (squadFlag > 0):
        print("Save Quadrant operational")
    else:
        print("Save Quadrant unavailable")
    if (phaserFlag > 0):
        print("Phasers operational")
    else:
        print("Phasers unavailable")
    if (ptFlag > 0):
        print("Photon Torpedoes operational")
    else:
        print("Photon Torpedoes unavailable")
    if (warpFlag > 0):
        print("Warp power available");
    else:
        print("Warp power unavailable");
    if (impulseFlag > 0):
        print("Impulse power available");
    else:
        print("Impulse power unavailable");
    print("")

    #print("Klingons in sector: " + str(K_inSector))
    #printf("Klingons in universe:  %3d\n", K_in_universe);
    #printf("Space Stations in universe: %3d\n\n", SS_in_universe);
    #printf("Saved Quadrants: Q0: K=%2d S=%2d W=%2d   Q1: K=%2d S=%2d W=%2d\n", ssK[0], ssS[0], ssW[0], ssK[1], ssS[1], ssW[1]);
    #printf("                 Q2: K=%2d S=%2d W=%2d   Q3: K=%2d S=%2d W=%2d\n\n", ssK[2], ssS[2], ssW[2], ssK[3], ssS[3], ssW[3]);



# Game introduction
def intro():
    clears()
    lines(8)
    print("\t\t\t * * * * * * * * * * *  *")
    print("\t\t\t *    **************    *")
    print("\t\t\t *    * STAR TRECK *    *")
    print("\t\t\t *    **************    *")
    print("\t\t\t *                      *")
    print("\t\t\t * Version 1.0          *")
    print("\t\t\t * By William White     *")
    print("\t\t\t * * * * * * * * * * *  *")
    lines(8)
    print("To list instrictions at any time type 'ins' at the command prompt.");
    print("Type <RETURN> to continue");
    input()



# ********************************************************************************
#                                 Main Program
# ********************************************************************************


# Create a universe of size "universeSize" with a random selection of
# Klingons (K), space stations (S) and worm holes (W)

#First initilise the universe so each co-ordinate is empty (-)
Universe = [["-" for x in range(universeSize)] for y in range(universeSize)]

#Populate the universe with Klingons, space stations and worm holes
for ux in range(0, universeSize):
    for uy in range(0, universeSize):
        #ran = rand_100()
        if rand(1000) < Kprob:
            Universe[ux][uy] = "K"
            K_inUniverse += 1
        elif rand(1000) < Sprob:
            Universe[ux][uy] = "S"
            S_inUniverse += 1
        elif rand(1000) < Wprob:
            Universe[ux][uy] = "W"
        #else:
        #    Universe[ux][uy] = "-"

# Place the Star Ship Enterprise somewhere in the universe. It must never
# be closer to the edge by less than one short range scan.
ex = random.randint(srsRange, universeSize-srsRange)
ey = random.randint(srsRange, universeSize-srsRange)

# decrement K/S count in case the Enterprise removes one
if Universe[ex][ey] == "K":
    K_inUniverse -= 1
if Universe[ex][ey] == "S":
    S_inUniverse -= 1

Universe[ex][ey] = "E"

# max_starDate is more comples than this. See original C code
max_starDate = K_inUniverse * 18
max_energy = (4 * universeSize)
energy = max_energy;

intro()
clears()
#ins()
strpt()

command=""
while command != "ex":

    if (starDate > max_starDate):
        clears()
        print("\nYou have run out of time. Current star date is: " + str(starDate))
        print("You should have been finished by: " + str(max_starDate))
        break

    if (energy <= 0):
        clears()
        print("\nNo energy available")
        break
    
    print("Commands: srs, lrs, imp, wrp, wrq, sq, phr, pht, es, ep, str, ins, rep, help, ex.");
    command=input("Input command: ")
    if command=="srs":
        clears()
        srs()
    elif command=="lrs":
        clears()
    elif command=="imp":
        pd=input("Input [Power(1-3)][Direction(1-8)]: ")
        impulsePower=int(pd[0])
        impulseDirection=int(pd[1])
        #print("PD = " + str(p) + str(d))
        starDate = starDate + impulsePower
    elif command=="wrp":
        pd=input("Input [Power(0-9)][Direction(1-8)]: ")
        warpPower=int(pd[0])
        warpDirection=int(pd[1])
        starDate = starDate + 1

    else:
        clears()
        print("srs    	- Short Range Scan.")
        print("lrs    	- Long Range Scan.")
        print("imp 	- Impulse Power.")
        print("wrp	- Warp Power ( 2 for one sector move, 0 = hyoperspace ).")
        print("wrq	- Warp to saved quadrant.")
        print("sq	- Save Quadrant.")
        print("phr	- Phasers.")
        print("pht	- Photon Torpedoes.")
        print("es	- Energise Shields ( Max 100 ).")
        print("ep	- Energise Phasers ( Max 100 ).")
        print("str    	- Status Report.")
        print("sq	- Save Quadrant.")
        print("save	- Save game (note: only one game can be saved).")
        print("load	- Load game.")
        print("help   	- Help.")
        print("ins	- Print full instructions.")
        print("ex     	- End Game.\n")
        print("A 0 used in any command parameter (except Warp power 0 which")
        print("represents Warp Factor 10) results in the command being aborted")
        lines(1)




print("Gane Over")








