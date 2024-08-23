# A simple library to validate different TEI URI syntaxes

TEI is a Transparency Exchange Identifier. See
https://github.com/CycloneDX/transparency-exchange-api/tree/main/discovery
for details.

Created by Olle E. Johansson, Edvina AB, oej@edvina.net

## Testing with CLI client

```text
usage: tei.py [--help] [-d] [-t [TEI ...]]

Tool for the TEI.

optional arguments:
  --help, -h            Get help with this command
  -d, --debug           Turn on debug output for developers
  -t [TEI ...], --tei [TEI ...]
                        TEI URN to process
```

There are some examples of TEI URNs in the file example.txt

## References

- URNParse https://pypi.org/project/urnparse/
