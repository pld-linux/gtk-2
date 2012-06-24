Summary:	The Gimp Toolkit
Summary(cs):	Sada n�stroj� pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-ty�kalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit aray�z kitapl���
Name:		gtk+
Version:	1.3.5
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.3/%{name}-%{version}.tar.gz
#Patch0:	%{name}-info.patch
#Patch1:	%{name}-ahiguti.patch
URL:		http://www.gtk.org/
#Icon:		gtk+.xpm
Requires:	glib >= %{version}
Requires:	iconv
Prereq:		pango
BuildRequires:	glib-devel >= %{version}
Buildrequires:	atk-devel
BuildRequires:	gettext-devel
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info
%define		_mandir		/usr/X11R6/man
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
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	glib-devel >= %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool  >= 1.3.2
# Every program using gtk+ should get a list of libraries to link with by
# executing `gtk-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with gtk+.
Requires:	XFree86-devel
Requires:	glib-devel

%description devel
Header files and development documentation for the Gtk+ libraries.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do bibliotek Gtk+.

%package static
Summary:	Gtk+ static libraries
Summary(pl):	Biblioteki statyczne Gtk+
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Gtk+ static libraries.

%description -l pl static
Biblioteki statyczne Gtk+

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
gettextize --copy --force
%configure \
	--enable-shm \
	--with-xinput=xfree \
	#--enable-debug=no \


%{__make} m4datadir=/usr/share/aclocal

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
#%lang(bg) %{_sysconfdir}/gtk-2.0/gtkrc.bg*
#%lang(cs) %{_sysconfdir}/gtk-2.0/gtkrc.cs
#%lang(cy) %{_sysconfdir}/gtk-2.0/gtkrc.cy
#%lang(el) %{_sysconfdir}/gtk-2.0/gtkrc.el
#%lang(eo) %{_sysconfdir}/gtk-2.0/gtkrc.eo
#%lang(et) %{_sysconfdir}/gtk-2.0/gtkrc.et
#%lang(ga) %{_sysconfdir}/gtk-2.0/gtkrc.ga
#%lang(he) %{_sysconfdir}/gtk-2.0/gtkrc.he
#%lang(hr) %{_sysconfdir}/gtk-2.0/gtkrc.hr
#%lang(hu) %{_sysconfdir}/gtk-2.0/gtkrc.hu
#%lang(hy) %{_sysconfdir}/gtk-2.0/gtkrc.hy
#%lang(ja) %{_sysconfdir}/gtk-2.0/gtkrc.ja
#%lang(ka) %{_sysconfdir}/gtk-2.0/gtkrc.ka*
#%lang(ko) %{_sysconfdir}/gtk-2.0/gtkrc.ko
#%lang(lt) %{_sysconfdir}/gtk-2.0/gtkrc.lt
#%lang(mk) %{_sysconfdir}/gtk-2.0/gtkrc.mk
#%lang(pl) %{_sysconfdir}/gtk-2.0/gtkrc.pl
#%lang(ro) %{_sysconfdir}/gtk-2.0/gtkrc.ro
#%lang(ru) %{_sysconfdir}/gtk-2.0/gtkrc.ru*
#%lang(sk) %{_sysconfdir}/gtk-2.0/gtkrc.sk
#%lang(sl) %{_sysconfdir}/gtk-2.0/gtkrc.sl
#%lang(sq) %{_sysconfdir}/gtk-2.0/gtkrc.sq
#%lang(sr) %{_sysconfdir}/gtk-2.0/gtkrc.sr
#%lang(th) %{_sysconfdir}/gtk-2.0/gtkrc.th
#%lang(tr) %{_sysconfdir}/gtk-2.0/gtkrc.tr
#%lang(uk) %{_sysconfdir}/gtk-2.0/gtkrc.uk
#%lang(vi) %{_sysconfdir}/gtk-2.0/gtkrc.vi*
#%lang(zh) %{_sysconfdir}/gtk-2.0/gtkrc.zh*
#%lang(cs,hr,hu,pl,ro,sk,sl,sq) %{_sysconfdir}/gtk-2.0/gtkrc.iso-8859-2
#%lang(bg,mk,ru,sr) %{_sysconfdir}/gtk-2.0/gtkrc.iso-8859-5
#%lang(lt) %{_sysconfdir}/gtk-2.0/gtkrc.iso-8859-13
#%lang(cy,ga) %{_sysconfdir}/gtk-2.0/gtkrc.iso-8859-14
#%lang(et) %{_sysconfdir}/gtk-2.0/gtkrc.iso-8859-15
%dir %{_libdir}/gtk/themes
%dir %{_libdir}/gtk/themes/engines
%dir %{_sysconfdir}/themes
%{_sysconfdir}/themes/Default

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
#%{_infodir}/*info*gz
/usr/share/aclocal/*.m4

%{_mandir}/man1/gtk-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
