%define plugin	externalplayer

Summary:	VDR plugin: launch external players
Name:		vdr-plugin-%plugin
Version:	0.1.0
Release:	21
Group:		Video
License:	GPL
URL:		https://sourceforge.net/projects/externalplayer
Source:		http://prdownloads.sourceforge.net/externalplayer/vdr-%plugin-%{version}.tar.bz2
Patch0:		externalplayer-0.1.0-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This can be used to launch external players from main menu.

%prep
%setup -q -n %plugin-%{version}
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
%vdr_plugin_install

install -D -m644 examples/externalplayer.conf %{buildroot}%{vdr_plugin_cfgdir}/externalplayer.conf

%files -f %plugin.vdr
%doc README HISTORY
%config(noreplace) %{vdr_plugin_cfgdir}/externalplayer.conf


