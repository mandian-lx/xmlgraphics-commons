%define gcj_support 0

Summary:	XML Graphics Commons
Name:		xmlgraphics-commons
Version:	1.4
Release:	%mkrel 0.0.2
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
Requires:	jakarta-commons-io >= 0:1.1
Requires:	jakarta-commons-logging
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}
install -Dpm 0644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf %{buildroot}

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
