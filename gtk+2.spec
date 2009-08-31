# TODO
# - solve this:
#| /tmp/gtk+2-2.12.8-root-glen $ find -type f|xargs file|grep -i python
#| ./usr/bin/gtk-builder-convert:                                     a python script text executable
#| /tmp/gtk+2-2.12.8-root-glen $ head -n 1 ./usr/bin/gtk-builder-convert
#| !/usr/bin/env python
#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	cups		# disable CUPS support
%bcond_without	static_libs	# don't build static library
#
Summary:	The GIMP Toolkit
Summary(cs.UTF-8):	Sada nástrojů pro GIMP
Summary(de.UTF-8):	Der GIMP-Toolkit
Summary(fi.UTF-8):	GIMP-työkalukokoelma
Summary(fr.UTF-8):	Le toolkit de GIMP
Summary(it.UTF-8):	Il toolkit per GIMP
Summary(pl.UTF-8):	GIMP Toolkit
Summary(tr.UTF-8):	GIMP ToolKit arayüz kitaplığı
Name:		gtk+2
Version:	2.16.6
Release:	1
Epoch:		2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/2.16/gtk+-%{version}.tar.bz2
# Source0-md5:	416412b336d9f3b6b78ca887395d1726
Patch0:		%{name}-objective-c++.patch
Patch1:		%{name}-arch_confdir.patch
Patch2:		%{name}-gtk-builder-convert.patch
URL:		http://www.gtk.org/
BuildRequires:	atk-devel >= 1:1.26.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 1.6.0
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake >= 1.8
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-progs >= 1:2.6.31
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pango-devel >= 1:1.24.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3.0
BuildRequires:	xorg-lib-libXrender-devel
Requires:	atk >= 1:1.25.0
Requires:	cairo >= 1.6.0
Requires:	glib2 >= 1:2.20.0
Requires:	pango >= 1:1.23.0
Requires:	xorg-lib-libXrandr >= 1.3.0
%if %{with cups}
# cups is used by default if gtk+ is built with cups
Suggests:	%{name}-cups = %{epoch}:%{version}-%{release}
%endif
Provides:	gail = 1.23.0
Provides:	gtk2 = %{version}
Obsoletes:	gail
Obsoletes:	gtk2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
Conflicts:	gtk2-engines < 1:2.2.0-6
# autopanog.exe crashes with gtk+2 2.8.x and libgdiplus 1.1.8
Conflicts:	libgdiplus < 1.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abivers	2.10.0

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		_sysconfdir	/etc/gtk%{libext}-2.0
%define		pqext		-%{libext}
%else
%define		_sysconfdir	/etc/gtk-2.0
%define		pqext		%{nil}
%endif

%description
GTK+, which stands for the GIMP ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%description -l cs.UTF-8
Knihovny X původně psané pro GIMP, které nyní používá také řada jiných
programů.

%description -l da.UTF-8
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de.UTF-8
Die X-Libraries, die ursprünglich für GIMP geschrieben wurden und
mittlerweile für eine ganze Reihe anderer Programme benutzt werden.

%description -l fr.UTF-8
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
käytetään nyt myös useissa muissakin ohjelmissa.

%description -l it.UTF-8
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl.UTF-8
GTK+, która to biblioteka stała się podstawą programu GIMP, zawiera
funkcje do tworzenia graficznego interfejsu użytkownika pod X Window.
Była tworzona z założeniem żeby była mała, efektywna i wygodna. GTK+
jest napisane w C z podejściem zorientowanym bardzo obiektowo. GDK
(część GTK+) jest warstwą pośrednią pomiędzy Xlib a właściwym GTK
zapewniającą pracę niezależnie od głębi koloru (ilości bitów na
piksel). GTK (druga część GTK+) jest natomiast już zbiorem różnego
rodzaju kontrolek służących do tworzenia interfejsu użytkownika.

%description -l tr.UTF-8
Başlangıçta GIMP için yazılmış X kitaplıkları. Şu anda başka
programlarca da kullanılmaktadır.

