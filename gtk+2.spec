#
# Conditional build:
%bcond_without 	doc	# disable gtk-doc
%bcond_with	xlibs	# use pkgconfig to find libX11
%bcond_with	debug
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
Version:	2.6.0
Release:	3
Epoch:		2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk+/2.6/gtk+-%{version}.tar.bz2
# Source0-md5:	ca717c728264fa0b3302ca00da2bcfe4
Patch0:		%{name}-insensitive-iain.patch
Patch1:		%{name}-menushadow.patch
Patch2:		%{name}-xlibs.patch
Patch3:		%{name}-bug-fixes.patch
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
%{?with_xlibs:BuildRequires:	libXi-devel}
BuildRequires:	atk-devel >= 1.8.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.7
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.6.0-2
%{?with_doc:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel >= 1:1.8.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xcursor-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	atk >= 1.8.0
Requires:	glib2 >= 1:2.6.0-2
Requires:	pango >= 1:1.8.0
Obsoletes:	gtk2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	atk-devel >= 1.8.0
Requires:	glib2-devel >= 1:2.6.0-2
Requires:	gtk-doc-common
Requires:	pango-devel >= 1:1.8.0
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

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1
%patch1 -p1
%{?with_xlibs:%patch2 -p1}
%patch3 -p1

%build
gtkdocize --copy
%{__libtoolize}
glib-gettextize --copy --force
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	%{?with_doc:--enable-gtk-doc} \
	--enable-shm \
	--enable-xim \
	--with-xinput=xfree \
	--with-gdktarget=x11 \
	--with-html-dir=%{_gtkdocdir} \
	--enable-debug=%{?with_debug:yes}%{?without_debug:minium} \
	--enable-man

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gtk-2.0} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/filesystems

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gtk.immodules

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
umask 022
/sbin/ldconfig
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
exit 0

%postun
/sbin/ldconfig
if [ "$1" != "0" ]; then
	umask 022
	%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
	%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
fi
exit 0

%triggerpostun -- gtk+2 < 2:2.4.0
umask 022
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
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
%{?with_doc:%{_gtkdocdir}/*}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
