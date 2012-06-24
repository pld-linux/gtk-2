Summary:	The Gimp Toolkit
Summary(cs):	Sada n�stroj� pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-ty�kalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit aray�z kitapl���
Name:		gtk+2
Version:	1.3.12
Release:	2
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/����������
Group(uk):	X11/��̦�����
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.3/gtk+-%{version}.tar.gz
Patch0:		%{name}-gettext.patch
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
BuildRequires:	glib2-devel >= %{version}
BuildRequires:	fribidi-devel >= 0.10.0
Buildrequires:	atk-devel >= 0.8
BuildRequires:	gettext-devel
BuildRequires:	pango-devel >= 0.21
Requires:	glib2 >= %{version}
Requires:	iconv
Requires:	pango
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	%{_datadir}

%description
Gtk+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. Gtk+ is written in C with a very
object-oriented approach. Gdk (part of Gtk+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and Gtk is a widget set for
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
Gtk+, kt�ra to biblioteka sta�a si� podstaw� programu Gimp zawiera
funkcje do tworzenia graficznego interfejsu u�ytkownika pod X Window.
By�a tworzona z za�o�eniem �eby by�a ma�a, efektywna i wygodna. Gtk+
jest napisane w C z podej�ciem zorientowanym bardzo obiektowo. Gdk
(cz�� Gtk+) jest warstw� po�redni� pomi�dzy Xlib a w�a�ciwym Gtk
zapewniaj�c� prac� niezale�nie od g��bi koloru (ilo�ci bit�w na
piksel). Gtk (druga cz�� Gtk+) jest natomiast ju� zbiorem r�nego
rodzaju kontrolek s�u��cych do tworzenia interfejsu u�ytkownika.

%description -l tr
Ba�lang��ta GIMP i�in yaz�lm�� X kitapl�klar�. �u anda ba�ka
programlarca da kullan�lmaktad�r.

%package devel
Summary:	Gtk+ header files and development documentation
Summary(cs):	Sada n�stroj� GIMP a kresl�c� kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-v�rkt�j
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi):	Gimp-ty�kalukokoelma ja Gimp-piirtoty�kalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag��wkowe i dokumentacja do Gtk+
Summary(tr):	GIMP ara� tak�m� ve �izim tak�m�
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	XFree86-devel
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	glib2-devel >= %{version}
Requires:	libtool  >= 1.3.2
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for the Gtk+ libraries.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do bibliotek Gtk+.

%package static
Summary:	Gtk+ static libraries
Summary(pl):	Biblioteki statyczne Gtk+
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Gtk+ static libraries.

%description -l pl static
Biblioteki statyczne Gtk+

%prep
%setup -q -n gtk+-%{version}

%build
gettextize --copy --force
patch -p1 < %{PATCH0}
aclocal
autoconf
%configure \
	--enable-shm \
	--enable-xim \
	--enable-fbmanager \
	--with-xinput=xfree \
	--with-gdktarget=x11

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

ln -sf ../../lib/gtk-2.0/immodules $RPM_BUILD_ROOT/%{_datadir}/gtk-2.0/gtk.immodules

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang gtk+20

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtk+20.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-demo
%attr(755,root,root) %{_bindir}/gtk-query*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gtk-*
%dir %{_libdir}/gtk-*/%{version}
%dir %{_libdir}/gtk-*/%{version}/loaders
%attr(755,root,root) %{_libdir}/gtk-*/%{version}/loaders/*.so
%dir %{_libdir}/gtk-*/immodules
%dir %{_libdir}/gtk-*/immodules/%{version}
%attr(755,root,root) %{_libdir}/gtk-*/immodules/%{version}/*.so
%{_datadir}/gtk-*
%dir %{_datadir}/themes/Default/gtk-*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*csource
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/gtk-*/%{version}/loaders/*.la
%attr(755,root,root) %{_libdir}/gtk-*/immodules/%{version}/*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_libdir}/gtk-*/include
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gtk-*/%{version}/loaders/*.a
