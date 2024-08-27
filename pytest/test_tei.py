"""Test the TEIparse library"""


def test_uuid(capsys, request):
    """Test UUID TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "urn:tei:uuid:prod2.example.com:7bdb4424-612f-11ef-947e-1a52914d44b3"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is True


def test_swid(capsys, request):
    """Test SWID TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "urn:tei:swid:prod2.example.com:Acme/example.com/" \
        "Enterprise+Server@1.0.0?tag_id=75b8c285-fa7b-485b-b199-4745e3004d0d"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is True


def test_bad_00(capsys, request):
    """Test bad TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "https://prod2.example.com/7bdb4424-612f-11ef-947e-1a52914d44b3"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is False


def test_bad_01(capsys, request):
    """Test bad TEI. URN type ISDN"""
    import os
    import sys
    import re
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "urn:isbn:0-486-27557-4"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is False
    assert re.search(
        "DEBUG: Invalid URN namespace",
        captured.out) is not None


def test_bad_02(capsys, request):
    """Test bad TEI with bare URL."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "https://google.com"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is False


def test_bad_03(capsys, request):
    """Test bad TEI with bad type"""
    import os
    import sys
    import re
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "urn:tei:gurka:prod2.example.com:" \
        "7bdb4424-612f-11ef-947e-1a52914d44b3"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is False
    assert re.search(
        "DEBUG: TEI type not supported",
        captured.out) is not None
