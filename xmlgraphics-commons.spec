%define gcj_support 0

Summary:	XML Graphics Commons
Name:		xmlgraphics-commons
Version:	1.4
Release:	0.0.4
Epoch:		0
Group:		Development/Java
License:	Apache License
URL:		http://xmlgraphics.apache.org/
Source0:	http://apache.osuosl.org/xmlgraphics/commons/source/%{name}-%{version}-src.tar.gz
%if %{gcj_support}
BuildRequires:	java-gcj-compat-devel
%else
BuildArch:	noarch
%endif
BuildRequires:	java-rpmbuild >= 0:1.6
BuildRequires:	ant >= 0:1.6
BuildRequires:	ant-junit >= 0:1.6
BuildRequires:	junit
BuildRequires:	jakarta-commons-io >= 0:1.1
BuildRequires:	jakarta-commons-logging
BuildRequires:	java-1.6.0-openjdk-devel
Requires:	jakarta-commons-io >= 0:1.1
Requires:	jakarta-commons-logging

%description
Apache XML Graphics Commons is a library that consists of 
several reusable components used by Apache Batik and 
Apache FOP. Many of these components can easily be used 
separately outside the domains of SVG and XSL-FO. You will 
find components such as a PDF library, an RTF library, 
Graphics2D implementations that let you generate PDF & 
PostScript files, and much more.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
%{summary}.

%prep
%setup -q
%{__rm} `find . -name "*.jar"`

%build
export JAVA_HOME=%{java_home}
export ANT_HOME=/usr/share/ant
export CLASSPATH=$CLASSPATH:/usr/share/java/commons-logging.jar
export OPT_JAR_LIST="ant/ant-junit junit"
pushd lib
ln -sf $(build-classpath commons-io) .
popd
%ant package javadocs

%install
install -Dpm 0644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%defattr(0644,root,root,0755)
%doc LICENSE NOTICE README
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Sat Sep 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0:1.4-0.0.1mdv2011.0
+ Revision: 575880
- update to new version 1.4 CCBUG: 60888

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0:1.3.1-0.0.2mdv2010.0
+ Revision: 446197
- rebuild

* Sat Nov 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0:1.3.1-0.0.1mdv2009.1
+ Revision: 308062
- spec file clean

* Sat Dec 29 2007 David Walluck <walluck@mandriva.org> 0:1.2-0.1.1mdv2008.1
+ Revision: 139364
- import xmlgraphics-commons


* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Added epoch version from dependencies.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Added missing BuildRoot line.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Fixed install section.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Fixed rpmlint errors.

* Tue Sep 18 2007 Joshua Sumali <jsumali at redhat.com> - 0:1.2-1jpp
- Update to 1.2

* Tue May 23 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- First JPP-1.7 release
