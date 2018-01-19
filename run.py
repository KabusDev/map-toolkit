import config

print("Map Toolkit \n")
# awful but will do for now


def error():
    print("unknown input\n")

while True:
    try:
        user_input = int(input("Press 1 to compile (exits script) \n"
                               "Press 2 to change config\n"
                               "Press 3 to reset config text\n"))
    except ValueError:
        error()
        user_input = 0
        continue
    else:
        if user_input == 2:
            print("Only input hierarchy for directory before steamapps, eg Z:/Steam/steamapps only put Z:/Steam/")
            config.user_steam_directory = input("Enter your base steamapps directory: ")
            config.user_meta_directory = input("Enter your metastruct directory if applicable: ")
            config.config_build()
        if user_input == 3:
            confirm = input("Are you sure you want to reset your gameinfo files? y/n")
            if confirm is "y":
                config.reset_config()
            elif confirm is "n":
                print("Returning,")
            else:
                error()
    finally:
        if user_input == 1:
            # todo implement
            quit()

