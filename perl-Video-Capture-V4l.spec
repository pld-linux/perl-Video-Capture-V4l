%define	pdir	Video
%define	pnam	Capture-V4l
%include 	/usr/lib/rpm/macros.perl
Summary:	Perl Video-Capture-V4l module
Summary(pl):	Modu³ Perla Video-Capture-V4l
Name:		perl-Video-Capture-V4l
Version:	0.221
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-make.patch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the Video4linux framegrabber interface.

%description -l pl
Perlowy interfejs do urz±dzeñ Video4linux.

%prep
%setup -q -n Video-Capture-V4l-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{perl_archlib},%{_examplesdir}/%{name}-%{version}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Video
%dir %{perl_sitearch}/auto/Video
%dir %{perl_sitearch}/auto/Video/*
%{perl_sitearch}/auto/Video/*/*.bs
%{perl_sitearch}/auto/Video/*/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Video/*/*.so
%attr(755,root,root) %{perl_sitearch}/auto/Video/*/*/*.so
%{_examplesdir}/%{name}-%{version}

%{_mandir}/man3/*
