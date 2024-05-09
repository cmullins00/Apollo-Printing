'!TITLE "<Title>"
PROGRAM StepperMotorTest
TAKEARM 0 keep=0
SPEED 20

' Establish connection to the Pi
com_discom #9

DEFINT flg
com_state #9,flg
IF flg=-1 THEN
  com_encom #9
  DELAY 1000
  FLUSH #9
ENDIF

' Turn on the motor
S10 = "stepOn"
PRINT #9,S10
DELAY 5000

' Turn off the motor
'S10 = "stepOff"
'PRINT #9,S10
'DELAY 1000

' Reverse the motor direction
S10 = "stepReverse"
PRINT #9,S10
DELAY 5000

S10 = "END"
PRINT #9,S10
com_discom #9

GIVEARM
END
