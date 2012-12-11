%define	pkgname ocs
%define name	octave-%{pkgname}
%define version 0.1.1

Summary:	Octave package for solving DC and transient circuit equations
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/ocs/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.0.0, octave-odepkg >= 0.0.0
BuildRequires:  octave-devel >= 3.0.0
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel

%description
Octave package for solving DC and transient electrical circuit equations.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .
mv %{pkgname}-%{version}/README .
mv %{pkgname}-%{version}/doc examples

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION README examples
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}



%changelog
* Wed Aug 17 2011 Lev Givon <lev@mandriva.org> 0.1.1-1mdv2012.0
+ Revision: 694809
- import octave-ocs


