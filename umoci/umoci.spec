%if 0%{?fedora}
%global with_devel 1
%global with_bundled 1
%global with_debug 1
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 1
%global with_bundled 1
%global with_debug 1
%global with_check 1
%global with_unit_test 1
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -tags="$BUILDTAGS rpm_crashtraceback" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

%global provider        github
%global provider_tld    com
%global project         openSUSE
%global repo            umoci
# https://github.com/openSUSE/umoci
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          a47bc3caf6bb1ade3a4453d58212239386d345c0
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           %{repo}
Version:        0.4.3
Release:        0.2%{?dist}
Summary:        umoci modifies Open Container images
License:        ASL 2.0
URL:            https://umo.ci/
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le s390x %{mips}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  go-md2man

%if ! 0%{?with_bundled}
BuildRequires:  golang(github.com/apex/log)
BuildRequires:  golang(github.com/apex/log/handlers/cli)
BuildRequires:  golang(github.com/cyphar/filepath-securejoin)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/runtime-tools/generate)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/rootless-containers/proto/go-proto)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(github.com/vbatts/go-mtree)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/sys/unix)
%endif

%description
umoci modifies Open Container images.

umoci is a manipulation tool for OCI images. In particular, it is an
alternative to oci-image-tools provided by the OCI.

%if 0%{?with_devel}
%package devel
Summary:        umoci Source Libraries
BuildArch:      noarch

%if 0%{?with_check}
%if ! 0%{?with_bundled}
BuildRequires:  golang(github.com/apex/log)
BuildRequires:  golang(github.com/apex/log/handlers/cli)
BuildRequires:  golang(github.com/cyphar/filepath-securejoin)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/klauspost/pgzip)
BuildRequires:  golang(github.com/mohae/deepcopy)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/runtime-tools/generate)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/rootless-containers/proto/go-proto)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(github.com/vbatts/go-mtree)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/sys/unix)
%endif
%endif

%if ! 0%{?with_bundled}
Requires:       golang(github.com/apex/log)
Requires:       golang(github.com/apex/log/handlers/cli)
Requires:       golang(github.com/cyphar/filepath-securejoin)
Requires:       golang(github.com/docker/go-units)
Requires:       golang(github.com/golang/protobuf/proto)
Requires:       golang(github.com/opencontainers/go-digest)
Requires:       golang(github.com/opencontainers/image-spec/specs-go)
Requires:       golang(github.com/opencontainers/image-spec/specs-go/v1)
Requires:       golang(github.com/opencontainers/runtime-spec/specs-go)
Requires:       golang(github.com/opencontainers/runtime-tools/generate)
Requires:       golang(github.com/pkg/errors)
Requires:       golang(github.com/rootless-containers/proto/go-proto)
Requires:       golang(github.com/urfave/cli)
Requires:       golang(github.com/vbatts/go-mtree)
Requires:       golang(golang.org/x/net/context)
Requires:       golang(golang.org/x/sys/unix)
%endif

Provides:       golang(%{import_path}/mutate) = %{version}-%{release}
Provides:       golang(%{import_path}/oci/cas) = %{version}-%{release}
Provides:       golang(%{import_path}/oci/cas/dir) = %{version}-%{release}
Provides:       golang(%{import_path}/oci/casext) = %{version}-%{release}
Provides:       golang(%{import_path}/oci/config/convert) = %{version}-%{release}
Provides:       golang(%{import_path}/oci/config/generate) = %{version}-%{release}
Provides:       golang(%{import_path}/oci/layer) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/fseval) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/idtools) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/mtreefilter) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/rootlesscontainers-proto) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/system) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/unpriv) = %{version}-%{release}
Provides:       golang(%{import_path}/third_party/shared) = %{version}-%{release}
Provides:       golang(%{import_path}/third_party/user) = %{version}-%{release}

