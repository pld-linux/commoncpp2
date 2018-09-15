#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_with	gnutls		# use GnuTLS instead of OpenSSL [needs update: recent gnutls no longer uses libgcrypt]
#
Summary:	A GNU package for creating portable C++ programs
Summary(pl.UTF-8):	Pakiet GNU do tworzenia przenośnych programów w C++
Name:		commoncpp2
Version:	1.8.1
Release:	4
License:	GPL v2+ with runtime exception
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz
# Source0-md5:	4804b184e609154ba2bc0aa9f61dc6ef
Patch0:		%{name}-netfilter.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-info.patch
Patch4:		openssl.patch
URL:		http://www.gnu.org/software/commoncpp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
%{?with_gnutls:BuildRequires:	gnutls-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel
%{!?with_gnutls:BuildRequires:	openssl-devel}
BuildRequires:	texinfo
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
%{?with_gnutls:Requires:	gnutls-devel}
Requires:	libstdc++-devel
Requires:	libxml2-devel
%{!?with_gnutls:Requires:	openssl-devel}
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	%{?with_gnutls:--with-gnutls} \
	%{!?with_gnutls:--with-openssl}

# ensure netfilter is detected
grep -q 'HAVE_NAT_NETFILTER 1' config.h || exit 1

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.addendum ChangeLog NEWS README SUPPORT THANKS TODO
%attr(755,root,root) %{_libdir}/libccext2-1.8.so.*.*.*
%ghost %{_libdir}/libccext2-1.8.so.0
%attr(755,root,root) %{_libdir}/libccgnu2-1.8.so.*.*.*
%ghost %{_libdir}/libccgnu2-1.8.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,js,png}
%attr(755,root,root) %{_bindir}/ccgnu2-config
%attr(755,root,root) %{_libdir}/libccext2.so
%attr(755,root,root) %{_libdir}/libccgnu2.so
%{_libdir}/libccext2.la
%{_libdir}/libccgnu2.la
%{_includedir}/cc++
%{_aclocaldir}/ost_check2.m4
%{_pkgconfigdir}/libccext2.pc
%{_pkgconfigdir}/libccgnu2.pc
%{_infodir}/commoncpp2.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libccext2.a
%{_libdir}/libccgnu2.a
%endif