%package devel
Summary:	GTK+ header files and development documentation
Summary(cs.UTF-8):	Sada nástrojů GIMP a kreslící kit GIMP
Summary(da.UTF-8):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de.UTF-8):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi.UTF-8):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr.UTF-8):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it.UTF-8):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do GTK+
Summary(tr.UTF-8):	GIMP araç takımı ve çizim takımı
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	atk-devel >= 1:1.25.0
Requires:	glib2-devel >= 1:2.20.0
Requires:	pango-devel >= 1:1.23.0
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXrandr-devel >= 1.3.0
Requires:	xorg-lib-libXrender-devel
Provides:	gail-devel = 1.23.0
Obsoletes:	gail-devel
Obsoletes:	gtk2-devel

%description devel
Header files and development documentation for the GTK+ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek GTK+.

%package static
Summary:	GTK+ static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GTK+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	gail-static = 1.23.0
Obsoletes:	gail-static

%description static
GTK+ static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GTK+

%package apidocs
Summary:	GTK+ API documentation
Summary(pl.UTF-8):	Dokumentacja API GTK+
Group:		Documentation
Requires:	gtk-doc-common
Provides:	gail-apidocs = 1.23.0
Obsoletes:	gail-apidocs

%description apidocs
GTK+ API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GTK+.

%package examples
Summary:	GTK+ - example programs
Summary(pl.UTF-8):	GTK+ - programy przykładowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
GTK+ - example programs.

%description examples -l pl.UTF-8
GTK+ - przykładowe programy.

%package cups
Summary:	CUPS printing module for GTK+
Summary(pl.UTF-8):	Moduł GTK+ do drukowania przez CUPS
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description cups
CUPS printing module for GTK+.