%if 0%{?with_bundled}
# version information manually retrieved from modules.txt
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/apex/log)) = v1.1.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/apex/log/handlers/cli)) = v1.1.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/blang/semver)) = v3.5.1
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/cyphar/filepath-securejoin)) = v0.2.2
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/docker/go-units)) = v0.3.3
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/fatih/color)) = v1.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/golang/protobuf/proto)) = v1.2.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/hashicorp/errwrap = 3d5d8f294aa03d8e98859feac328afbdf1ae0703
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/hashicorp/go-multierror = 3d5d8f294aa03d8e98859feac328afbdf1ae0703
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/klauspost/compress)) = v1.4.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/klauspost/cpuid)) = ae7887de9fa5d2db4eaa8174a7eff2c1ac00f2da
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/klauspost/crc32)) = cb6bfca970f6908083f26f39a79009d608efd5cd
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/klauspost/pgzip)) = 0bf5dcad4ada2814c3c00f996a982270bb81a506
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/mattn/go-colorable)) = v0.0.9
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/mattn/go-isatty)) = v0.0.3
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/mohae/deepcopy)) = 491d3605edfb866af34a48075bd4355ac1bf46ca
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/go-digest)) = v1.0.0-rc1
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/image-spec/specs-go)) = v1.0.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/image-spec/specs-go/v1)) = v1.0.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-spec/specs-go)) = v1.0.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-tools/filepath)) = v0.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-tools/error)) = v0.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-tools/generate)) = v0.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-tools/generate/seccomp)) = v0.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-tools/specerror)) = v0.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/opencontainers/runtime-tools/validate)) = v0.7.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/pkg/errors)) = v0.8.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/rootless-containers/proto/go-proto)) = v0.1.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/sirupsen/logrus)) = v1.0.6
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/syndtr/gocapability/capability)) = 33e07d32887e1e06b7c025f27ce52f62c7990bc0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/urfave/cli)) = v1.20.0
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/vbatts/go-mtree)) = v0.4.3
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/vbatts/go-mtree/pkg/govis)) = v0.4.3
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/vbatts/go-mtree/xattr)) = v0.4.3
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/xeipuuv/gojsonpointer)) = 4e3ac2762d5f479393488629ee9370b50873b3a6
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/xeipuuv/gojsonreference)) = bd5ef7bd5415a7ac448318e64f11a24cd21e594b
Provides:       bundled(golang(%{import_path}/vendor/src/github.com/xeipuuv/gojsonschema)) = b84684d0e066369f2a7a8a525f3080909ed4ea6b
Provides:       bundled(golang(%{import_path}/vendor/src/golang.org/x/crypto/ripemd160)) = c126467f60eb25f8f27e5a981f32a87e3965053f
Provides:       bundled(golang(%{import_path}/vendor/src/golang.org/x/crypto/ssh/terminal)) = c126467f60eb25f8f27e5a981f32a87e3965053f
Provides:       bundled(golang(%{import_path}/vendor/src/golang.org/x/net/context)) = f4c29de78a2a91c00474a2e689954305c350adf9
Provides:       bundled(golang(%{import_path}/vendor/src/golang.org/x/sys/unix)) = 3dc4335d56c789b04b0ba99b7a37249d9b614314
Provides:       bundled(golang(%{import_path}/vendor/src/golang.org/x/sys/windows)) = 3dc4335d56c789b04b0ba99b7a37249d9b614314
%endif

%description devel
%{summary}.

This package contains library sources intended for building other packages
which use the import path %{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:        Unit tests for %{name} package
BuildArch:      noarch
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

# test subpackage tests code from devel subpackage
Requires:       %{name}-devel = %{version}-%{release}

%if ! 0%{?with_bundled}
Requires:       golang(github.com/golang/protobuf/proto)
Requires:       golang(github.com/mohae/deepcopy)
Requires:       golang(github.com/opencontainers/go-digest)
Requires:       golang(github.com/opencontainers/image-spec/specs-go)
Requires:       golang(github.com/opencontainers/image-spec/specs-go/v1)
Requires:       golang(github.com/opencontainers/runtime-spec/specs-go)
Requires:       golang(github.com/pkg/errors)
Requires:       golang(github.com/rootless-containers/proto/go-proto)
Requires:       golang(github.com/vbatts/go-mtree)
Requires:       golang(golang.org/x/net/context)
Requires:       golang(golang.org/x/sys/unix)
%endif

%description unit-test-devel
%{summary}.

This package contains unit tests for project providing packages with
%{import_path} prefix.
%endif

%prep
%setup -q -n %{name}-%{version}

%build
%if 0%{?with_bundled}
mkdir _output
pushd _output
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd

ln -s vendor src
export GOPATH=$(pwd)/_output:$(pwd):%{gopath}
%else
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}

export GOPATH=$(pwd):%{gopath}
%endif

export LDFLAGS="-X main.version=%{version}"
export GO111MODULE=off
%gobuild -o _bin/%{name} %{import_path}/cmd/%{name}

for manpage in doc/man/*.md; do
    go-md2man -in ${manpage} -out "${manpage%%.md}"
done

%install
install -D -p -m 0755 _bin/%{name} %{buildroot}%{_bindir}/%{name}

for file in doc/man/*.1; do               
  install -D -p -m 0644 $file "%{buildroot}/%{_mandir}/man1/$(basename $file)"       
done 

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
# find all *.s and *.c source and syscall files and generate devel.file-list
for file in $(find . -iname "*.s" -o -iname "*.c"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

export GO111MODULE=off
%gotest %{import_path}/cmd/umoci
%gotest %{import_path}/mutate
%gotest %{import_path}/oci/cas/dir
%gotest %{import_path}/oci/casext
%gotest %{import_path}/oci/config/generate
%gotest %{import_path}/oci/layer
%gotest %{import_path}/pkg/idtools
%gotest %{import_path}/pkg/mtreefilter
%gotest %{import_path}/pkg/system
%gotest %{import_path}/pkg/unpriv
%gotest %{import_path}/third_party/user

%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc *.md MAINTAINERS
%{_bindir}/%{name}
%{_mandir}/man1/umoci*

%if 0%{?with_devel}
%files devel -f devel.file-list
%license COPYING
%doc *.md MAINTAINERS
%endif

%if 0%{?with_unit_test}
%files unit-test-devel -f unit-test.file-list
%license COPYING
%doc *.md MAINTAINERS
%endif

%changelog
* Sun Nov 11 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.3-0.1
- Update to 0.4.3

* Tue Sep 11 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.2-0.1
- Update to 0.4.2

* Tue Sep 04 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.1-0.1
- Update to 0.4.1

* Fri Apr 13 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.0-0.2
- Disable failing test (see openSUSE/umoci#235)
- Don't set commit hash for stable release

* Wed Apr 11 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.0-0.1
- Initial package

