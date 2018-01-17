Name: rubys-server-config
Version: 1.0
Release: %{_release}
Summary: Server config
License: MIT
Source0: root.tar.gz
BuildArch: noarch

%description
Server config

%prep
tar -xvf %{SOURCE0}

%install
install -d -m 0755 %{buildroot}/etc/systemd/system
install -d -m 0755 %{buildroot}/etc/letsencrypt/conf.d
install -d -m 0755 %{buildroot}/usr/bin
install -d -m 0755 %{buildroot}/etc/nginx/conf.d

cp -R %{_builddir}/* %{buildroot}/

%post
[ ! -f /etc/nginx/dhparams.pem ] && openssl dhparam -out /etc/nginx/dhparams.pem 2048

%files
%defattr(-,root,root)
%dir /etc/systemd/system
%dir /etc/letsencrypt/conf.d
%dir /usr/bin
%dir /etc/nginx/conf.d
/etc/systemd/system/*
/etc/letsencrypt/conf.d/*
/usr/bin/*
/etc/nginx/conf.d/*
