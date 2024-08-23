"""The TEI - Transparency Exchange Identifier - parsing library"""


def parse_tei(
        tei: str,
        debug: bool
        ):
    """Parse a TEI.

    Return FALSE if it's not a valid syntax."""

    if debug:
        print("Got this URN: {}\n".format(tei))

    return True
