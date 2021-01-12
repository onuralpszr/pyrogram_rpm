%global modname pyrogram
%global srcname Pyrogram


Name:       python-%{modname}
Version:    1.1.11
Release:    1%{?dist}
Summary:    Telegram MTProto API Framework for Python
License:    LGPLv3+
BuildArch:  noarch
URL:        https://pypi.python.org/pypi/Pyrogram
Source0:    %{pypi_source}


%global _description %{expand:
Pyrogram is a modern, elegant and easy-to-use Telegram client library framework written from the ground up in Python and C. 
It enables you to easily create custom Telegram client applications for both user and bot identities 
(bot API alternative) via the MTProto API. }

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-devel         

Recommends: python3-tgcrypto

Requires:  python3-pyaes
Requires:  python3-pysocks
Requires:  python3-async-lru


%description -n python3-%{modname} %{_description}


Python 3 version.
%global debug_package %{nil}

%prep
%autosetup -n %{srcname}-%{version}
rm -rf tests/



%build
%py3_build

%install
python3 setup.py install --root %{buildroot}
%files -n python3-%{modname}
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{srcname}-*.egg-info/




%changelog
* Tue Jan 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.1.11-1
- Pyrogram Version updated to 1.1.11-1

%changelog
* Tue Jan 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.1.10-1
- Initial package