%description cups -l pl.UTF-8
Moduł GTK+ do drukowania przez CUPS.

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1
%patch1 -p1
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
	--with-html-dir=%{_gtkdocdir} \
	--with-xinput=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{abivers}/filesystems

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk.immodules

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# shut up check-files (static modules and *.la for modules)
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.{a,la}
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{abivers}/*/*.{a,la}

%if "%{_lib}" != "lib"
# We need to have 32-bit and 64-bit binaries as they have hardcoded LIBDIR.
# (needed when multilib is used)
mv $RPM_BUILD_ROOT%{_bindir}/gdk-pixbuf-query-loaders{,%{pqext}}
mv $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0{,%{pqext}}
%endif

# for various GTK+2 modules
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{az_IR,ca@valencia,io}

%find_lang %{name} --all-name

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/{gdk,gdk-pixbuf,gtk}}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/gdk-pixbuf-query-loaders%{pqext} > %{_sysconfdir}/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0%{pqext} > %{_sysconfdir}/gtk.immodules
exit 0

%postun
/sbin/ldconfig
if [ "$1" != "0" ]; then
	umask 022
	# we need to check for dir existence for multilib installs as the $1 is 1
	# if we remove the other arch pkg will be still present.
	# i.e we have installed gtk+2-2.16.5-1.x86_64 and gtk+2-2.16.5-1.i686, and remove gtk+2-2.16.5-1.i686
	if [ -d %{_sysconfdir} ]; then
		%{_bindir}/gdk-pixbuf-query-loaders%{pqext} > %{_sysconfdir}/gdk-pixbuf.loaders
		%{_bindir}/gtk-query-immodules-2.0%{pqext} > %{_sysconfdir}/gtk.immodules
	fi
fi
exit 0

%triggerpostun -- gtk+2 < 2:2.4.0
umask 022
%{_bindir}/gdk-pixbuf-query-loaders%{pqext} > %{_sysconfdir}/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0%{pqext} > %{_sysconfdir}/gtk.immodules
exit 0

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gdk-pixbuf-query-loaders%{pqext}
%attr(755,root,root) %{_bindir}/gtk-demo
%attr(755,root,root) %{_bindir}/gtk-query-immodules-2.0%{pqext}
%attr(755,root,root) %{_bindir}/gtk-update-icon-cache
%attr(755,root,root) %{_libdir}/libgailutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgailutil.so.18
%attr(755,root,root) %{_libdir}/libgdk-x11-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk-x11-2.0.so.0
%attr(755,root,root) %{_libdir}/libgdk_pixbuf-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk_pixbuf-2.0.so.0
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk_pixbuf_xlib-2.0.so.0
%attr(755,root,root) %{_libdir}/libgtk-x11-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-x11-2.0.so.0

%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/modules
%dir %{_libdir}/gtk-2.0/%{abivers}
%dir %{_libdir}/gtk-2.0/%{abivers}/engines
%dir %{_libdir}/gtk-2.0/%{abivers}/filesystems
%dir %{_libdir}/gtk-2.0/%{abivers}/immodules
%dir %{_libdir}/gtk-2.0/%{abivers}/loaders
%dir %{_libdir}/gtk-2.0/%{abivers}/printbackends
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libferret.so
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libgail.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/engines/libpixmap.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/immodules/im-*.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/loaders/libpixbufloader-*.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/printbackends/libprintbackend-file.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/printbackends/libprintbackend-lpr.so

# XXX: just demo data - move to examples?
%{_datadir}/gtk-2.0

%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/im-multipress.conf
%ghost %{_sysconfdir}/gdk-pixbuf.loaders
%ghost %{_sysconfdir}/gtk.immodules
%dir %{_datadir}/themes/Default/gtk-*
%{_datadir}/themes/Default/gtk-*/gtkrc
%dir %{_datadir}/themes/Emacs
%dir %{_datadir}/themes/Emacs/gtk-*
%{_datadir}/themes/Emacs/gtk-*/gtkrc
%dir %{_datadir}/themes/Raleigh
%dir %{_datadir}/themes/Raleigh/gtk-*
%{_datadir}/themes/Raleigh/gtk-*/gtkrc
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*
%{_mandir}/man1/gtk-query-immodules-2.0.1*
%{_mandir}/man1/gtk-update-icon-cache.1*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gdk-pixbuf-csource
%attr(755,root,root) %{_bindir}/gtk-builder-convert
%attr(755,root,root) %{_libdir}/libgailutil.so
%attr(755,root,root) %{_libdir}/libgdk-x11-2.0.so
%attr(755,root,root) %{_libdir}/libgdk_pixbuf-2.0.so
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib-2.0.so
%attr(755,root,root) %{_libdir}/libgtk-x11-2.0.so
%{_libdir}/libgailutil.la
%{_libdir}/libgdk-x11-2.0.la
%{_libdir}/libgdk_pixbuf-2.0.la
%{_libdir}/libgdk_pixbuf_xlib-2.0.la
%{_libdir}/libgtk-x11-2.0.la
%{_includedir}/gail-1.0
%{_includedir}/gtk-2.0
%{_includedir}/gtk-unix-print-2.0
%{_aclocaldir}/gtk-2.0.m4
%{_libdir}/gtk-2.0/include
%{_pkgconfigdir}/gail.pc
%{_pkgconfigdir}/gdk-2.0.pc
%{_pkgconfigdir}/gdk-pixbuf-2.0.pc
%{_pkgconfigdir}/gdk-pixbuf-xlib-2.0.pc
%{_pkgconfigdir}/gdk-x11-2.0.pc
%{_pkgconfigdir}/gtk+-2.0.pc
%{_pkgconfigdir}/gtk+-unix-print-2.0.pc
%{_pkgconfigdir}/gtk+-x11-2.0.pc
%{_mandir}/man1/gdk-pixbuf-csource.1*
%{_mandir}/man1/gtk-builder-convert.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgailutil.a
%{_libdir}/libgdk-x11-2.0.a
%{_libdir}/libgdk_pixbuf-2.0.a
%{_libdir}/libgdk_pixbuf_xlib-2.0.a
%{_libdir}/libgtk-x11-2.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gail-libgail-util
%{_gtkdocdir}/gdk
%{_gtkdocdir}/gdk-pixbuf
%{_gtkdocdir}/gtk
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/printbackends/libprintbackend-cups.so
%endif
