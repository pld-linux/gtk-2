Summary:	The Gimp Toolkit
Summary(cs):	Sada nástrojù pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-työkalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit arayüz kitaplýðý
Name:		gtk+2
Version:	2.4.1
Release:	1
Epoch:		2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk+/2.4/gtk+-%{version}.tar.bz2
# Source0-md5:	b71fc8b24ffd9399f98fc2a41cfe0c0c
Patch0:		%{name}-insensitive-iain.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-2.2.0-path-check.patch
Patch3:		%{name}-menushadow.patch
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
BuildRequires:	atk-devel >= 1.6.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.7
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.4.1
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel >= 1.4.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-8.2
BuildRequires:	xcursor-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	atk >= 1.6.0
Requires:	glib2 >= 1:2.4.1
Requires:	pango >= 1.4.0
Requires:	iconv
Obsoletes:	gtk2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. Gtk+ is written in C with a very
object-oriented approach. Gdk (part of Gtk+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and Gtk is a widget set for
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
Gtk+, która to biblioteka sta³a siê podstaw± programu Gimp zawiera
funkcje do tworzenia graficznego interfejsu u¿ytkownika pod X Window.
By³a tworzona z za³o¿eniem ¿eby by³a ma³a, efektywna i wygodna. Gtk+
jest napisane w C z podej¶ciem zorientowanym bardzo obiektowo. Gdk
(czê¶æ Gtk+) jest warstw± po¶redni± pomiêdzy Xlib a w³a¶ciwym Gtk
zapewniaj±c± pracê niezale¿nie od g³êbi koloru (ilo¶ci bitów na
piksel). Gtk (druga czê¶æ Gtk+) jest natomiast ju¿ zbiorem ró¿nego
rodzaju kontrolek s³u¿±cych do tworzenia interfejsu u¿ytkownika.

%description -l tr
Baþlangýçta GIMP için yazýlmýþ X kitaplýklarý. Þu anda baþka
programlarca da kullanýlmaktadýr.

%package devel
Summary:	Gtk+ header files and development documentation
Summary(cs):	Sada nástrojù GIMP a kreslící kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag³ówkowe i dokumentacja do Gtk+
Summary(tr):	GIMP araç takýmý ve çizim takýmý
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	XFree86-devel
Requires:	atk-devel >= 1.6.0
Requires:	glib2-devel >= 1:2.4.1
Requires:	gtk-doc-common
Requires:	pango-devel >= 1.4.0
Requires:	xcursor-devel
Obsoletes:	gtk2-devel

%description devel
Header files and development documentation for the Gtk+ libraries.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek Gtk+.

%package static
Summary:	Gtk+ static libraries
Summary(pl):	Biblioteki statyczne Gtk+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Gtk+ static libraries.

%description static -l pl
Biblioteki statyczne Gtk+

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv po/{no,nb}.po
mv po-properties/{no,nb}.po

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
	--enable-gtk-doc \
	--enable-shm \
	--enable-xim \
	--with-xinput=xfree \
	--with-gdktarget=x11 \
	--with-html-dir=%{_gtkdocdir} \
	--enable-debug=%{?debug:yes}%{!?debug:minimum} \
	--enable-man

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gtk-2.0}

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

# for various gtk+2 modules
install -d $(echo $RPM_BUILD_ROOT%{_libdir}/gtk-*)/modules
# for gtk+2 theme engines
install -d $(echo $RPM_BUILD_ROOT%{_libdir}/gtk-*/2.*)/engines

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
%attr(755,root,root) %{_bindir}/gdk-pixbuf-query-loaders
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gtk-*
%dir %{_libdir}/gtk-*/modules
%dir %{_libdir}/gtk-*/2.*
%dir %{_libdir}/gtk-*/2.*/engines
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
%{_gtkdocdir}/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
