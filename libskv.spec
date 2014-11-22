Summary:	Silly Key Value store
Summary(pl.UTF-8):	Baza do przechowywania danych Silly Key Value
Name:		libskv
Version:	0
%define	snap	20140404
%define	gitrev	58caa0d
Release:	0.%{snap}.1
License:	unknown
Group:		Libraries
Source0:	https://github.com/rossdylan/SKV/archive/%{gitrev}/SKV-%{gitrev}.tar.gz
# Source0-md5:	9d5fdbebc60b388569a9ff2e245357cf
Patch0:		%{name}-libdir.patch
URL:		https://github.com/rossdylan/SKV
BuildRequires:	cmake >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silly Key Value store.

%description -l pl.UTF-8
Baza do przechowywania danych Silly Key Value.

%package devel
Summary:	Header files for SKV library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SKV
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SKV library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SKV.

%prep
%setup -q -n SKV-58caa0d007c563f06078143c5edd15c4b9486403
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -std=c99 -D_XOPEN_SOURCE=500"
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libskv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libskv.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libskv.so
%{_includedir}/libskv
