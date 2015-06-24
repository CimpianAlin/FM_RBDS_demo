# RPM package for rh.FM_RBDS_demo
# This file is regularly AUTO-GENERATED by the IDE. DO NOT MODIFY.

# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix: %{_prefix}

Name: rh.FM_RBDS_demo
Summary: Waveform rh.FM_RBDS_demo
Version: 1.0.0
Release: 1
License: None
Group: REDHAWK/Waveforms
Source: %{name}-%{version}.tar.gz
# Require the controller whose SPD is referenced
Requires: rh.TuneFilterDecimate
# Require each referenced component
Requires: rh.TuneFilterDecimate rh.fastfilter rh.RBDSDecoder rh.AmFmPmBasebandDemod rh.psk_soft
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description

%prep
%setup

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p "$RPM_BUILD_ROOT%{_prefix}/dom/waveforms/rh/FM_RBDS_demo"
%__install -m 644 FM_RBDS_demo.sad.xml $RPM_BUILD_ROOT%{_prefix}/dom/waveforms/rh/FM_RBDS_demo/FM_RBDS_demo.sad.xml

%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/waveforms/rh/FM_RBDS_demo
%{_prefix}/dom/waveforms/rh/FM_RBDS_demo/FM_RBDS_demo.sad.xml
