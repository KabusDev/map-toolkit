import config

print("Map Toolkit \n")
# awful but will do for now

while True:
    try:
        user_input = int(input("press 1 to compile(exits script), 2 to change config: "))
    except ValueError:
        print("invalid input \n")
        user_input = 0
        continue
    else:

        if user_input == 2:
            print("Only input hierarchy for directory before steamapps, eg Z:/Steam/steamapps only put Z:/Steam/")
            config.user_steam_directory = input("Enter your base steamapps directory: ")
            config.config_build()
    finally:
        if user_input == 1:
            #todo implement
            quit()

