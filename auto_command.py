"""
Automatic command runner.
"""

# Built-in modules
import getpass
from time import sleep

# Downloadable modules
import netmiko


def execute_commands(device_settings: dict, commands: list, wait_time: int):
    """
    Runs each command in the provided list, on the provided device, in each provided time interval.
    """
    connection = netmiko.ConnectHandler(**device_settings)
    try:
        print("Stop the loop with Ctrl-C")
        while True:
            print("\n")
            for command in commands: # TODO: check for errors
                results = connection.send_command(command)
                if results != "":
                    print(results)
                else:
                    #print(f"!-ERROR-! There was no output for `{command}`")
                    pass
            sleep(wait_time)
    except KeyboardInterrupt:
        connection.disconnect()
        print("\n---- CONNECTION CLOSED ----")


def collect_commands():
    """
    Collects a multi-line input from the user.

    User exits input with Ctrl-C or Ctrl-Z.
    """
    getting_commands = True
    while getting_commands == True:
        print("\nEnter/Paste your commands. Ctrl-C or Ctrl-Z to finish.")
        print("---------------------------------------------\n")
        commands = []
        try:
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                commands.append(line)
        except KeyboardInterrupt:
            pass
        print("\n---------------------------------------------\n")

        # Verify these are the correct commands
        answer = are_you_sure("Are you sure these are the commands you want to run?")
        if answer == True:
            break
        else:
            print("Ok, try again...\n")
    return commands


def are_you_sure(question: str):
    """
    Loop while asking a Y/N question.
    
    Adds str(" (Y/N):  ") to the end of the provided question.
    """
    while True:
        answer = str(input(question + " (Y/N):  ")).lower()
        if answer.startswith("y"):
            result = True
            break
        elif answer.startswith("n"):
            result = False
            break
        else:
            pass
    return result


def main():
    # Ask for ip address to connect to # TODO: Validate input and ask again if it's not an IP address
    client_address = input("Device IP address:  ")

    # Ask for credentials
    username = input("Username:  ")
    password = getpass.getpass(prompt="Password:  ", stream=None)
    
    # Ask for how long to wait # TODO: Validate input, set default value if none is set
    wait_time = int(input("Run the commands every X seconds:  "))

    # connect to device and run commands, print stdout
    device_settings = {
        #'device_type': 'paloalto_panos_ssh',
        'device_type': 'cisco_ios_ssh',
        'ip': client_address,
        'username': username,
        'password': password,
        'global_delay_factor': 2,
        'timeout': 30,
    }

    # Ask for and run the commands and wait after each set
    more_commands = True
    while more_commands == True:
        commands = collect_commands()
        execute_commands(device_settings=device_settings, commands=commands, wait_time=wait_time)

        # Check if the user want to run a new set of commands without filling out all the previous information again
        answer = are_you_sure("\n\nWould you like to run new commands?")
        if answer == True:
            pass
        else:
            break

    input("\n\nPress ENTER to close window.")


if __name__ == '__main__':
    main()