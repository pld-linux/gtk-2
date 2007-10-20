#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
%bcond_without	arch_confdir	# build with architecture-dependant config dir
#
Summary:	The Gimp Toolkit
Summary(cs):	Sada n�stroj� pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-ty�kalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit aray�z kitapl���
Name:		gtk+2
Version:	2.8.20
Release:	2
Epoch:		2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v2.8/gtk+-%{version}.tar.bz2
# Source0-md5:	74e7ca98194f1fadfe906e66d763d05d
Patch0:		%{name}-insensitive-iain.patch
Patch1:		%{name}-tree_selection_emit_changed.patch
Patch2:		%{name}-arch_confdir.patch
URL:		http://www.gtk.org/
BuildRequires:	X11-devel >= 1:6.8.0
BuildRequires:	atk-devel >= 1.8.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 1.0.4
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.10.3
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel >= 1:1.10.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xcursor-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	atk >= 1.11.4
Requires:	cairo >= 1.0.4
Requires:	glib2 >= 1:2.10.3
Requires:	pango >= 1:1.12.3
Obsoletes:	gtk2
Conflicts:	gtk2-engines < 1:2.2.0-6
# autopanog.exe crashes with gtk+2 2.8.x and libgdiplus 1.1.8
Conflicts:	libgdiplus < 1.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with arch_confdir}
%define	_confdir_suf	-%{_target_cpu}
%else
%define	_confdir_suf	%{nil}
%endif

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%description -l cs
Knihovny X p�vodn� psan� pro GIMP, kter� nyn� pou��v� tak� �ada jin�ch
program�.

%description -l da
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de
Die X-Libraries, die urspr�nglich f�r GIMP geschrieben wurden und
mittlerweile f�r eine ganze Reihe anderer Programme benutzt werden.

%description -l fr
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
k�ytet��n nyt my�s useissa muissakin ohjelmissa.

%description -l it
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl
GTK+, kt�ra to biblioteka sta�a si� podstaw� programu Gimp zawiera
funkcje do tworzenia graficznego interfejsu u�ytkownika pod X Window.
By�a tworzona z za�o�eniem �eby by�a ma�a, efektywna i wygodna. GTK+
jest napisane w C z podej�ciem zorientowanym bardzo obiektowo. GDK
(cz�� GTK+) jest warstw� po�redni� pomi�dzy Xlib a w�a�ciwym GTK
zapewniaj�c� prac� niezale�nie od g��bi koloru (ilo�ci bit�w na
piksel). GTK (druga cz�� GTK+) jest natomiast ju� zbiorem r�nego
rodzaju kontrolek s�u��cych do tworzenia interfejsu u�ytkownika.

%description -l tr
Ba�lang��ta GIMP i�in yaz�lm�� X kitapl�klar�. �u anda ba�ka
programlarca da kullan�lmaktad�r.

%package devel
Summary:	GTK+ header files and development documentation
Summary(cs):	Sada n�stroj� GIMP a kresl�c� kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-v�rkt�j
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi):	Gimp-ty�kalukokoelma ja Gimp-piirtoty�kalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag��wkowe i dokumentacja do GTK+
Summary(tr):	GIMP ara� tak�m� ve �izim tak�m�
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	X11-devel >= 1:6.8.0
Requires:	atk-devel >= 1.11.4
Requires:	glib2-devel >= 1:2.10.3
Requires:	gtk-doc-common
Requires:	pango-devel >= 1:1.10.0
Requires:	xcursor-devel
Obsoletes:	gtk2-devel

%description devel
Header files and development documentation for the GTK+ libraries.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do bibliotek GTK+.

%package static
Summary:	GTK+ static libraries
Summary(pl):	Biblioteki statyczne GTK+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GTK+ static libraries.

%description static -l pl
Biblioteki statyczne GTK+

%package apidocs
Summary:	GTK+ API documentation
Summary(pl):	Dokumentacja API GTK+
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GTK+ API documentation.

%description apidocs -l pl
Dokumentacja API GTK+.

%package examples
Summary:	GTK+ - example programs
Summary(pl):	GTK+ - programy przyk�adowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
GTK+ - example programs.

%description examples -l pl
GTK+ - przyk�adowe programy.

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1
%patch1 -p1
%{?with_arch_confdir:%patch2 -p1}

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{?debug:--enable-debug=yes} \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--enable-man \
	--enable-shm \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static \
	--with-gdktarget=x11 \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}} \
	--with-xinput=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gtk-2.0%{_confdir_suf}} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/filesystems

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gtk.immodules

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# remove unsupported locale scheme
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en@IPA
# shut up check-files (static modules and *.la for modules)
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-*/2.*/*/*.{a,la}

# for various GTK+2 modules
install -d $(echo $RPM_BUILD_ROOT%{_libdir}/gtk-*)/modules
# for GTK+2 theme engines
install -d $(echo $RPM_BUILD_ROOT%{_libdir}/gtk-*/2.*)/engines

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gtk.immodules
exit 0

%postun
/sbin/ldconfig
if [ "$1" != "0" ]; then
	umask 022
	%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gdk-pixbuf.loaders
	%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gtk.immodules
fi
exit 0

%triggerpostun -- gtk+2 < 2:2.4.0
umask 022
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0%{_confdir_suf}/gtk.immodules
exit 0

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gtk-demo
%attr(755,root,root) %{_bindir}/gtk-query*
%attr(755,root,root) %{_bindir}/gtk-update-icon-cache
%attr(755,root,root) %{_bindir}/gdk-pixbuf-query-loaders
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gtk-*
%dir %{_libdir}/gtk-*/modules
%dir %{_libdir}/gtk-*/2.*
%dir %{_libdir}/gtk-*/2.*/engines
%attr(755,root,root) %{_libdir}/gtk-*/2.*/engines/libpixmap.so
%dir %{_libdir}/gtk-*/2.*/filesystems
%dir %{_libdir}/gtk-*/2.*/loaders
%attr(755,root,root) %{_libdir}/gtk-*/2.*/loaders/*.so
%dir %{_libdir}/gtk-*/2.*/immodules
%attr(755,root,root) %{_libdir}/gtk-*/2.*/immodules/*.so
%{_datadir}/gtk-*
%dir %{_sysconfdir}/gtk-*
%ghost %{_sysconfdir}/gtk-*/*
%dir %{_datadir}/themes/Default/gtk-*
%{_datadir}/themes/Default/gtk-*/gtkrc
%dir %{_datadir}/themes/Emacs
%dir %{_datadir}/themes/Emacs/gtk-*
%{_datadir}/themes/Emacs/gtk-*/gtkrc
%dir %{_datadir}/themes/Raleigh
%dir %{_datadir}/themes/Raleigh/gtk-*
%{_datadir}/themes/Raleigh/gtk-*/gtkrc

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*csource
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_libdir}/gtk-*/include
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
