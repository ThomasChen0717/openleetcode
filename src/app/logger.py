# logger.py

_verbose = False

def red(text):
    return f"\033[91m{text}\033[0m"

def green(text):  
    return f"\033[92m{text}\033[0m"

def set_verbose(verbose: bool):
    global _verbose
    _verbose = verbose

def log(message: str):
    if _verbose:
        print(message)

def logResults(results):
    #TODO: Print indivitual test status for a failed run?
    print("Status: " + str(results["status"]) + "\n" +
          "Duration: " + str(results["duration_ms"]) + "ms")