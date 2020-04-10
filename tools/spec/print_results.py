def INFO(*args):
    return "[INFO] " + args

def WARNING(*args):
    print("\033[1;33;40m [WARN]  {} \n".format(*args))
    # raise Warning("[WARN] ", text)

def ERROR(*args):
    print("\033[1;31;40m [FATAL]  {} \n".format(*args))
    # raise Exception("[ERROR] ", text)

def FATAL(*args):
    print("\033[1;31;40m [FATAL]  {} \n".format(*args))
    # raise Exception("[FATAL] ", text)

def SUCCESS(*args):
    print("\033[1;32;40m [SUCCESS]  {} \n".format(*args))

def __init__():
    SUCCESS("Logger imported successfully!")