"""Test the TEIparse library"""

def test_uuid(capsys, request):
    """Test UUID TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei="urn:tei:uuid:prod2.example.com:7bdb4424-612f-11ef-947e-1a52914d44b3"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("\nDEBUG {}: output: \n{}\n"
                .format(request.node.name, captured.out))
    assert tvalid is True

def test_purl01(capsys, request):
    """Test PURL TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei="urn:tei:purl:prod.example.com:pkg:alpm/arch/containers-common@1:0.47.4-4?arch=x86_64"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("\nDEBUG {}: output: \n{}\n"
                .format(request.node.name, captured.out))
    assert tvalid is True

def test_bad(capsys, request):
    """Test bad TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei="https://prod2.example.com/7bdb4424-612f-11ef-947e-1a52914d44b3"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("\nDEBUG {}: output: \n{}\n"
                .format(request.node.name, captured.out))
    assert tvalid is False

def test_bad_02(capsys, request):
    """Test bad TEI with bare URL."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei="https://google.com"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("\nDEBUG {}: output: \n{}\n"
                .format(request.node.name, captured.out))
    assert tvalid is False