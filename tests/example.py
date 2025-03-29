import sys
sys.path.append('/home/vallereichi/vallog/')

import vallog as vl
from vallog.Logger import Logger
    
def main():
    debug = Logger("Debug")
    release = Logger("Release")

    print("\n\n============================================================================================================\n")

    print("DEBUG MODE: all massages are printed")

    debug.log("Default massage",    vl.default)
    debug.log("Info massage",       vl.info)
    debug.log("Warning massage",    vl.warning)
    debug.log("Error massage",      vl.error)
    debug.log("Debug massage",      vl.debug)

    print("\n\nRELEASE MODE: debug messages dont get printed")

    release.log("Default massage",    vl.default)
    release.log("Info massage",       vl.info)
    release.log("Warning massage",    vl.warning)
    release.log("Error massage",      vl.error)
    release.log("Debug massage",      vl.debug)  

    print("\nCUSTOM LABELS")

    debug.log("custom massage", "CUSTOM")
    release.log("custom massage", "CUSTOM") 

    print("\nLONG TEXT gets wrapped around like this")
    debug.log("this is some really long text. But at the end of the line (depending on the terminal width) it gets wrapped around and has the same indentation as the start of this massage. The Linebreak should also not break words apart but instead break at the end of a word")
    
        




if __name__ == "__main__":
    main()