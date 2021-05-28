%bcond_without check

%if 0%{?centos} && 0%{?centos} < 9
%global debug_package %{nil}
%endif

# https://github.com/opencontainers/umoci
%global goipath        github.com/opencontainers/umoci
Version:               0.4.7

%if 0%{?fedora} || 0%{?centos} >= 8
%gometa
%endif

%global common_description %{expand:
umoci modifies Open Container images.}

%global golicenses     COPYING
%global godocs         CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md MAINTAINERS README.md

%if 0%{?centos} && 0%{?centos} < 8
Name:                  golang-github-opencontainers-umoci
%else
Name:                  %{goname}
%endif
Release:               0.1%{?dist}
Summary:               umoci modifies Open Container images

License:               ASL 2.0
URL:                   https://umo.ci/
Source0:               https://github.com/opencontainers/%{name}/archive/v%{version}.tar.gz

%if 0%{?centos} && 0%{?centos} < 8
BuildRequires:         %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%endif
BuildRequires:         go-md2man
Provides:              umoci = %{version}-%{release}
Obsoletes:             umoci < %{version}-%{release}

%description
%{common_description}

umoci is a manipulation tool for OCI images. In particular, it is an
alternative to oci-image-tools provided by the OCI.

%gopkg

%prep
%if 0%{?centos} && 0%{?centos} < 9
%setup -q -n umoci-%{version}
%else
# Keep vendor code
%goprep -k
%endif

%build
%if 0%{?centos}
%if 0%{?centos} < 8
%define gobuild(o:) go build -tags="$BUILDTAGS rpm_crashtraceback" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif
%if 0%{?centos} < 9
%define gobuilddir %{_builddir}/_build
%endif
%endif

export LDFLAGS="${LDFLAGS} -X %{goipath}.version=%{version}"
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

for manpage in doc/man/*.md; do
  go-md2man -in ${manpage} -out "${manpage%%.md}"
done

%install
%if 0%{?fedora}
%gopkginstall
%endif
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

for file in doc/man/*.1; do               
  install -D -p -m 0644 $file "%{buildroot}/%{_mandir}/man1/$(basename $file)"       
done 

%if %{with check}
%check
%if 0%{?centos} && 0%{?centos} < 9
%global gotest go test
%gotest ./...
%else
%gocheck
%endif
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*
%{_mandir}/man1/umoci*

%if 0%{?fedora}
%gopkgfiles
%endif

%changelog
* Sat May 29 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.7-0.1
- Update to 0.4.7.
- Rename to match Golang packaging guidelines

* Fri May 28 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.6-0.1
- Update to 0.4.6.
- Complete spec file rewrite with new macros but keep minimal EPEL compatibility.

* Sun Apr 12 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.5-0.1
- Update to 0.4.5.

* Sun Feb 17 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.4-0.1
- Update to 0.4.4

* Mon Nov 12 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.4.3-0.2
- Set GO111MODULE=off to fix build on Fedora 29 and rawhide

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

