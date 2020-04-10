def INFO(text):
    return "[INFO] " + text

def WARNING(text):
    raise Warning("[WARN] ", text)

def ERROR(text):
    raise Exception("[ERROR] ", text)

def FATAL(text):
    raise Exception("[FATAL] ", text)

def SUCCESS(*args):
    pass

def __init__():
    INFO("Logger imported successfully!")