'!TITLE "<Title>"
PROGRAM MultiTest
TAKEARM 0 keep=0 
SPEED 20

'compressor, ink, glue, compressor

'Establish connection to the Pi
com_discom #9

DEFINT flg
com_state #9,flg
IF flg=-1 THEN
  com_encom #9
  DELAY 1000
  FLUSH #9
ENDIF

S10 = "compressorOn"
S11 = "compressorOff"

S12 = "pumpOn"
S13 = "pumpOff"

S14 = "stepOn"
S15 = "stepOff"

S16 = "END"

' Turn on the compressor for 10 seconds
PRINT #9,S10
DELAY 10000

' Turn off the compressor
PRINT #9,S11
DELAY 3000

' Turn on the pump
PRINT #9,S12
DELAY 10000

' Turn off the pump
PRINT #9,S13
DELAY 3000

' Turn on the stepper motor
PRINT #9,S14
DELAY 10000

' Turn off the stepper motor
PRINT #9,S15
DELAY 3000

' Turn on the compressor
PRINT #9,S10
DELAY 10000

' Turn off the compressor
PRINT #9,S11
DELAY 3000

PRINT #9,S16
DELAY 1000

com_discom #9
GIVEARM
END
