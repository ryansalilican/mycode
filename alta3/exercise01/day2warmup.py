    #!/usr/bin/env python3
    import time
    heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]
    choice= input("Pick your favorite character from this list!\n -" + heroes[0] + "\n -" + heroes[1] + "\n -" + heroes[2] + "\n -" + heroes[3] + "\n -" + heroes[4] + "\n>")
    time.sleep(3)
    print("You picked " + choice + "! Great decision.")
    time.sleep(3)
    num= input("Pick a number between 1-100\n>")
    time.sleep(3)
    print("You picked " + num + ".")


    nums= [1, -5, 56, 987, 0]
    print(max(nums))

