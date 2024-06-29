# Inject-EXE

## Overview

- The provided Python program, Inject-EXE.py, allows you to combine a malicious executable with a legitimate executable, producing a single output executable. This output executable will contain both the malicious and legitimate executables. This tool is designed to work on Windows systems and requires a Windows environment or Wine if you are using linux to build the executable.

## Features

- **Malicious EXE Embedded into Legit EXE:** Combines a malicious executable with a legitimate executable, embedding the malicious content within the legitimate wrapper.
- **Helps in Malware Development:** Facilitates the creation of combined executables for testing and development purposes in a controlled environment.
- **Bypass Antivirus Detection:** Conceals the malicious executable within a legitimate one, potentially helping to evade basic antivirus detection mechanisms.
- **Assists in Social Engineering:** Creates a seemingly legitimate executable that can be used in social engineering attacks to trick users into executing malicious code.
- **Executable Packaging:** Packages both the malicious and legitimate executables into a single output executable.

## How to Use

![Inject-EXE](https://github.com/malwarekid/Inject-EXE/assets/91931069/baaebb95-c22e-4642-8611-8ef0bce736af)


1. **Clone the Repository:**

    `git clone https://github.com/malwarekid/Inject-EXE.git && cd Inject-EXE`

2. **Run the Script:**

    `python Inject-EXE.py`

```
python3.exe Inject-EXE.py

    ____        _           __        _______  __ ______
   /  _/___    (_)__  _____/ /_      / ____/ |/ // ____/
   / // __ \  / / _ \/ ___/ __/_____/ __/  |   // __/
 _/ // / / / / /  __/ /__/ /_/_____/ /___ /   |/ /___
/___/_/ /_/_/ /\___/\___/\__/     /_____//_/|_/_____/
         /___/
                                      By @malwarekid

Enter your malicious executable: payload.exe
Enter your legit executable: calc.exe
Inject-EXE generated and save as: calc-output.exe
```

3. **Enter Input Parameters:**

   - **Malicious Executable:** Enter the path to your malicious executable.
   - **Legitimate Executable:** Enter the path to your legitimate executable.

4. **Output Executable:** The combined output executable will be saved in the current directory with the name based on the legitimate executable's name appended with `-output`.

## Requirements

- Python 3.x
- PyInstaller

## Installation

Ensure you have the required dependencies:

`python3.exe -m pip install pyinstaller`

## Example

`python3.exe Inject-EXE.py`


When prompted, enter the paths to your malicious and legitimate executables:

```
Enter your malicious executable: path/to/malicious.exe
Enter your legit executable: path/to/legit.exe
```
The script will generate a combined executable in the current directory.


## Contributors

- [MalwareKid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

Feel free to contribute, report issues, or provide feedback. Don't forget to follow me on [Instagram](https://www.instagram.com/malwarekid/) and [GitHub](https://github.com/malwarekid/). Happy Hacking!
