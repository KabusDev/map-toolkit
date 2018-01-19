import os, urllib.request

# empty strings for initial run
# todo save base directory and modified directory so that it can be reset without download.
user_steam_directory = ""
user_meta_directory = ""


def config_build():
    old_steam_dir = "__INSTALL_DRIVE__"
    new_steam_dir = user_steam_directory
    old_meta_dir = "__META_FILE_DRIVE__"
    new_meta_dir = user_meta_directory

    filename = "game_compile/gameinfo.txt"

    # use with to check if dir is not original
    with open(filename) as file:
        build = file.read()
        if old_steam_dir not in build:
            print('"{old_steam_dir}" not found in {filename}.'.format(**locals()))
            check = input("Woukd you like to reset your config to base settings? Y/N")
            if check is "y":
                print("Resetting path.")
                reset_config()
            elif check is "n":
                pass
            else:
                print("Input unknown.")
                return
            return
        if old_meta_dir not in build:
            print('"{old_meta_dir}" not found in {filename}.'.format(**locals()))
            check = input("Woukd you like to reset your config to base settings? Y/N")
            if check is "y":
                print("Resetting path.")
                reset_config()
            elif check is "n":
                pass
            else:
                print("Input unknown.")
                return
            return
    # Safely write the changed content, if found in the file
    with open(filename, 'w') as file:
        print('Changing "{old_steam_dir}" -> "{new_steam_dir}" in {filename}'.format(**locals()))
        build = build.replace(old_steam_dir, new_steam_dir)
        print('Changing "{old_meta_dir}" -> "{new_meta_dir}" in {filename}'.format(**locals()))
        build = build.replace(old_meta_dir, new_meta_dir)
        file.write(build)


def reset_config():
    dl = urllib.request.URLopener()
    print("Downloading gameinfo.text")
    dl.retrieve("https://raw.githubusercontent.com/KabusIblis/map-toolkit/master/game_compile/gameinfo.txt",
                "game_compile/gameinfo.txt") # shoddy but should work
    print("Finished reset on config gameinfo.text")
    pass
