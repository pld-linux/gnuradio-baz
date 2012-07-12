%define	snap	20120412
Summary:	GNU Radio additional functionality
Name:		gnuradio-baz
Version:	0.1
Release:	0.%{snap}.2
License:	GPL v3
Group:		Applications/Engineering
URL:		http://wiki.spench.net/wiki/Gr-baz
# http://svn.spench.net/main/gr-baz/
Source0:	gr-baz-%{snap}.tar.bz2
# Source0-md5:	3ae988c24c0c18967721177eef77ab40
Patch0:		%{name}-link.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cppunit-devel
BuildRequires:	gnuradio-devel
BuildRequires:	libtool
BuildRequires:	python-devel
Requires:	gnuradio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gr-baz is a GNU Radio project that adds new functionality (blocks, GRC
definitions, apps, etc).

%prep
%setup -q -n gr-baz
%patch0 -p1

%build
sh ./bootstrap

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pythondir=%{py_sitedir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_datadir}/gnuradio/grc/blocks/*.xml
%dir %{py_sitedir}/baz/
%{py_sitedir}/baz/*.py*
%attr(755,root,root) %{py_sitedir}/baz/_baz_swig.so
%attr(755,root,root) %{_libdir}/libgnuradio-baz.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnuradio-baz.so.0
