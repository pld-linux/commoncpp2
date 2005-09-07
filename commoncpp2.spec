# TODO: pl description
Summary:	A GNU package for creating portable C++ programs
Summary(pl):	Pakiet GNU do tworzenia przeno¶nych programów C++
Name:		commoncpp2
Version:	1.3.19
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/commonc++/%{name}-%{version}.tar.gz
# Source0-md5:	48c06d224b38e4627f71cd71a726b637
URL:		http://www.gnu.org/software/commonc++/commonc++.html
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the second major release of GNU Common C++. GNU Common C++ "2"
is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. GNU Common C++ "2"
also offers individual frameworks generally useful to developing
portable C++ applications including a object persistance engine, math
libraries, threading, sockets, etc. GNU Common C++ "2" is small, and
highly portable. GNU Common C++ "2" will support most Unix operating
systems as well as W32, in addition to GNU/Linux.

%package devel
Summary:	Header files for commoncpp2 library
Summary(pl):	Pliki nag³ówkowe biblioteki commoncpp2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libxml2-devel
Requires:	zlib-devel

%description devel
Header files for commoncpp2 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki commoncpp2.

%package static
Summary:	Static commoncpp2 library
Summary(pl):	Statyczna biblioteka commoncpp2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static commoncpp2 library.

%description static -l pl
Statyczna biblioteka commoncpp2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.addendum NEWS README TODO ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.html doc/html/*.*g*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cc++2
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_infodir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
