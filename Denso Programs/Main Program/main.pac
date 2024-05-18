'!TITLE "<Title>"
PROGRAM Main
TAKEARM 0 keep=0
SPEED 30

' Set up message variables
S10 = "pumpOn"
S11 = "pumpOff"
S12 = "compressorOn"
S13 = "compressorOff"
S14 = "stepOn"
S15 = "stepReverse"
S16 = "END"

' Make sure the controller is not connected to anything
com_discom #9

' Establish connection to the Pi
DEFINT flg
com_state #9,flg
IF flg=-1 THEN
  com_encom #9
  MOVE P, @0 J0 ' Starting position
  FLUSH #9
  DELAY 1000
ENDIF



' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' PLACING THE SUBSTRATE

' Touch the substrate
MOVE P, @0 J84 ' baseApproach
MOVE P, @0 J85 ' touchBase

' Turn on the compressor
PRINT #9,S12
DELAY 1000

' Rotate and place the substrate
MOVE L, @0 J86 ' aboveBase
MOVE L, @0 J87 ' safeToRotate
MOVE P, @0 J88 ' rotateBase
MOVE L, @0 J89 ' slideBase
MOVE P, @0 J90 ' placeBase

' Turn off the compressor
PRINT #9,S13
DELAY 1000

MOVE P, @0 J96 ' placeBase


' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' Print the Conductive Ink

' Ready position
MOVE P, @0 J84
DELAY 1000

' Bottom long strip
MOVE P, @0 J52
SPEED 4
PRINT #9,S10
DELAY 7000
MOVE L, @0 J53
PRINT #9,S11

' Change speed in-between moves to save time
SPEED 30
' In-between
MOVE P, @0 J49

' Top long strip
MOVE L, @0 J54
SPEED 4
PRINT #9,S10
MOVE L, @0 J55
PRINT #9,S11
MOVE L, @0 J54

SPEED 30
' In-between
MOVE P, @0 J40

' Column 1 row 1
MOVE L, @0 J56
SPEED 6
PRINT #9,S10
MOVE L, @0 J57
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J40

' Column 1 row 2
MOVE L, @0 J58
SPEED 6
PRINT #9,S10
MOVE L, @0 J59
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J41

' Column 1 row 3
MOVE L, @0 J60
SPEED 6
PRINT #9,S10
MOVE L, @0 J61
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J42

' Column 2 row 3
MOVE L, @0 J62
SPEED 6
PRINT #9,S10
MOVE L, @0 J63
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J43

' Column 2 row 2
MOVE L, @0 J64
SPEED 6
PRINT #9,S10
MOVE L, @0 J65
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J44

' Column 2 row 1
MOVE L, @0 J66
SPEED 6
PRINT #9,S10
MOVE L, @0 J67
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J45

' Column 3 row 1
MOVE L, @0 J68
SPEED 4
PRINT #9,S10
MOVE L, @0 J69
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J46

' Column 3 row 2
MOVE L, @0 J70
SPEED 6
PRINT #9,S10
MOVE L, @0 J71
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J47

' Column 3 row 3
MOVE L, @0 J72
SPEED 6
PRINT #9,S10
MOVE L, @0 J73
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J48

' Column 4 row 3
MOVE L, @0 J74
SPEED 6
PRINT #9,S10
MOVE L, @0 J75
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J49

' Column 4 row 2
MOVE L, @0 J76
SPEED 6
PRINT #9,S10
MOVE L, @0 J77
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J50

' Column 4 row 1
MOVE L, @0 J78
SPEED 6
PRINT #9,S10
MOVE L, @0 J79
PRINT #9,S11

SPEED 30

' Return to ready position
MOVE P, @0 J84


' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' Place the Hot Glue

MOVE P, @0 J11 ' In-between

MOVE P, @0 J1 ' Place glue #1
PRINT #9, S14 ' Press the glue stick
DELAY 17500   ' The first press required more time to allow the glue to melt
PRINT #9, S15 ' Retract glue stick
DELAY 1000

MOVE P, @0 J11 ' In-between

MOVE P, @0 J2 ' Place glue #2
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J11, J12 ' In-between

MOVE P, @0 J3 ' Place glue #3
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J12 ' In-between

MOVE P, @0 J4 ' Place glue #4
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J12, J13 ' In-between

MOVE P, @0 J5 ' Place glue #5
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J13 ' In-between

MOVE P, @0 J6 ' Place glue #6
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J13, J14 ' In-betweens

MOVE P, @0 J7 ' Place glue #7
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J14 ' In-between

MOVE P, @0 J8 ' Place glue #8
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J14 ' In-between



' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' Place the Cells

' Grabbing the first set of cells 
MOVE P, @0 J91 ' aboveCells
MOVE P, @0 J92 ' touch

' Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 ' slide
MOVE P, @0 J94 ' rise

' Move to the first cells location
MOVE L, @0 J80

' Turn off the compressor
PRINT #9,S13
DELAY 3000
'******************************

' Grabbing the next cells  
MOVE P, @0 J91 ' aboveCells
MOVE P, @0 J92 ' touch

' Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 ' slide
MOVE P, @0 J94 ' rise

' Move to the second cells location
MOVE L, @0 J81

' Place the cells
PRINT #9,S13
DELAY 3000
'******************************

' Grabbing the next set of cells 
MOVE P, @0 J91 ' aboveCells
MOVE P, @0 J92 ' touch

' Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 ' slide
MOVE P, @0 J94 ' rise

' Place the third set of cells
MOVE L, @0 J82

' Turn off the compressor
PRINT #9,S13
DELAY 3000
'******************************

' Grabbing the next set of cells 
MOVE P, @0 J91 'aboveCells
MOVE P, @0 J92 'touch

'Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 'slide
MOVE P, @0 J94 'rise

