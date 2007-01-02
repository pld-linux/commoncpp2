Summary:	A GNU package for creating portable C++ programs
Summary(pl):	Pakiet GNU do tworzenia przeno¶nych programów w C++
Name:		commoncpp2
Version:	1.5.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/commoncpp/%{name}-%{version}.tar.gz
# Source0-md5:	559c6cb2e1fbbaa6d1856d037e3722b2
Patch0:		%{name}-Makefile.patch
URL:		http://www.gnu.org/software/commoncpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
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

%description -l pl
Drugie g³ówne wydanie GNU Common C++. GNU Common C++ oferuje przeno¶ne
abstrakcje us³ug systemowych takich jak w±tki, sieci i gniazda.
Oferuje tak¿e poszczególne szkielety u¿yteczne do rozwijania
przeno¶nych aplikacji C++ zawieraj±ce silnik trwa³ych obiektów,
biblioteki matematyczne, w±tków, gniazd itd. GNU Common C++ jest ma³y
i przeno¶ny. Oprócz GNU/Linuksa obs³uguje tak¿e wiêkszo¶æ uniksowych
systemów operacyjnych oraz Win32.

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
%patch0 -p1

%build
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
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
%{_includedir}/cc++
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
