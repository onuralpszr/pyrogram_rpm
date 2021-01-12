%global modname async-lru
%global srcname async_lru


Name:       python-%{modname}
Version:    1.0.2
Release:    1%{?dist}
Summary:    Simple lru cache for asyncio
License:    MIT
URL:        https://pypi.python.org/pypi/async_lru
Source0:    %{pypi_source}


%global _description %{expand:
Simple lru cache for asyncio
}

%description %{_description}

%package -n python3-%{modname}
Summary:   %{summary}
%{?python_provide:%python_provide python3-%{modname}}

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-devel


%description -n python3-%{modname} %{_description}


Python 3 version.

%global debug_package %{nil}
%prep
%autosetup -n %{srcname}-%{version}
rm -rf tests/

%build
%py3_build

%install
%py3_install
%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/__pycache__/%{srcname}.*.pyc
%{python3_sitelib}/%{srcname}.py



%changelog
* Mon Jan 11 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.0.2-1
- Initial package