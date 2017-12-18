import os, urllib.request
user_steam_directory = ""


def config_build():
    old_dir = "__INSTALL_DRIVE__"
    new_dir = user_steam_directory
    filename = "game_compile/gameinfo.txt"
    # use with to check if dir is not original
    with open(filename) as file:
        build = file.read()
        if old_dir not in build:
            print('"{old_dir}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as file:
        print('Changing "{old_dir}" -> "{new_dir}" in {filename}'.format(**locals()))
        build = build.replace(old_dir, new_dir)
        file.write(build)

def reset_config():
    dl = urllib.request.URLopener()
    dl.retrieve("https://raw.githubusercontent.com/KabusIblis/map-toolkit/master/game_compile/gameinfo.txt",
                "game_compile/gameinfo.txt") # shoddy but should work
    pass
