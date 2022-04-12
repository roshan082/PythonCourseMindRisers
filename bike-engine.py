# 
key = str
gear = str

key = input("""
1. Insert Key
2. No key
""")

if key == str(1):
    print("key inserted")
    gear = input("""
    Check Gear:
    1. Neutral
    2. 1st Gear
    3. 2nd Gear
    4. 3rd Gear
    5. 4th Gear
    6. 5th Gear
    """)
    if gear == str(1):
        engineStart = input("""
        Do you want to start the engine.
        1. engine start
        2. none
        """)
        if engineStart == str(1):
            print("Engine has started...")
        else:
            print("Engine has not started...")
    else:
        clutch = input("""
        Clutch:
        1. True
        2. False
        """)
        if clutch == str(1):
            engineStart = input("""
            Do you want to start the engine.
            1. engine start
            2. none
            """)
            if engineStart == str(1):
                print("Engine has started...")
            else:
                print("Engine has not started...")
        elif clutch == str(2):
            engineStart = input("""
            Do you want to start the engine.
            1. engine start
            2. none
            """)
            if engineStart == str(1):
                print("Clutch should be true to strat the engine.")
            else:
                print("Engine has not started...")
elif key == str(2):
    print("You can't start without key")
else:
    print("Invalid number")

