Summary:	Enhanced version of GNU dd with features useful for forensics
Summary(pl.UTF-8):	Rozszerzona wersja GNU dd z opcjami do śledzenia
Name:		dcfldd
Version:	1.3.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/dcfldd/%{name}-%{version}-1.tar.gz
# Source0-md5:	952026c872f11b53ce0ec6681a3eef0a
URL:		http://dcfldd.sourceforge.net/
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
%setup -q -n %{name}-%{version}-1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dcfldd
%{_mandir}/man1/*
