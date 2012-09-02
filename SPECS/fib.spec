Name: fib
Summary: fib package
Version: 1.0.0
Release: 1
#Group: Applications/Text
License: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
fib package

%prep
%setup -q

%build
make

%install
rm -f %{buildroot}
#%{makeinstall}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
/home/andre/local/usr/bin/fib


