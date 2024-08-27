"""Test PURL support"""
import pytest

def test_purl01(capsys, request):
    """Test PURL TEI."""
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from lib.teiparse import valid

    tei = "urn:tei:purl:prod.example.com:pkg:" \
        "alpm/arch/containers-common@1:0.47.4-4?arch=x86_64"

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is True

# Not valid according to PURL library
#  "urn:tei:purl:products.example.com:pkg:cpan/Perl::Version@1.013",
# DEBUG: Not a valid PURL: pkg:cpan/LWP::UserAgent
# ERROR: Invalid purl 'pkg:cpan/LWP::UserAgent' cannot contain a "user:pass@host:port" URL Authority component: ''.

@pytest.mark.parametrize("teipurl", [
    "urn:tei:purl:products.example.com:pkg:alpm/arch/pacman@6.0.1-1?arch=x86_64",
    "urn:tei:purl:products.example.com:pkg:alpm/arch/python-pip@21.0-1?arch=any",
    "urn:tei:purl:products.example.com:pkg:alpm/arch/containers-common@1:0.47.4-4?arch=x86_64",
    "urn:tei:purl:products.example.com:pkg:apk/alpine/curl@7.83.0-r0?arch=x86",
    "urn:tei:purl:products.example.com:pkg:apk/alpine/apk@2.12.9-r3?arch=x86",
    "urn:tei:purl:products.example.com:pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c",
    "urn:tei:purl:products.example.com:pkg:bitnami/wordpress?distro=debian-12",
    "urn:tei:purl:products.example.com:pkg:bitnami/wordpress@6.2.0?distro=debian-12",
    "urn:tei:purl:products.example.com:pkg:bitnami/wordpress@6.2.0?arch=arm64&distro=debian-12",
    "urn:tei:purl:products.example.com:pkg:bitnami/wordpress@6.2.0?arch=arm64&distro=photon-4",
    "urn:tei:purl:products.example.com:pkg:cocoapods/AFNetworking@4.0.1",
    "urn:tei:purl:products.example.com:pkg:cocoapods/MapsIndoors@3.24.0",
    "urn:tei:purl:products.example.com:pkg:cocoapods/ShareKit@2.0#Twitter",
    "urn:tei:purl:products.example.com:pkg:cocoapods/GoogleUtilities@7.5.2#NSData+zlib",
    "urn:tei:purl:products.example.com:pkg:cargo/rand@0.7.2",
    "urn:tei:purl:products.example.com:pkg:cargo/clap@2.33.0",
    "urn:tei:purl:products.example.com:pkg:cargo/structopt@0.3.11",
    "urn:tei:purl:products.example.com:pkg:composer/laravel/laravel@5.5.0",
    "urn:tei:purl:products.example.com:pkg:conan/openssl@3.0.3",
    "urn:tei:purl:products.example.com:pkg:conan/openssl.org/openssl@3.0.3?user=bincrafters&channel=stable",
    "urn:tei:purl:products.example.com:pkg:conan/openssl.org/openssl@3.0.3?arch=x86_64&build_type=Debug&compiler=Visual%20Studio&compiler.runtime=MDd&compiler.version=16&os=Windows&shared=True&rrev=93a82349c31917d2d674d22065c7a9ef9f380c8e&prev=b429db8a0e324114c25ec387bfd8281f330d7c5c",
    "urn:tei:purl:products.example.com:pkg:conda/absl-py@0.4.1?build=py36h06a4308_0&channel=main&subdir=linux-64&type=tar.bz2",
    "urn:tei:purl:products.example.com:pkg:cpan/DROLSKY/DateTime@1.55",
    "urn:tei:purl:products.example.com:pkg:cpan/DateTime@1.55",
    "urn:tei:purl:products.example.com:pkg:cpan/GDT/URI-PackageURL",
    "urn:tei:purl:products.example.com:pkg:cpan/OALDERS/libwww-perl@6.76",
    "urn:tei:purl:products.example.com:pkg:cpan/URI",
    "urn:tei:purl:products.example.com:pkg:cran/A3@1.0.0",
    "urn:tei:purl:products.example.com:pkg:cran/rJava@1.0-4",
    "urn:tei:purl:products.example.com:pkg:cran/caret@6.0-88",
    "urn:tei:purl:products.example.com:pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie",
    "urn:tei:purl:products.example.com:pkg:deb/debian/dpkg@1.19.0.4?arch=amd64&distro=stretch",
    "urn:tei:purl:products.example.com:pkg:deb/ubuntu/dpkg@1.19.0.4?arch=amd64",
    "urn:tei:purl:products.example.com:pkg:deb/debian/attr@1:2.4.47-2?arch=source",
    "urn:tei:purl:products.example.com:pkg:deb/debian/attr@1:2.4.47-2%2Bb1?arch=amd64",
    "urn:tei:purl:products.example.com:pkg:docker/cassandra@latest",
    "urn:tei:purl:products.example.com:pkg:docker/smartentry/debian@dc437cc87d10",
    "urn:tei:purl:products.example.com:pkg:docker/customer/dockerimage@sha256%3A244fd47e07d10?repository_url=gcr.io",
    "urn:tei:purl:products.example.com:pkg:gem/ruby-advisory-db-check@0.12.4",
    "urn:tei:purl:products.example.com:pkg:gem/jruby-launcher@1.1.2?platform=java",
    "urn:tei:purl:products.example.com:pkg:generic/openssl@1.1.10g",
    "urn:tei:purl:products.example.com:pkg:generic/openssl@1.1.10g?download_url=https://openssl.org/source/openssl-1.1.0g.tar.gz&checksum=sha256:de4d501267da",
    "urn:tei:purl:products.example.com:pkg:generic/bitwarderl?vcs_url=git%2Bhttps://git.fsfe.org/dxtr/bitwarderl%40cc55108da32",
    "urn:tei:purl:products.example.com:pkg:github/package-url/purl-spec@244fd47e07d1004",
    "urn:tei:purl:products.example.com:pkg:github/package-url/purl-spec@244fd47e07d1004#everybody/loves/dogs",
    "urn:tei:purl:products.example.com:pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c",
    "urn:tei:purl:products.example.com:pkg:golang/google.golang.org/genproto#googleapis/api/annotations",
    "urn:tei:purl:products.example.com:pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c#api",
    "urn:tei:purl:products.example.com:pkg:hackage/a50@0.5",
    "urn:tei:purl:products.example.com:pkg:hackage/AC-HalfInteger@1.2.1",
    "urn:tei:purl:products.example.com:pkg:hackage/3d-graphics-examples@0.0.0.2",
    "urn:tei:purl:products.example.com:pkg:hex/jason@1.1.2",
    "urn:tei:purl:products.example.com:pkg:hex/acme/foo@2.3.",
    "urn:tei:purl:products.example.com:pkg:hex/phoenix_html@2.13.3#priv/static/phoenix_html.js",
    "urn:tei:purl:products.example.com:pkg:hex/bar@1.2.3?repository_url=https://myrepo.example.com",
    "urn:tei:purl:products.example.com:pkg:huggingface/distilbert-base-uncased@043235d6088ecd3dd5fb5ca3592b6913fd516027",
    "urn:tei:purl:products.example.com:pkg:huggingface/microsoft/deberta-v3-base@559062ad13d311b87b2c455e67dcd5f1c8f65111?repository_url=https://hub-ci.huggingface.co",
    "urn:tei:purl:products.example.com:pkg:luarocks/luasocket@3.1.0-1",
    "urn:tei:purl:products.example.com:pkg:luarocks/hisham/luafilesystem@1.8.0-1",
    "urn:tei:purl:products.example.com:pkg:luarocks/username/packagename@0.1.0-1?repository_url=https://example.com/private_rocks_server/",
    "urn:tei:purl:products.example.com:pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1",
    "urn:tei:purl:products.example.com:pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=pom",
    "urn:tei:purl:products.example.com:pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?classifier=sources",
    "urn:tei:purl:products.example.com:pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=zip&classifier=dist",
    "urn:tei:purl:products.example.com:pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x86&type=dll",
    "urn:tei:purl:products.example.com:pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x64&type=dll",
    "urn:tei:purl:products.example.com:pkg:mlflow/creditfraud@3?repository_url=https://westus2.api.azureml.ms/mlflow/v1.0/subscriptions/a50f2011-fab8-4164-af23-c62881ef8c95/resourceGroups/TestResourceGroup/providers/Microsoft.MachineLearningServices/workspaces/TestWorkspace",
    "urn:tei:purl:products.example.com:pkg:mlflow/trafficsigns@10?model_uuid=36233173b22f4c89b451f1228d700d49&run_id=410a3121-2709-4f88-98dd-dba0ef056b0a&repository_url=https://adb-5245952564735461.0.azuredatabricks.net/api/2.0/mlflow",
    "urn:tei:purl:products.example.com:pkg:npm/foobar@12.3.1",
    "urn:tei:purl:products.example.com:pkg:npm/%40angular/animation@12.3.1",
    "urn:tei:purl:products.example.com:pkg:npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git%404345abcd34343",
    "urn:tei:purl:products.example.com:pkg:nuget/EnterpriseLibrary.Common@6.0.1304",
    "urn:tei:purl:products.example.com:pkg:qpkg/blackberry/com.qnx.sdp@7.0.0.SGA201702151847",
    "urn:tei:purl:products.example.com:pkg:qpkg/blackberry/com.qnx.qnx710.foo.bar.qux@0.0.4.01449T202205040833L",
    "urn:tei:purl:products.example.com:pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=docker.io/library/debian&arch=amd64&tag=latest",
    "urn:tei:purl:products.example.com:pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=ghcr.io/debian&tag=bullseye",
    "urn:tei:purl:products.example.com:pkg:oci/static@sha256%3A244fd47e07d10?repository_url=gcr.io/distroless/static&tag=latest",
    "urn:tei:purl:products.example.com:pkg:oci/hello-wasm@sha256%3A244fd47e07d10?tag=v1",
    "urn:tei:purl:products.example.com:pkg:pub/characters@1.2.0",
    "urn:tei:purl:products.example.com:pkg:pub/flutter@0.0.0",
    "urn:tei:purl:products.example.com:pkg:pypi/django@1.11.1",
    "urn:tei:purl:products.example.com:pkg:pypi/django-allauth@12.23",
    "urn:tei:purl:products.example.com:pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25",
    "urn:tei:purl:products.example.com:pkg:rpm/centerim@4.22.10-1.el6?arch=i686&epoch=1&distro=fedora-25",
    "urn:tei:purl:products.example.com:pkg:swid/Acme/example.com/Enterprise+Server@1.0.0?tag_id=75b8c285-fa7b-485b-b199-4745e3004d0d",
    "urn:tei:purl:products.example.com:pkg:swid/Fedora@29?tag_id=org.fedoraproject.Fedora-29",
    "urn:tei:purl:products.example.com:pkg:swid/Adobe+Systems+Incorporated/Adobe+InDesign@CC?tag_id=CreativeCloud-CS6-Win-GM-MUL",
    "urn:tei:purl:products.example.com:pkg:swift/github.com/Alamofire/Alamofire@5.4.3",
    "urn:tei:purl:products.example.com:pkg:swift/github.com/RxSwiftCommunity/RxFlow@2.12.4"
    ])
def test_all_purls(capsys, request, teipurl):
    """Test PURL TEI of all types."""
    from lib.teiparse import valid
    import re

    tei = teipurl

    tvalid = valid(tei, True)
    captured = capsys.readouterr()
    with capsys.disabled():
        print(
            "\nDEBUG {}: output: \n{}\n"
            .format(request.node.name, captured.out))
    assert tvalid is True
    assert re.search(
        "DEBUG: Valid PURL",
        captured.out
    ) is not None
