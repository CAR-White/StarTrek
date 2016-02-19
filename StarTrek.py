# Star Treck

#Python modules
import random

# Game parametrs
universeSize = 60           # Universe size is a square
Kprob=30                    # Probability of Universe cord having a Klingon
Sprob=10                    # Probability of Universe cord having a space station
Wprob=5                     # Probability of Universe cord having a worm hole

srsRange = 3                # Short range scan range

# Variable initilisation
K_in_universe = 0;          # Number of Klingons in universe
S_in_universe = 0;	    # Space Stations in universe


# Function to return a random number between 0 and 100
def rand_100():
    return random.randint(0,100)


# Create a universe of size universeSize with a random selection of
# Klingons (K), space stations (S) and worm holes (W)

#First initilise the universe so each co-ordinate to empty (-)
Universe = [["-" for x in range(universeSize)] for x in range(universeSize)]

for ux in range(0, universeSize-1):
    for uy in range(0, universeSize-1):
        if rand_100() < Kprob:
            Universe[ux][uy] = "K"
            K_in_universe += 1
        elif rand_100() < Sprob:
            Universe[ux][uy] = "S"
            S_in_universe += 1
        elif rand_100() < Wprob:
            Universe[ux][uy] = "W"
        #else:
        #    Universe[ux][uy] = "-"


# Place the Star Ship Enterprise somewhere in the universe. It must never
# be closer to the edge by less than one short range scan.
ex = random.randint(srsRange, universeSize-srsRange)
ey = random.randint(srsRange, universeSize-srsRange)
Universe[ex][ey] = "E"



print("-----------------------------------------")
print("Welcome to Star Treck, the final Frontier")

