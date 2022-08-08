%global modname tgcrypto
%global srcname TgCrypto

Name:       python-%{modname}
Version:    1.2.3
Release:    %autorelease
Summary:    Fast and Portable Telegram Crypto Library for Python
License:    LGPLv3+
URL:        https://pypi.python.org/pypi/TgCrypto
Source0:    %{pypi_source}


%global _description %{expand:
TgCrypto is a Telegram Crypto Library written in C89 as a Python extension. It is designed to be portable, fast, 
easy to install and use. TgCrypto is intended for Pyrogram and implements the crypto algorithms Telegram requires, namely: 
 
AES256-IGE - used in MTProto v2.0. 
AES256-CTR - used for CDN encrypted files. 
AES256-CBC - used for encrypted passport credentials. }

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}

BuildRequires:  python3dist(setuptools)         
BuildRequires:  gcc
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}


Python 3 version.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf tests/

%build
%py3_build

%install
%py3_install
%files -n python3-%{modname}
%license COPYING COPYING.lesser NOTICE
%doc README.md
%{python3_sitearch}/%{modname}.*-linux-gnu.so
%{python3_sitearch}/%{srcname}-*.egg-info/

%changelog
%autochangelog
