# From https://github.com/firebolt-space/canary/blob/master/src/external/common/log_states.py
def INFO(*args):
    print("[INFO] {}".format(*args))

def WARNING(*args):
    print("\033[1;33;40m[WARN] {}".format(*args))
    # raise Warning("[WARN] ", text)

def ERROR(*args):
    print("\033[1;31;40m[FATAL] {}".format(*args))
    # raise Exception("[ERROR] ", text)

def FATAL(*args):
    print("\033[1;31;40m[FATAL] {}".format(*args))
    # raise Exception("[FATAL] ", text)

def SUCCESS(*args):
    print("\033[1;32;40m[SUCCESS] {}".format(*args))

def __init__():
    SUCCESS("Test prettier imported successfully!\n")

# From https://github.com/firebolt-space/canary/blob/master/src/external/common/log_states.py