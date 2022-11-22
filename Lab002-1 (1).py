def falling_distance():
    t= int(input())
    gravity = 9.8
    distance = (1/2)*gravity*(t**2)
    print("Falling Distance for an object that been falling for", t, "seconds is", distance,"meters")

falling_distance()
