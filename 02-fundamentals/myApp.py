import myModule

print("Svetlo uleti vzdalenost 50000km za: " + str(myModule.casSvetlo(50000, myModule.SPEED_OF_LIGHT)) + " s")

print("Zvuk uleti vzdalenost 6000km za: " + str(myModule.casSvetlo(6000, myModule.SPEED_OF_SOUND)) + " s")

print("Tihova sila Zeme na teleso o hmotnosti 50kg je: " + str(myModule.tihaZeme(50, myModule.EARTH_GRAVITY)) + " N")

print("Tihova sila  Mesice na teleso o hmotnosti 50kg je: " + str(myModule.tihaZeme(50, myModule.MOON_GRAVITY)) + " N")