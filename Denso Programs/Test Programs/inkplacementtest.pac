'!TITLE "Ink Placement Test"
PROGRAM InkPlacementTest
TAKEARM 0 keep=0
SPEED 20

S10 = "pumpOn"
S11 = "pumpOff"
S12 = "compressorOn"
S13 = "compressorOff"
S14 = "END"

' Make sure the controller is not connected to anything
com_discom #9

' Establish connection to the Pi
DEFINT flg
com_state #9,flg
IF flg=-1 THEN
  com_encom #9
  MOVE P, @0 J0 'Starting position
  FLUSH #9
  DELAY 1000
ENDIF

'Grab the Base ********************
MOVE P, @0 J84 'baseApproach
MOVE P, @0 J85 'touchBase

'Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J86 'aboveBase
MOVE P, @0 J88 'rotateBase
MOVE L, @0 J89 'placeBase

'Turn off the compressor
PRINT #9,S13
DELAY 3000
'**********************************

' Initial move
MOVE P, @0 J84
DELAY 1000

SPEED 10

' Bottom long strip
MOVE P, @0 J43
PRINT #9,S10
MOVE L, @0 J44
PRINT #9,S11

' Top long strip
MOVE L, @0 J45
PRINT #9,S10
MOVE L, @0 J46
PRINT #9,S11

' Column 1 row 1
MOVE L, @0 J48
PRINT #9,S10
MOVE L, @0 J49
PRINT #9,S11

' Column 1 row 2
MOVE L, @0 J50
PRINT #9,S10
MOVE L, @0 J51
PRINT #9,S11

' Column 1 row 3
MOVE L, @0 J52
PRINT #9,S10
MOVE L, @0 J53
PRINT #9,S11

' Column 2 row 3
MOVE L, @0 J54
PRINT #9,S10
MOVE L, @0 J55
PRINT #9,S11

' Column 2 row 2
MOVE L, @0 J56
PRINT #9,S10
MOVE L, @0 J57
PRINT #9,S11

' Column 2 row 1
MOVE L, @0 J58
PRINT #9,S10
MOVE L, @0 J59
PRINT #9,S11

' Column 3 row 1
MOVE L, @0 J60
PRINT #9,S10
MOVE L, @0 J61
PRINT #9,S11

' Column 3 row 2
MOVE L, @0 J62
PRINT #9,S10
MOVE L, @0 J63
PRINT #9,S11

' Column 3 row 3
MOVE L, @0 J64
PRINT #9,S10
MOVE L, @0 J65
PRINT #9,S11

' Column 4 row 3
MOVE L, @0 J66
PRINT #9,S10
MOVE L, @0 J67
PRINT #9,S11

' Column 4 row 2
MOVE L, @0 J68
PRINT #9,S10
MOVE L, @0 J69
PRINT #9,S11

' Column 4 row 1
MOVE L, @0 J70
PRINT #9,S10
MOVE L, @0 J71
PRINT #9,S11

' Return to starting position
MOVE P, @0 J0

'End Pi program
PRINT #9,S14

'Disconnect from the socket
com_discom #9


GIVEARM
END
