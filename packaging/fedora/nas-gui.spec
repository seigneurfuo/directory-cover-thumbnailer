# fedpkg --release f39 local
# fedpkg --release f39 mockbuild --no-clean-all

Name:           directory-cover-thumbnailer
Version:        1.04
Release:        %autorelease
BuildArch:      noarch
Summary:        Affiche l'image \"cover.<png | jpg>\" en tant que mignature du dossier

License:        None
URL:            .

Requires:       python3
Requires:       python3-pillow

%description
Affiche l'image \"cover.<png | jpg>\" en tant que mignature du dossier

%install
# Programme
mkdir -p %{buildroot}/%{_bindir}
install -m 644 ../../src/directory-cover.py %{buildroot}/%{_bindir}/directory-cover.py

# Thumbnailer
mkdir -p %{buildroot}/usr/share/thumbnailers
install -m 644 ../../src/directory-cover.thumbnailer %{buildroot}/usr/share/thumbnailers/directory-cover.thumbnailer

%files
%{_bindir}/directory-cover.py
/usr/share/thumbnailers/directory-cover.thumbnailer
