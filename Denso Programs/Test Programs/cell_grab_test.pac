'!TITLE "Cell Grab Test"
PROGRAM Cell_Grab_Test
TAKEARM 0 keep=0
SPEED 20

S10 = "compressorOn"
S11 = "compressorOff"
S12 = "END"

'Establish connection to the Pi
com_discom #9

DEFINT flg
com_state #9,flg
IF flg=-1 THEN
  com_encom #9
  MOVE P, @0 J0 'Starting position
  DELAY 1000
ENDIF

'Grab the Base ******************** ---- NEED TO CHANGE ALL VARIABLES!
MOVE P, @0 J84 'baseApproach
MOVE P, @0 J85 'touchBase

'Turn on the compressor
PRINT #9,S10
DELAY 3000

MOVE L, @0 J86 'aboveBase
MOVE P, @0 J88 'rotateBase
MOVE L, @0 J89 'placeBase

'Turn off the compressor
PRINT #9,S11
DELAY 3000
'**********************************

'Grabbing the Cells *************** 
MOVE P, @0 J90 'aboveCells
MOVE P, @0 J91 'touch

'Turn on the compressor
PRINT #9,S10
DELAY 2000

MOVE L, @0 J92 'slide
MOVE P, @0 J93 'rise
'**********************************
 
'Move to the first cells location
MOVE P, @0 J80

'Place the cells
PRINT #9,S11
DELAY 3000
 

'Grabbing the Cells *************** 
MOVE P, @0 J90 'aboveCells
MOVE P, @0 J91 'touch

'Turn on the compressor
PRINT #9,S10
DELAY 2000

MOVE L, @0 J92 'slide
MOVE P, @0 J93 'rise
'**********************************

'Move to the second cells location
MOVE P, @0 J81

'Place the cells
#Ifdef __VRC__                   ' Don't edit this block
#Else
PRINT #9,S11
#Endif
DELAY 3000

'Grabbing the Cells *************** 
MOVE P, @0 J90 'aboveCells
MOVE P, @0 J91 'touch

'Turn on the compressor
#Ifdef __VRC__                   ' Don't edit this block
#Else
PRINT #9,S10
#Endif
DELAY 2000

MOVE L, @0 J92 'slide
MOVE P, @0 J93 'rise
'**********************************

'Place the third set of cells
MOVE P, @0 J82

'Turn off the compressor
#Ifdef __VRC__                   ' Don't edit this block
#Else
PRINT #9,S11
#Endif
DELAY 3000

'Grabbing the Cells *************** 
MOVE P, @0 J90 'aboveCells
MOVE P, @0 J91 'touch

'Turn on the compressor
#Ifdef __VRC__                   ' Don't edit this block
#Else
PRINT #9,S10
#Endif
DELAY 2000

MOVE L, @0 J92 'slide
MOVE P, @0 J93 'rise
'**********************************

'Place to the fourth cells location
MOVE P, @0 J83

'Turn off the compressor
#Ifdef __VRC__                   ' Don't edit this block
#Else
PRINT #9,S11
#Endif
DELAY 3000

'Go to home position
MOVE P, @0 J0

'End Pi program
#Ifdef __VRC__                   ' Don't edit this block
#Else
PRINT #9,S12

'Disconnect from the socket
com_discom #9
#Endif
 
GIVEARM 
END
