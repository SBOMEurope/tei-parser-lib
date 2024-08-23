"""The TEI - Transparency Exchange Identifier - parsing library
(C) Copyright Olle E. Johansson, Edvina AB - oej@edvina.net
"""


def valid(
        tei: str,
        debug: bool
        ):
    """Parse a TEI.

    Return FALSE if it's not a valid syntax."""
    from urnparse import URN8141, InvalidURNFormatError

    try:
        urn = URN8141.from_string(tei)
    except InvalidURNFormatError:
        if debug:
            print("DEBUG: Invalid format (InvalidURNFormatError)\n")
        return False
    except AttributeError:
        if debug:
            print("DEBUG: Invalid format (attribute error)\n")
        return False
    if debug:
        print("DEBUG: Got this URN: {}\n".format(tei))
        print("- Namespace ID {}\n".format(urn.namespace_id))
        print("- specific parts: {}\n".format(urn.specific_string.parts))
        print("- Query part: {}\n".format(urn.rqf_component.query))
    return True
