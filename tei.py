#!/usr/bin/env python3

"""TEI parser command line client.

For testing."""

import argparse
import sys

def testtei(tei:str, debug:bool):
    """Test a single TEI"""
    from lib.teiparse import valid

    print("Testing {}\n".format(tei))
    teivalid = valid(tei, debug)
    if not teivalid:
        print("ERROR: Invalid TEI: {}\n".format(tei))
        return False
    print("--- Congratulations! TEI is valid.")
    return True

def main():
    """Run the command line TEI parser."""
    debug = False

    parser = argparse.ArgumentParser(
        description='Tool for the TEI.',
        add_help=False)
    maincommands = parser.add_mutually_exclusive_group()
    maincommands.add_argument('--help', '-h',
                              action="store_true",
                              help='Get help with this command')
    parser.add_argument('-d', '--debug',
                        action="store_true",
                        help='Turn on debug output for developers')
    args = parser.parse_args()
    # Parse and set debug early
    if args.debug:
        debug = True
        print("DEBUG: Debugging enabled.")
    if args.help:
        parser.print_help()
        help_sign_commands(ca_config, debug)
        sys.exit(0)
    
    tei = "urn:tei:uuid:prod2.example.com:7bdb4424-612f-11ef-947e-1a52914d44b3"
    if not testtei(tei, debug):
        print("ERROR: Invalid TEI: {}\n".format(tei))

if __name__ == "__main__":
    main()