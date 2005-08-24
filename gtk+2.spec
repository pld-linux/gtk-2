#
# Conditional build:
%bcond_without	doc		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
%bcond_with	xlibs		# use pkgconfig to find libX11
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
Version:	2.8.1
Release:	1
Epoch:		2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v2.8/gtk+-%{version}.tar.bz2
# Source0-md5:	62ffb0e555dcc4eee3eba5e3214897e3
Patch0:		%{name}-insensitive-iain.patch
Patch1:		%{name}-xlibs.patch
# from CVS, should disapear in the next version
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
%{!?with_xlibs:BuildRequires:	X11-devel >= 1:6.8.0}
BuildRequires:	atk-devel >= 1.8.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 0.9.2
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.8.1
%{?with_doc:BuildRequires:	gtk-doc >= 1.0}
%{?with_xlibs:BuildRequires:	libXfixes-devel}
%{?with_xlibs:BuildRequires:	libXi-devel}
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
Requires:	atk >= 1.8.0
Requires:	cairo >= 0.9.2
Requires:	glib2 >= 1:2.8.0
Requires:	pango >= 1:1.10.0
Obsoletes:	gtk2
Conflicts:	gtk2-engines < 1:2.2.0-6
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
%{!?with_xlibs:Requires:	X11-devel >= 1:6.8.0}
Requires:	atk-devel >= 1.8.0
Requires:	glib2-devel >= 1:2.8.0
Requires:	gtk-doc-common
%{?with_xlibs:Requires:	libXfixes-devel}
%{?with_xlibs:Requires:	libXi-devel}
Requires:	pango-devel >= 1:1.10.0
Requires:	xcursor-devel
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

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1
%{?with_xlibs:%patch1 -p1}

%build
%{__gtkdocize}
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{?debug:--enable-debug=yes} \
	%{?with_doc:--enable-gtk-doc} \
	--enable-man \
	--enable-shm \
	--enable-static \
	--with-gdktarget=x11 \
	--with-html-dir=%{_gtkdocdir} \
	--with-xinput=yes \
	%{!?with_static_libs:--disable-static}
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
%{?with_doc:%{_gtkdocdir}/*}
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
