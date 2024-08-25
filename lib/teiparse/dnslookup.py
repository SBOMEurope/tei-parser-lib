"""The TEI - Transparency Exchange Identifier - parsing library
(C) Copyright Olle E. Johansson, Edvina AB - oej@edvina.net

The DNS support module

SPDX-License-Identifier: BSD
"""
from typing import Any


class dnslookup():
    """DNS lookup object."""

    debug = False
    name = None
    dnsobject: dict[Any, Any]
    dnsobject = dict()
    recordexist = False
    record_a = False
    record_aaaa = False
    record_uri = False

    def __init__(self, name, debug):
        """Initialise dnslookup object"""
        self.debug = debug
        self.dnsobject[name] = name

    def __str__(self):
        """Return a printable dnsobject."""
        import json
        printobj = dict(self.dnsobject)
        return json.dumps(printobj, sort_keys=False, indent=4)

    def lookup_a(self, name):
        """Check DNS for A record"""
        import dns.resolver
        try:
            # Resolve the A record (IPv4 address) for the domain
            result = dns.resolver.resolve(name, 'A')
            if self.debug:
                for ip in result:
                    print(f'DEBUG: {name} resolves to {ip.address}\n')
                self.recordexist = True
                self.record_a = True
        except dns.resolver.NoAnswer:
            if self.debug:
                print(f'DEBUG: No A record found for {name}\n')
        except dns.exception.DNSException as e:
            print(f'DNS lookup failed: {e}')
        return False

    def lookup_aaaa(self, name):
        """Check DNS for AAAA (IPv6) record"""
        import dns.resolver
        try:
            # Resolve the AAAA record (IPv6 address) for the domain
            result = dns.resolver.resolve(name, 'AAAA')
            if self.debug:
                for ip in result:
                    print(f'DEBUG: {name} resolves to {ip.address}\n')
            self.recordexist = True
            self.record_aaaa = True
        except dns.resolver.NoAnswer:
            if self.debug:
                print(f'DEBUG: No A record found for {name}\n')
            return False
        except dns.exception.DNSException as e:
            print(f'DNS lookup failed: {e}')
            return False
        return True

    def lookup_uri(self, name):
        """Lookup DNS URI record."""
        import dns.resolver
        try:
            answers = dns.resolver.resolve(
                name,
                "URI")
            self.recordexist = True
            self.record_uri = True
        except dns.resolver.NoAnswer:
            if self.debug:
                print("DEBUG: No answer on URI query for {}".format(name))
            return False
        except dns.exception.DNSException as e:
            print(f'DNS lookup failed: {e}')
            return False
        if self.debug:
            for rdata in answers:
                print(
                    "DEBUG: Host",
                    rdata.exchange,
                    "has preference",
                    rdata.preference, "\n")
        return True

    def lookup(self):
        """Query DNS for data.

        Start with URI records, then A/AAAA records.
        If not records found, we have a problem.
        """
        import dns.name
        import dns.resolver

        if self.name is None:
            return False, None

        n = dns.name.from_text(self.name)
        if self.debug:
            print("DEBUG: Name: {}\n".format(n.labels))
            # ['www', 'dnspython', 'org', '']
        import dns.resolver
        # Raises dns.resolver.LifetimeTimeout if no answers could be
        # found in the specified lifetime.

        # Raises dns.resolver.NXDOMAIN if the query name does not exist.

        # Raises dns.resolver.YXDOMAIN if the query name is too long
        # after DNAME substitution.

        # Raises dns.resolver.NoAnswer if raise_on_no_answer is True and
        # the query name exists but has no RRset of the desired type and class.

        # Raises dns.resolver.NoNameservers if no non-broken nameservers
        # are available to answer the question.

        # Returns a dns.resolver.Answer instance.
        if (self.lookup_uri(self.name)):
            return True
        self.lookup_a(self.name)
        self.lookup_aaaa(self.name)

        # If there are no URI records, find the canonical name
        # canonical_name(name: Name | str)→ Name
        if self.recordexist:
            if self.debug:
                print("DEBUG: Found a DNS entry for {}".format(self.name))
            return True
        return False
