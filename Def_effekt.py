def beregn_I():
    global I
    print("Indtast effektforbrug på brugsgenstanden")
    P = int(input())        # Indtast effektforbruget
    U = 230                 # Spændingen er på 230V
    I = P/U                 # Beregner strømmen
    print(str(I)+" A")      # skriver amperer

print("skal der benyttes 70c kabel(tast 0) 90c kable (tast 1)")
taller=int(input())
               #Taller bruges til checke om programmet skal stoppe(1) eller forsætte(0)
while taller == 0:
    beregn_I()
    if I < 13:              # er strømmen mindre end 13 A
        print('1,5 mm2')
    elif I >= 13 and I <= 25:# er strømmen større end 13 og mindre end 25
        print('2,5 mm2')
    elif I >=26 and I<= 34:
        print("4 mm2")
    else:
        print('For stor effekt til denne beregning')
    print("70c tast 0, tast 1 for 90c og 3 for stop ")
    taller=int(input())


while taller == 1:
    beregn_I()
    if I < 18:              # er strømmen mindre end 13 A
        print('1,5 mm2')
    elif I >= 18 and I <= 25:# er strømmen større end 13 og mindre end 25
        print('2,5 mm2')
    elif I >=26 and I< 40:
        print("4 mm2")
    else:
        print('For stor effekt til denne beregning')
    print("70c tast 0, tast 1 for 90c og 3 for stop ")
    taller=int(input())
