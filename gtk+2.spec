#
# Conditional build:
%bcond_with	macmenu		# experimental mac/kde-like
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	cups		# disable CUPS support
%bcond_without	static_libs	# don't build static library
#
Summary:	The Gimp Toolkit
Summary(cs):	Sada nástrojù pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-työkalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit arayüz kitaplýðý
Name:		gtk+2
Version:	2.10.8
Release:	2
Epoch:		2
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.gtk.org/pub/gtk/v2.10/gtk+-%{version}.tar.bz2
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/2.10/gtk+-%{version}.tar.bz2
# Source0-md5:	46bfef60f02c39acdcdba2ac46825db4
Patch0:		%{name}-insensitive-iain.patch
Patch1:		%{name}-menu-mac.patch
Patch2:		%{name}-free.patch
URL:		http://www.gtk.org/
BuildRequires:	atk-devel >= 1:1.12.4
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 1.2.4
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.7
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	gtk-doc-automake >= 1.7
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-progs >= 1:2.6.27
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	pango-devel >= 1:1.14.9
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	atk >= 1:1.12.4
Requires:	cairo >= 1.2.4
Requires:	glib2 >= 1:2.12.7
Requires:	pango >= 1:1.14.9
Obsoletes:	gtk2
Conflicts:	gtk2-engines < 1:2.2.0-6
# autopanog.exe crashes with gtk+2 2.8.x and libgdiplus 1.1.8
Conflicts:	libgdiplus < 1.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abivers	2.10.0

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%description -l cs
Knihovny X pùvodnì psané pro GIMP, které nyní pou¾ívá také øada jiných
programù.

%description -l da
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de
Die X-Libraries, die ursprünglich für GIMP geschrieben wurden und
mittlerweile für eine ganze Reihe anderer Programme benutzt werden.

%description -l fr
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
käytetään nyt myös useissa muissakin ohjelmissa.

%description -l it
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl
GTK+, która to biblioteka sta³a siê podstaw± programu Gimp zawiera
funkcje do tworzenia graficznego interfejsu u¿ytkownika pod X Window.
By³a tworzona z za³o¿eniem ¿eby by³a ma³a, efektywna i wygodna. GTK+
jest napisane w C z podej¶ciem zorientowanym bardzo obiektowo. GDK
(czê¶æ GTK+) jest warstw± po¶redni± pomiêdzy Xlib a w³a¶ciwym GTK
zapewniaj±c± pracê niezale¿nie od g³êbi koloru (ilo¶ci bitów na
piksel). GTK (druga czê¶æ GTK+) jest natomiast ju¿ zbiorem ró¿nego
rodzaju kontrolek s³u¿±cych do tworzenia interfejsu u¿ytkownika.

%description -l tr
Baþlangýçta GIMP için yazýlmýþ X kitaplýklarý. Þu anda baþka
programlarca da kullanýlmaktadýr.

%package devel
Summary:	GTK+ header files and development documentation
Summary(cs):	Sada nástrojù GIMP a kreslící kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag³ówkowe i dokumentacja do GTK+
Summary(tr):	GIMP araç takýmý ve çizim takýmý
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	atk-devel >= 1:1.12.4
Requires:	glib2-devel >= 1:2.12.7
Requires:	pango-devel >= 1:1.14.9
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXrender-devel
Obsoletes:	gtk2-devel

%description devel
Header files and development documentation for the GTK+ libraries.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek GTK+.

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
Summary(pl):	GTK+ - programy przyk³adowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
GTK+ - example programs.

%description examples -l pl
GTK+ - przyk³adowe programy.

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1
%{?with_macmenu:%patch1 -p0}
%patch2 -p1

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_cups:ac_cv_path_CUPS_CONFIG=no} \
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
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gtk-2.0} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{abivers}/filesystems

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{az_IR,uz@Latn}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
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
%dir %{_libdir}/gtk-*/%{abivers}
%dir %{_libdir}/gtk-*/%{abivers}/engines
%dir %{_libdir}/gtk-*/%{abivers}/filesystems
%dir %{_libdir}/gtk-*/%{abivers}/immodules
%dir %{_libdir}/gtk-*/%{abivers}/loaders
%dir %{_libdir}/gtk-*/%{abivers}/printbackends
%attr(755,root,root) %{_libdir}/gtk-*/%{abivers}/engines/libpixmap.so
%attr(755,root,root) %{_libdir}/gtk-*/%{abivers}/immodules/*.so
%attr(755,root,root) %{_libdir}/gtk-*/%{abivers}/loaders/*.so
%attr(755,root,root) %{_libdir}/gtk-*/%{abivers}/printbackends/*.so

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
