#
# Conditional build:
# _with_tests - perform "make test" (needs working, not busy /dev/audio!)
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
Summary:	Audio Perl module - beginnings of Audio manipulation routines from Perl
Summary(pl):	Modu³ Perla Audio - pocz±tki funkcji do obróbki d¼wiêku w Perlu
Name:		perl-Audio
Version:	1.000
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Patch0:		%{name}-nas-fix.patch
Patch1:		%{name}-perl_version.patch
BuildRequires:	nas-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio Perl module - the beginnings of Audio manipulation routines from
Perl. It can load or save Sun/Next .au/.snd files and play them via
Network Audio Server (from ftp://ftp.x.org/) or native Sun (or
compatible) /dev/audio.

%description -l pl
Modu³ Perla Audio - pocz±tki funkcji do obróbki d¼wiêku w Perlu. Modul
ten potrafi wczytywaæ i zapisywaæ pliki .au/.snd z Suna/NeXTa oraz
odtwarzaæ je przez NAS albo sunowskie (lub kompatybilne) /dev/audio.

%package Play-Net
Summary:	Audio::Play::Net - nas driver for Audio module
Summary(pl):	Audio::Play::Net - sterownik nas do modu³u Audio
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Play-Net
Audio::Play::Net - nas driver for Audio module.

%description Play-Net -l pl
Audio::Play::Net - sterownik nas do modu³u Audio.

%package Tk
Summary:	Tk interface to Audio Perl module
Summary(pl):	Interfejs Tk do modu³u Perla Audio
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Tk
Tk interface to Audio Perl module.

%description Tk -l pl
Interfejs Tk do modu³u Perla Audio.

%package devel
Summary:	Audio Perl module - development files
Summary(pl):	Modu³ Perla Audio - pliki nag³ówkowe
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description devel
Audio Perl module - development files.

%description devel -l pl
Modu³ Perla Audio - pliki nag³ówkowe.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# names are too common
cd $RPM_BUILD_ROOT%{_bindir}
for f in * ; do
	mv -f $f Audio-$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_bindir}/Audio-[dmp]*
%{perl_vendorarch}/Audio/*.pm
%{perl_vendorarch}/Audio/Data
%dir %{perl_vendorarch}/Audio/Play
%{perl_vendorarch}/Audio/Play/linux.pm
%dir %{perl_vendorarch}/auto/Audio/Data
%{perl_vendorarch}/auto/Audio/Data/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Data/*.so
%dir %{perl_vendorarch}/auto/Audio/Play
%{perl_vendorarch}/auto/Audio/Play/autosplit.ix
%dir %{perl_vendorarch}/auto/Audio/Play/linux
%{perl_vendorarch}/auto/Audio/Play/linux/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Play/linux/*.so
%{_mandir}/man3/*

%files Play-Net
%defattr(644,root,root,755)
%{perl_vendorarch}/Audio/Play/Net.pm
%dir %{perl_vendorarch}/auto/Audio/Play/Net
%{perl_vendorarch}/auto/Audio/Play/Net/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Play/Net/*.so

%files Tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Audio-t*
%{perl_vendorarch}/Tk/Scope.pm

%files devel
%defattr(644,root,root,755)
%doc README.Porting
%{perl_vendorarch}/Audio/*.h
%{perl_vendorarch}/Audio/*.m
%{perl_vendorarch}/Audio/*.t
%{perl_vendorarch}/Audio/typemap
