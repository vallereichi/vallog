"""
example file on how to use the vallog Logger module
"""

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

    debug.heading("CUSTOM CATEGORIES")
    debug.add_category("USR_CAT", "red", ["Debug", "Release"])
    debug.log(
        "This is how the user can add new categories. Note that new categories are limited to a Logger instance",
        debug.USR_CAT,
    )
    new_cat = vl.Logger.LogCategory("NEW_CAT", "yellow")
    debug.log("custom categories can also be created like this. But you may loose some functionalities", new_cat)
    debug.log("And of course there is also coloured massages", new_cat, colored_text=True)

    debug.list_categories()

    release.sep()

    debug.heading("Supress all output to the Terminal with 'cout = False'")
    test = vl.Logger("Test", cout=True)
    test.log(
        "this Test mode will only display Warnings, Errors and Default messages so that annoying infos dont get printed in large test runs",
        vl.warning,
    )
    test.log("Here is some text that wont get printed", vl.info)
    test.toggle_cout()
    test.log("Now that cout is turned off nothing will get printed to the terminal", vl.error)
    test.sep("?")
    test.toggle_cout()
    test.sep()


if __name__ == "__main__":
    main()
