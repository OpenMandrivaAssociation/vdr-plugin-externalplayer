
%define plugin	externalplayer
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	19

Summary:	VDR plugin: launch external players
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://sourceforge.net/projects/externalplayer
Source:		http://prdownloads.sourceforge.net/externalplayer/vdr-%plugin-%version.tar.bz2
Patch0:		externalplayer-0.1.0-i18n-1.6.patch
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
%vdr_plugin_install

install -D -m644 examples/externalplayer.conf %{buildroot}%{vdr_plugin_cfgdir}/externalplayer.conf

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{vdr_plugin_cfgdir}/externalplayer.conf


%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-17mdv2011.0
+ Revision: 404567
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-15mdv2009.1
+ Revision: 359315
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-14mdv2009.0
+ Revision: 197927
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-13mdv2009.0
+ Revision: 197661
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-12mdv2008.1
+ Revision: 145092
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-11mdv2008.1
+ Revision: 103092
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-10mdv2008.0
+ Revision: 49998
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-9mdv2008.0
+ Revision: 42084
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-8mdv2008.0
+ Revision: 22754
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-7mdv2007.0
+ Revision: 90919
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-6mdv2007.1
+ Revision: 74006
- rebuild for new vdr
- Import vdr-plugin-externalplayer

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2007.0
- rebuild for new vdr

* Tue Jul 11 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2007.0
- initial Mandriva release

