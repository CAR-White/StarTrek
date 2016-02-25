
#Star Trek Instructions.

The object off the game is to kill all of the Klingons in the 
universe. The Klingons are represented by the character K, the 
Enterprise by E, Space Stations by S and Worm Holes by W. You life 
support system are only available for a given amount of time. If you 
do not complete your mission within this time the game is over. When 
the game commences the star date will be 1000 and the screen will 
display the star date when your life support systems will expire, 
the number of Klingons to be destroyed and the number of Space 
Stations and Worm Holes in the universe, together with useful 
information about your operational and weapons status. Your status 
report can be displayed at any time with the command str. It will 
display the following information. 

Energy: percent energy remaining and absolute energy. Energy is 
required to power the Enterprise. You need and will consume energy 
whenever you travel using either impulse or warp power. Energy is 
also consumed when you fire a weapon or energies your shields or 
phasers.

Shields: The current energy state of your shields. When the game 
starts you shield energy will be 0. It is most important that your 
first command should be to energies you shields, not doing so could 
result in serious consequences on your first move. You shields can 
be energized with the command es. The maximum is 100 absolute energy 
units.

Phasers: The current energy state of your phasers. Once again when 
the game starts your phaser energy will be 0. You will need to 
energies your phasers with the command ep before they can be used. 
The maximum is 100 absolute energy units.

Photon Torpedoes: You have a limited number of Photon Torpedoes. 
There is no need to energies these, however some energy will be 
consumed when they are launched. 

The next section displays the operational status of your resources. 
SRS is your Short Range Scan and displays the current sector of the 
universe you are in. LRS is your Long Range Scan and will display 
information about the surrounding sectors. The area the LRS 
displays is called a quadrant. The rest of this section displays 
operational information about you weapons and energy conversion 
systems for impulse and warp power.
The final section displays information about the number of Klingons 
and Space Stations and also the current status of any saved 
quadrants.

You can dock with a Space Station simply by using impulse power and 
placing the Enterprise on the same square as the Space Station. All 
damage will be repaired and you energy will be returned to maximum. 
Before docking it is worth fully energising your phasers and shields 
but make sure you have enough energy remaining to performing the 
docking procedure. The amount of time spent docked with the Space 
Station will depend on how badly damaged you are.

If you enter a Worm Hole you will be randomly placed somewhere else 
in the universe. However if the Worm Hole is unstable you run the 
risk of being damaged.

Commands
--------

Short Range Scan - srs
----------------------
A srs command will display the current sector with the Enterprise 
in the center. If a square does not contain an object ( E, K, S, W ) 
then a - will be displayed showing that square is empty.

Long Range Scan - lrs
---------------------
A lrs will display the number of Klingons, Space Stations and Worm 
Holes in the surrounding sectors. The center sector is the current 
sector in which is the Star Ship Enterprise ( SS E ). To get the 
Klingon, Space Station and Worm Hole numbers for this sector you 
need to run a srs.

Impulse Power - imp
-------------------
imp will allow you to move the Enterprise by short distances ( up to 
3 squares ). After typing imp followed by <RETURN>, you will be 
prompted to enter two numbers in the form xy for power and direction. 
The power is a number from 1 to 3 indicating the number of squares 
to move. The direction is a number from 1 to 8 indicating the 
direction of movement as shown on the Short Range Scan. For example 
38 will move the Enterprise three squares to the top left of the 
scan and 24 will move the enterprise two units to the bottom right 
of the scan.

Warp Power - wrp
----------------
wrp will move the Enterprise by larger distances. Once again after 
typing wrp followed by <RETURN>, you will be prompted to enter two 
numbers in the form xy for power and direction. Power is a number 
from 1 to 9 indicating the warp factor as shown in the table below 
and direction is used in the same way as in impulse power and is 
indicated by the sector number. 

     Factor   Squares

        1        4 
        2        7 ie 1 Sector
        3       10
        4       13
        5       16
        6       19
        7       22
        8       25
        9       28

If you use 0 for power ( the number used for direction is then 
irrelevant ), this indicates warp factor 10 which will take the 
Enterprise into Hyperspace. The Enterprise will appear somewhere 
else in the Universe unknown to you.

Warp Power to Saved Quadrant - wrq
----------------------------------
wrq will move the Enterprise to a previously saved quadrant using 
the save quadrant command. You will be prompted for the quadrant 
number after typing the wrq command.

Save Quadrant - sq
------------------
You may wish to save the current universe coordinates so that you 
can return to this quadrant at a future time with the wrq command. 
You can save up to four quadrants from 0 to 3. Once they have been 
saved information about the number of Klingons, Space Stations and 
Worm Holes in that quadrant is displayed in the Status report using 
the str command.

Warp power is a "blind" maneuver so there is a distinct possibility 
of colideing with something ie Klingons or Space Stations which will 
cause the Enterprise damage.
 
Phasers - ep, phr
-----------------
Before phasers can be fired they must be energized. The current 
energy status of your phasers are shown in the status report. The 
maximum amount of energy that you phasers can have is 100. They can 
be energized to this maximum at any time with the Energies Phasers 
command ep. Phasers can be used up to a maximum range of six squares
consuming three units of power per square each time they are fired. 
So in order to destroy a Klingon that is two squares away from the 
Enterprise you will need to fire phasers with a power of two and 
this will consume 6 units of energy from your phasers. Phasers will 
destroy one Klingon at a time. The phr command follows the same 
format as the imp ( impulse power ) command. 

Photon Torpedoes - pht
----------------------
You have a finite number of Photon Torpedoes when the games 
commences and this is shown in you Status Report. A Photon Torpedo 
will destroy all Klingons directly surrounding the target Klingon 
(or target square ). When photon torpedoes are fired using the pht 
command they will consume energy to the values of the power 
parameter. The pht command follows the same format as the phr 
conmmand.

Energies Shields or Phasers -es, ep
-----------------------------------

es - energies shields and ep - energies phasers will allow you to 
energies these resources. When the game commences shield energy will 
be zero. If you do not energies your shields as you first move you 
will almost certainly sustain server damage. 

Status Report - str
-------------------

str will display your current status.
