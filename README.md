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

## TEI types

The following TEI types are supported:

### TEI UUID

Syntax:

```text
urn:tei:uuid:<domain or host>:<uuid>
````

Has to be a valid UUID

### TEI PURL

Syntax:

```text
urn:tei:uuid:<domain or host>:<purl>
````

### TEI SWID

Syntax:

```text
urn:tei:swid:<domain or host>:<swid>
````

Note that there is a TEI SWID type as well as a PURL SWID type. 

### TEI HASH

Supports the following hash values:

* SHA256
* SHA384
* SHA512

```text
urn:tei:hash:<domain or host>:<hashtype>:<hash>
````

## References

- URNParse https://pypi.org/project/urnparse/
