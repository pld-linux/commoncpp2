#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A GNU package for creating portable C++ programs
Summary(pl.UTF-8):	Pakiet GNU do tworzenia przenośnych programów w C++
Name:		commoncpp2
Version:	1.7.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz
# Source0-md5:	e1041356c3129e4d3d3d6a44f281d905
Patch0:		%{name}-lt.patch
URL:		http://www.gnu.org/software/commoncpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
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
systems as well as Win32, in addition to GNU/Linux.

%description -l pl.UTF-8
Drugie główne wydanie GNU Common C++. GNU Common C++ oferuje przenośne
abstrakcje usług systemowych takich jak wątki, sieci i gniazda.
Oferuje także poszczególne szkielety użyteczne do rozwijania
przenośnych aplikacji C++ zawierające silnik trwałych obiektów,
biblioteki matematyczne, wątków, gniazd itd. GNU Common C++ jest mały
i przenośny. Oprócz GNU/Linuksa obsługuje także większość uniksowych
systemów operacyjnych oraz Win32.

%package devel
Summary:	Header files for commoncpp2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki commoncpp2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libxml2-devel
Requires:	openssl-devel
Requires:	zlib-devel

%description devel
Header files for commoncpp2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki commoncpp2.

%package static
Summary:	Static commoncpp2 library
Summary(pl.UTF-8):	Statyczna biblioteka commoncpp2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static commoncpp2 library.

%description static -l pl.UTF-8
Statyczna biblioteka commoncpp2.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--with-openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.addendum NEWS README TODO ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%ghost %{_libdir}/libccext2-1.7.so.0
%ghost %{_libdir}/libccgnu2-1.7.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.html doc/html/*.*g*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cc++
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_infodir}/*.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
