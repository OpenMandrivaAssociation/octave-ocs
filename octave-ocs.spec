%define octpkg ocs

Summary:	Package for solving DC and transient electrical circuit equations
Name:		octave-%{octpkg}
Version:	0.1.5
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:		%{name}-0.1.5-fix_build.patch
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 3.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Package for solving DC and transient electrical circuit equations 

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

