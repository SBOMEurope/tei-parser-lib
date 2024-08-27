"""The TEI - Transparency Exchange Identifier - parsing library
(C) Copyright Olle E. Johansson, Edvina AB - oej@edvina.net

SPDX-License-Identifier: BSD
"""


def check_tei_type(type: str, debug: bool):
    """Check for a supported TEI type."""
    ttype = [
        "purl",
        "uuid",
        "hash",
        "swid"
    ]
    if type in ttype:
        return True
    if debug:
        print("DEBUG: TEI type not supported: {}".format(type))
    return False

def valid_hash(hashtype: str, teihash: str, debug: bool):
    """Check if the TEI hash URN is valid.

    Sample syntax:
    urn:tei:hash:teapot.example.com:sha256:00480065006C006C006F00200077006F0072006C00640021

    the hash value needs to be in hex code
    """
    htype = [
        "sha256",
        "sha384",
        "sha512"
    ]
    if hashtype not in htype:
        if debug:
            print("DEBUG: Invalid hash type: {}\n".format(hashtype))
        return True
    try:
        val = int(teihash, 16)
    except ValueError:
        if debug:
            print("DEBUG: Hash is not a hex value: {}\n".format(teihash))
        return False
    if debug:
        print("DEBUG: Valid TEI hash {}: {}".format(hashtype, teihash))
    return True


def valid_purl(purl: str, debug: bool):
    """Check if the PURL is valid.
    Specification: https://github.com/package-url/purl-spec

    Sample syntax:
    urn:tei:purl:prod.example.com:pkg:alpm/arch/containers-common@1:0.47.4-4?arch=x86_64

    we need to remove the four first parts separated by :
    and get the rest, including colons

    Using https://github.com/package-url/packageurl-python
    """
    from packageurl import PackageURL
    if debug:
        print("DEBUG: Checking PURL: {}\n".format(purl))
    try:
        purlobj = PackageURL.from_string(purl)
    except ValueError as err:
        if debug:
            print("DEBUG: Not a valid PURL: {}".format(purl))
            print("ERROR: {}".format(err))
        return False
    if debug:
        print("DEBUG: Valid PURL {}\n".format(repr(purlobj)))
    return True


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
    if urn.namespace_id != "tei":
        if debug:
            print(
                "DEBUG: Invalid URN namespace ({})\n"
                .format(urn.namespace_id))
        return False
    if not check_tei_type(urn.specific_string.parts[0], debug):
        return False
    # Check the length of the domain part
    domlen = len(urn.specific_string.parts[1])
    if domlen == 0:
        if debug:
            print("ERROR: No domain part given.")
            return False
    if urn.specific_string.parts[0] == "purl":
        if debug:
            print("DEBUG: Checking PURL syntax")
        # Calculate where PURL begins
        start = len("urn:tei:purl:")
        #remove the domain
        start += domlen + 1
        if not valid_purl(tei[start:], debug):
            return False
        return True
    if urn.specific_string.parts[0] == "hash":
        # Hash type tei:hash:<domain>:hashtype:<hash>
        hashtype = urn.specific_string.parts[2]
        if not valid_hash(
            hashtype=hashtype,
            teihash = urn.specific_string.parts[3],
            debug = debug):
            return False
        return True

    return True
