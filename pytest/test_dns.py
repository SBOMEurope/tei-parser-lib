"""Test the TEIparse DNS library"""


def test_dns_00(capsys, request):
    """Test basic DNS class."""
    from lib.teiparse.dnslookup import dnslookup

    name = "google.com"

    # Just initiate the object, do not query anything
    dnsres = dnslookup(name=name, debug=True)

    captured = capsys.readouterr()
    with capsys.disabled():
        print("DEBUG: DNS object: {}".format(dnsres))
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert dnsres.recordexist is False

def test_dns_01(capsys, request):
    """Test basic DNS class A lookup."""
    from lib.teiparse.dnslookup import dnslookup

    name = "google.com"

    # Just initiate the object, do not query anything
    dnsres = dnslookup(name=name, debug=True)
    dnsres.lookup_a(name=name)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("DEBUG: DNS object: {}".format(dnsres))
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert dnsres.recordexist is True

def test_dns_02(capsys, request):
    """Test basic DNS class AAAA lookup."""
    from lib.teiparse.dnslookup import dnslookup

    name = "google.com"

    # Just initiate the object, do not query anything
    dnsres = dnslookup(name=name, debug=True)
    dnsres.lookup_aaaa(name=name)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("DEBUG: DNS object: {}".format(dnsres))
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert dnsres.recordexist is True

def test_dns_03(capsys, request):
    """Test basic DNS class URI lookup."""
    from lib.teiparse.dnslookup import dnslookup

    name = "google.com"

    # Just initiate the object, do not query anything
    dnsres = dnslookup(name=name, debug=True)
    dnsres.lookup_uri(name=name)
    captured = capsys.readouterr()
    with capsys.disabled():
        print("DEBUG: DNS object: {}".format(dnsres))
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert dnsres.recordexist is False
