
%define plugin	externalplayer
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	13

Summary:	VDR plugin: launch external players
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://sourceforge.net/projects/externalplayer
Source:		http://prdownloads.sourceforge.net/externalplayer/vdr-%plugin-%version.tar.bz2
Patch0:		externalplayer-0.1.0-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This can be used to launch external players from main menu.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# specify path to an alternative config file
var=CFGFILE
param=--config=CFGFILE
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m644 examples/externalplayer.conf %{buildroot}%{_vdr_plugin_cfgdir}/externalplayer.conf

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{_vdr_plugin_cfgdir}/externalplayer.conf
