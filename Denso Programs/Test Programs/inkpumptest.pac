'!TITLE "Ink Pump Test"
PROGRAM InkPumpTest
TAKEARM 0 keep=0
SPEED 20

'Establish connection to the Pi
com_discom #9

DEFINT flg
com_state #9,flg
IF flg=-1 THEN
  com_encom #9
  'MOVE P, @0 J0 'Starting position
  DELAY 1000
ENDIF

'Turn on the pump
FLUSH #9
S10 = "pumpOn"
PRINT #9,S10
DELAY 100000

'Turn off the pump
S10 = "pumpOff"
PRINT #9,S10

DELAY 1000

S10 = "END"
PRINT #9,S10
com_discom #9
GIVEARM
END
