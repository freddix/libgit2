Summary:	Pure C implementation of the Git core methods
Name:		libgit2
Version:	0.20.0
Release:	1
License:	GPL v2 with linking exception
Group:		Libraries
Source0:	https://github.com/libgit2/libgit2/archive/v%{version}.tar.gz
# Source0-md5:	e35f613a37e11354f34249f2faa68237
URL:		http://libgit2.github.com/
BuildRequires:	cmake
BuildRequires:	libssh2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language with
bindings.

%package devel
Summary:	Header files for libgit2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libssh2-devel
Requires:	openssl-devel
Requires:	zlib-devel

%description devel
Header files for libgit2 library.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DINCLUDE_INSTALL_DIR:PATH=include  \
	-DLIB_INSTALL_DIR:PATH=%{_lib}	    \
	-DTHREADSAFE:BOOL=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.md COPYING README.md
%attr(755,root,root) %ghost %{_libdir}/libgit2.so.0
%attr(755,root,root) %{_libdir}/libgit2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgit2.so
%{_includedir}/git2.h
%{_includedir}/git2
%{_pkgconfigdir}/libgit2.pc

