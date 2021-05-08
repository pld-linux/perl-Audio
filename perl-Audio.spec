#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		pdir	Audio
Summary:	Audio Perl module - beginnings of Audio manipulation routines from Perl
Summary(pl.UTF-8):	Moduł Perla Audio - początki funkcji do obróbki dźwięku w Perlu
Name:		perl-Audio
Version:	1.029
Release:	17
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	58b67ade294b960f617d9ccc495f07f1
Patch0:		%{name}-nas-fix.patch
Patch1:		%{name}-perl_version.patch
Patch2:		format-security.patch
URL:		http://search.cpan.org/dist/Audio/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	nas-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio Perl module - the beginnings of Audio manipulation routines from
Perl. It can load or save Sun/Next .au/.snd files and play them via
ALSA, Network Audio Server (from ftp://ftp.x.org/) or native Sun (or
compatible) /dev/audio.

%description -l pl.UTF-8
Moduł Perla Audio - początki funkcji do obróbki dźwięku w Perlu. Moduł
ten potrafi wczytywać i zapisywać pliki .au/.snd z Suna/NeXTa oraz
odtwarzać je przez sterowniki ALSA, NAS albo sunowskie (lub
kompatybilne) /dev/audio.

%package Play-Net
Summary:	Audio::Play::Net - nas driver for Audio module
Summary(pl.UTF-8):	Audio::Play::Net - sterownik nas do modułu Audio
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Play-Net
Audio::Play::Net - nas driver for Audio module.

%description Play-Net -l pl.UTF-8
Audio::Play::Net - sterownik nas do modułu Audio.

%package Tk
Summary:	Tk interface to Audio Perl module
Summary(pl.UTF-8):	Interfejs Tk do modułu Perla Audio
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Tk
Tk interface to Audio Perl module.

%description Tk -l pl.UTF-8
Interfejs Tk do modułu Perla Audio.

%package devel
Summary:	Audio Perl module - development files
Summary(pl.UTF-8):	Moduł Perla Audio - pliki nagłówkowe
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description devel
Audio Perl module - development files.

%description devel -l pl.UTF-8
Moduł Perla Audio - pliki nagłówkowe.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="-Wall %{rpmcflags}"

%{?with_tests:%{__make} test}

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
%{perl_vendorarch}/auto/Audio/Data/autosplit.ix
%{perl_vendorarch}/auto/Audio/Data/solve_polynomial.al
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Data/*.so
%dir %{perl_vendorarch}/auto/Audio/Play
%{perl_vendorarch}/auto/Audio/Play/autosplit.ix
%dir %{perl_vendorarch}/auto/Audio/Play/linux
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Play/linux/*.so
%{_mandir}/man3/*

%files Play-Net
%defattr(644,root,root,755)
%{perl_vendorarch}/Audio/Play/Net.pm
%dir %{perl_vendorarch}/auto/Audio/Play/Net
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
