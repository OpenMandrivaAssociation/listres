%define name	listres
%define version	1.0.1
%define release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	List resources in widgets
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxmu-devel >= 1.0.0
BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The listres program generates a list of a widget's resource database.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/listres
%{_mandir}/man1/listres.*

