Summary:	The Gimp Toolkit
Summary(cs):	Sada nástrojù pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-työkalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit arayüz kitaplýðý
Name:		gtk+2
Version:	2.1.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtk+/2.1/gtk+-%{version}.tar.bz2
Patch1:		%{name}-Xft2.patch
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
BuildRequires:  Xft-devel >= 2.0
BuildRequires:	atk-devel >= 1.0.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.1.0
BuildRequires:	gtk-doc >= 0.9-4
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.0.4
Requires(post):	/sbin/ldconfig
Requires:	glib2 >= 2.1.0
Requires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gtk2

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

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
Requires:	%{name} = %{version}
Requires:	XFree86-devel
Requires:	atk-devel >= 1.0.0
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	glib2-devel >= 2.0.1
Requires:	gtk-doc-common
Requires:	libtool  >= 1.3.2
Requires:	pango-devel >= 1.0.0
Obsoletes:	gtk2-devel

%description devel
Header files and development documentation for the Gtk+ libraries.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek Gtk+.

%package static
Summary:	Gtk+ static libraries
Summary(pl):	Biblioteki statyczne Gtk+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Gtk+ static libraries.

%description static -l pl
Biblioteki statyczne Gtk+

%prep
%setup -q -n gtk+-%{version}
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%configure \
	--enable-static \
	--enable-gtk-doc \
	--enable-shm \
	--enable-xim \
	--with-xinput=xfree \
	--with-gdktarget=x11 \
	--with-html-path=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gtk-2.0}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir} \
	HTML_DIR=%{_gtkdocdir}

#ln -sf ../../lib/gtk-2.0/2.0.100/immodules $RPM_BUILD_ROOT/%{_sysconfdir}/gtk-2.0/gtk.immodules

touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gtk.immodules

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# remove unsupported locale scheme
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en@IPA

%find_lang gtk20

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules

%postun -p /sbin/ldconfig

%files -f gtk20.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gtk-demo
%attr(755,root,root) %{_bindir}/gtk-query*
%attr(755,root,root) %{_bindir}/gdk-pixbuf-query-loaders
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gtk-*
%dir %{_libdir}/gtk-*/2.*
%dir %{_libdir}/gtk-*/2.*/loaders
%attr(755,root,root) %{_libdir}/gtk-*/2.*/loaders/*.so
%dir %{_libdir}/gtk-*/2.*/immodules
%attr(755,root,root) %{_libdir}/gtk-*/2.*/immodules/*.so
%{_datadir}/gtk-*
%dir %{_sysconfdir}/gtk-*
%ghost %{_sysconfdir}/gtk-*/*
# %dir %{_datadir}/themes/Default	-- belongs to gtk+ 1.2
%dir %{_datadir}/themes/Default/gtk-*
%{_datadir}/themes/Default/gtk-*/gtkrc
%dir %{_datadir}/themes/Emacs
%dir %{_datadir}/themes/Emacs/gtk-*
%{_datadir}/themes/Emacs/gtk-*/gtkrc

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*csource
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/gtk-*/2.*/*/*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_libdir}/gtk-*/include
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/*
%{_gtkdocdir}/*
%doc %{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gtk-*/2.*/loaders/*.a
%{_libdir}/gtk-*/2.*/immodules/*.a
