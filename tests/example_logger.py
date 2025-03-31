"""
example file on how to use the vallog Logger module
"""

import sys

sys.path.append("/home/vallereichi/vallog/")

import vallog as vl
from vallog.logger import Logger


def main():
    """all functionalities of the logger module are listed here. execute to see the corresponding output"""
    debug = Logger("Debug")
    release = Logger("Release")

    debug.sep("*")
    debug.sep("0")

    debug.heading("this is a heading")
    debug.log(
        "same as heading with more customization in the future",
        vl.header,
        display_category=True,
        colored_text=False,
    )

    release.sep("*")
    release.sep()

    debug.heading("DEBUG MODE: everything gets printed")

    debug.log("Default massage", vl.default)
    debug.log("Info massage", vl.info)
    debug.log("Warning massage", vl.warning)
    debug.log("Error massage", vl.error)
    debug.log("Debug massage", vl.debug)

    release.heading("RELEASE MODE: debug messages dont get printed")

    release.log("Default massage", vl.default)
    release.log("Info massage", vl.info)
    release.log("Warning massage", vl.warning)
    release.log("Error massage", vl.error)
    release.log("Debug massage", vl.debug)

    debug.heading("CUSTOM LABELS")

    debug.log("custom massage", "CUSTOM")
    release.log("custom massage", "CUSTOM")

    debug.heading("LONG TEXT gets wrapped around like this")
    debug.log(
        "this is some really long text. But at the end of the line (depending on the terminal width) it gets wrapped around and has the same indentation as the start of this massage. The Linebreak should also not break words apart but instead break at the end of a word. And of course this should also work for multiple line breaks and completely independant of the terminal size",
        vl.info,
    )

    release.sep()


if __name__ == "__main__":
    main()