'Place to the fourth cells location
MOVE L, @0 J83

'Turn off the compressor
PRINT #9,S13
DELAY 2000
'******************************

' Move to the home position
MOVE P, @0 J0

' From here, the entire process repeats.
' We were unable to get functions or loops to work in Wincaps, so this our the alternative.
' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' PLACING THE SUBSTRATE

' Touch the substrate
MOVE P, @0 J84 ' baseApproach
MOVE P, @0 J85 ' touchBase

' Turn on the compressor
PRINT #9,S12
DELAY 1000

' Rotate and place the substrate
MOVE L, @0 J86 ' aboveBase
MOVE L, @0 J87 ' safeToRotate
MOVE P, @0 J88 ' rotateBase
MOVE L, @0 J89 ' slideBase
MOVE P, @0 J90 ' placeBase

' Turn off the compressor
PRINT #9,S13
DELAY 1000



' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' Print the Conductive Ink

' Ready position
MOVE P, @0 J84
DELAY 1000

' Bottom long strip
MOVE P, @0 J52
SPEED 4
PRINT #9,S10
DELAY 7000
MOVE L, @0 J53
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J49

' Top long strip
MOVE L, @0 J54
SPEED 4
PRINT #9,S10
MOVE L, @0 J55
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J40

' Column 1 row 1
MOVE L, @0 J56
SPEED 6
PRINT #9,S10
MOVE L, @0 J57
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J40

' Column 1 row 2
MOVE L, @0 J58
SPEED 6
PRINT #9,S10
MOVE L, @0 J59
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J41

' Column 1 row 3
MOVE L, @0 J60
SPEED 6
PRINT #9,S10
MOVE L, @0 J61
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J42

' Column 2 row 3
MOVE L, @0 J62
SPEED 6
PRINT #9,S10
MOVE L, @0 J63
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J43

' Column 2 row 2
MOVE L, @0 J64
SPEED 6
PRINT #9,S10
MOVE L, @0 J65
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J44

' Column 2 row 1
MOVE L, @0 J66
SPEED 6
PRINT #9,S10
MOVE L, @0 J67
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J45

' Column 3 row 1
MOVE L, @0 J68
SPEED 4
PRINT #9,S10
MOVE L, @0 J69
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J46

' Column 3 row 2
MOVE L, @0 J70
SPEED 6
PRINT #9,S10
MOVE L, @0 J71
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J47

' Column 3 row 3
MOVE L, @0 J72
SPEED 6
PRINT #9,S10
MOVE L, @0 J73
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J48

' Column 4 row 3
MOVE L, @0 J74
SPEED 6
PRINT #9,S10
MOVE L, @0 J75
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J49

' Column 4 row 2
MOVE L, @0 J76
SPEED 6
PRINT #9,S10
MOVE L, @0 J77
PRINT #9,S11

SPEED 30
' In-between
MOVE P, @0 J50

' Column 4 row 1
MOVE L, @0 J78
SPEED 6
PRINT #9,S10
MOVE L, @0 J79
PRINT #9,S11

SPEED 30

' Return to ready position
MOVE P, @0 J84


' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' Place the Hot Glue

MOVE P, @0 J11 ' In-between

MOVE P, @0 J1 ' Place glue #1
PRINT #9, S14 ' Press the glue stick
DELAY 17500   ' The first press required more time to allow the glue to melt
PRINT #9, S15 ' Retract glue stick
DELAY 1000

MOVE P, @0 J11 ' In-between

MOVE P, @0 J2 ' Place glue #2
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J11, J12 ' In-between

MOVE P, @0 J3 ' Place glue #3
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J12 ' In-between

MOVE P, @0 J4 ' Place glue #4
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J12, J13 ' In-between

MOVE P, @0 J5 ' Place glue #5
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J13 ' In-between

MOVE P, @0 J6 ' Place glue #6
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 500

MOVE P, @0 J13, J14 ' In-betweens

MOVE P, @0 J7 ' Place glue #7
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J14 ' In-between

MOVE P, @0 J8 ' Place glue #8
PRINT #9, S14
DELAY 12500
PRINT #9, S15
DELAY 1000

MOVE P, @0 J14 ' In-between



' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
' Place the Cells

' Grabbing the first set of cells 
MOVE P, @0 J91 ' aboveCells
MOVE P, @0 J92 ' touch

' Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 ' slide
MOVE P, @0 J94 ' rise

' Move to the first cells location
MOVE L, @0 J80

' Turn off the compressor
PRINT #9,S13
DELAY 3000
'******************************

' Grabbing the next cells  
MOVE P, @0 J91 ' aboveCells
MOVE P, @0 J92 ' touch

' Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 ' slide
MOVE P, @0 J94 ' rise

' Move to the second cells location
MOVE L, @0 J81

' Place the cells
PRINT #9,S13
DELAY 3000
'******************************

' Grabbing the next set of cells 
MOVE P, @0 J91 ' aboveCells
MOVE P, @0 J92 ' touch

' Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 ' slide
MOVE P, @0 J94 ' rise

' Place the third set of cells
MOVE L, @0 J82

' Turn off the compressor
PRINT #9,S13
DELAY 3000
'******************************

' Grabbing the next set of cells 
MOVE P, @0 J91 'aboveCells
MOVE P, @0 J92 'touch

'Turn on the compressor
PRINT #9,S12
DELAY 2000

MOVE L, @0 J93 'slide
MOVE P, @0 J94 'rise

'Place to the fourth cells location
MOVE L, @0 J83

'Turn off the compressor
PRINT #9,S13
DELAY 2000
'******************************



'Go to home position
MOVE P, @0 J0

' End Pi program
PRINT #9,S16

' Disconnect from the socket
com_discom #9

GIVEARM
END
