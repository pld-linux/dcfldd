Summary:	Enhanced version of GNU dd with features useful for forensics
Summary(pl.UTF-8):	Rozszerzona wersja GNU dd z opcjami do śledzenia
Name:		dcfldd
Version:	1.9.2
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/resurrecting-open-source-projects/dcfldd/releases
Source0:	https://github.com/resurrecting-open-source-projects/dcfldd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	293ff59a9cc7f9865816ca041272b468
URL:		https://github.com/resurrecting-open-source-projects/dcfldd
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dcfldd is an enhanced version of GNU dd with features useful for
forensics and security. Based on the dd program found in the GNU
Coreutils package, dcfldd has the following additional features:

- Hashing on-the-fly - dcfldd can hash the input data as it is being
  transferred, helping to ensure data integrity.
- Status output - dcfldd can update the user of its progress in terms
  of the amount of data transferred and how much longer operation will
  take.
- Flexible disk wipes - dcfldd can be used to wipe disks quickly and
  with a known pattern if desired.
- Image/wipe Verify - dcfldd can verify that a target drive is a
  bit-for-bit match of the specified input file or pattern.
- Multiple outputs - dcfldd can output to multiple files or disks at
  the same time.
- Split output - dcfldd can split output to multiple files with more
  configurability than the split command.
- Piped output and logs - dcfldd can send all its log data and output
  to commands as well as files natively.

%description -l pl.UTF-8
dcfldd to rozszerzona wersja GNU dd z opcjami przydatnymi przy
śledzeniu i utrzymywaniu bezpieczeństwa. Opierając się na programie dd
z pakietu GNU Coreutils dcfldd ma następujące dodatkowe możliwości:

- Haszowanie w locie: dcfldd potrafi haszować dane wejściowe w trakcie
  przesyłania, co pomaga w zachowaniu ich spójności.
- Wyjście diagnostyczne: dcfldd może informować użytkownika o
  postępach w postaci ilości przesłanych danych i pozostałym czasie
  operacji.
- Elastyczne czyszczenie dysku: dcfldd może być używany do szybkiego
  usuwania danych z dysku, ewentualnie z użyciem znanego wzorca.
- Kontrola obrazów i czyszczenia: dcfldd potrafi sprawdzać, czy dysk
  docelowy zgadza się co do bitu z podanym plikiem wejściowym lub
  wzorcem.
- Wiele wyjść: dcfldd potrafi zapisywać wiele plików lub dysków w tym
  samym czasie.
- Podział wyjścia: dcfldd potrafi podzielić wyjście na wiele plików w
  sposób bardziej konfigurowalny niż robi to polecenie split.
- Wyjście i logowanie przez potoki: dcfldd może wysyłać dane wyjściowe
  i logi do innych poleceń, a także plików.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-bash-completion=%{bash_compdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/dcfldd
%{bash_compdir}/dcfldd-bash_completion
%{_mandir}/man1/dcfldd.1*
