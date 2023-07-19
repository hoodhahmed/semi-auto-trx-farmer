import os
import time
import json
import exception


# A flag to indicate whether or not debug mode is enabled
IS_DEBUG = True

# The current working directory
PATH = os.path.dirname(os.path.realpath(__file__))


def debug_print(*args):
    """
    A function to print debug messages

    Args:
        *args: The arguments to print
    """

    # Check if debug mode is enabled
    if not IS_DEBUG:
        return

    # Check if the debug path exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Print and log debug messages
    now = time.strftime("%H:%M:%S")
    print(f"{now} [DEBUG] " + " ".join(args),
          file=open(f"{PATH}/logs/debug.log", "a", encoding='utf-8'))

def check_and_create_path(path=None, file_name=None):
    """
    Function to check if a path exists and create it if it doesn't exist.

    Args:
        path: The path to check and create.
        file_name: The file name.

    Returns:
        True if the path exists, False otherwise.
    """

    if not path and not file_name:
        raise ValueError("Please specify a path or a file name.")

    path = path if path else file_name

    path_parts = path.split("/")
    directory = os.path.join(*path_parts[:-1])

    if os.path.exists(path):
        return True

    if directory and not os.path.exists(directory):
        debug_print(f"Creating the {directory} directory")
        os.makedirs(directory)
        debug_print(f"Created the {directory} directory")

    if file_name:
        with open(f"{file_name}", "w", encoding="utf-8") as f:
            f.write("{}")

        return True
    else:
        return False



def load_json(file_path):
    """
    Function to load a json file. from a path.
    create it if it doesn't exist.
    Params:
        file_path: The path to the json file.
    Returns:
        The json object.
    """

    # file path ends with .json
    if not file_path.endswith(".json"):
        raise exception.NotJsonError(file_path)
        
    else:
        try:
            return json.load(open(file_path, "r", encoding='utf-8'))
        except json.JSONDecodeError as _e:
            raise exception.NotJsonError(file_path) from _e

def dump_json(file_path, json_object):
    """
    Function to dump a json object to a json file.
    Params:
        file_path: The path to the json file.
        json_object: The json object to dump.
    """

    # file path ends with .json
    if not file_path.endswith(".json"):
        raise exception.NotJsonError(file_path)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
        
    else:
        try:
            json.dump(json_object, open(file_path, "w", encoding='utf-8'), indent=4, sort_keys=True)
        except json.JSONDecodeError as _e:
            raise exception.NotJsonError(file_path) from _e

# Create the `secrets` directory if it doesn't exist
if check_and_create_path(file_name="secrets/secrets.json"):
    # create the secrets.json file
    debug_print("Creating the `secrets.json` file")
    secrets = load_json("secrets.json")
    secrets = {
        "cwallet_auth_token": "REPLACE_ME_WITH_AUTH_TOKEN_OF_CWALLET",
        "ci_session_browser": "REPLACE_ME_WITH_CI_SESSION_OF_BROWSER",
        "tron_wallet_private_key": "REPLACE_ME_WITH_PRIVATE_KEY_OF_TRON_WALLET"
    }
    dump_json("secrets/secrets.json", secrets)



if __name__ == "__main__":
    # Start the program
    debug_print("Starting the program")
