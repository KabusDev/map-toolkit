stop = True


def config_build():
    old_dir = "__INSTALL_DRIVE__"
    new_dir = user_steam_directory
    filename = "game_compile/gameinfo.txt"
    # use with to check if dir is not original
    with open(filename) as file:
        build = file.read()
        if old_dir not in build:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as file:
        print('Changing "{old_string}" -> "{user_steam_directory}" in {filename}'.format(**locals()))
        build = build.replace(old_dir, new_dir)
        file.write(build)

# this is very basic and bad and will change later
while stop is True:
    print("Only input hierarchy for directory before steamapps, eg Z:/Steam/steamapps only put Z:/Steam/")
    user_steam_directory = input("Enter your base steamapps directory: ")
    config_build()
