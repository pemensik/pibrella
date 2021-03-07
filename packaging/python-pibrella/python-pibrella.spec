%global srcname pibrella

%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-pibrella
Version:        1.4.0
Release:        1%{?dist}
Summary:        Support code and API library for the Pibrella addon board

License:        MIT
URL:            http://pibrella.com/
# project URL
# https://github.com/pimoroni/pibrella
Source0:        https://github.com/pimoroni/%{srcname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
Support code and API library for the Pibrella addon board.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-RPi.GPIO

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python 3 library for the Pibrella addon board.

%package doc
Summary:        Set of exampels for the Pibrella addon board library
Requires:       %{name} = %{version}-%{release}

%{?python_provide:%python_provide python3-%{srcname}}

%description doc
Examples for the Pibrella addon board.

%prep
tar tzf %{SOURCE0}
%autosetup -n %{srcname}-%{version}

%build
CFLAGS="${RPM_OPT_FLAGS} -fcommon"
pushd library
%py3_build
popd

%install
pushd library
%py3_install
popd

%files -n python3-%{srcname}
%doc README.md
%license library/LICENSE.txt
%{python3_sitelib}/pibrella
%{python3_sitelib}/Pibrella-%{version}-py*.egg-info/

%files doc
%doc documentation/*.md
%doc examples

%changelog
* Sun Feb 14 2021 Petr Menšík <pemensik@redhat.com> - 1.4.0-1
- Initial package

