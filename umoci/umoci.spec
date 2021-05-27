%bcond_without check

# https://github.com/opencontainers/umoci
%global goipath        github.com/opencontainers/umoci
Version:               0.4.6

%gometa

%global common_description %{expand:
umoci modifies Open Container images.}

%global golicenses     COPYING
%global godocs         CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md MAINTAINERS README.md

Name:                  umoci
Release:               0.1%{?dist}
Summary:               umoci modifies Open Container images

License:               ASL 2.0
URL:                   https://umo.ci/
Source0:               https://github.com/opencontainers/%{name}/archive/v%{version}.tar.gz

BuildRequires:         go-md2man

%description
%{common_description}

umoci is a manipulation tool for OCI images. In particular, it is an
alternative to oci-image-tools provided by the OCI.

%gopkg

%prep
# Keep vendor code
%goprep -k

%build
export LDFLAGS="${LDFLAGS} -X main.version=%{version}"
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

for manpage in doc/man/*.md; do
  go-md2man -in ${manpage} -out "${manpage%%.md}"
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

for file in doc/man/*.1; do               
  install -D -p -m 0644 $file "%{buildroot}/%{_mandir}/man1/$(basename $file)"       
done 

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*
%{_mandir}/man1/umoci*

%gopkgfiles

%changelog
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

