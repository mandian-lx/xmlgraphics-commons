Name:           xmlgraphics-commons
Version:        1.4
Release:        2
Summary:        XML Graphics Commons

Group:          Development/Java
License:        ASL 2.0
URL:            http://xmlgraphics.apache.org/
Source0:        http://apache.skknet.net/xmlgraphics/commons/source/%{name}-%{version}-src.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit
BuildRequires:  apache-commons-io >= 0:1.1
BuildRequires:  apache-commons-logging >= 0:1.0.4
Requires:	    apache-commons-logging >= 0:1.0.4
Requires:       apache-commons-io >= 0:1.1

%description
Apache XML Graphics Commons is a library that consists of 
several reusable components used by Apache Batik and 
Apache FOP. Many of these components can easily be used 
separately outside the domains of SVG and XSL-FO. You will 
find components such as a PDF library, an RTF library, 
Graphics2D implementations that let you generate PDF & 
PostScript files, and much more.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description    javadoc
%{summary}.


%prep
%setup -q %{name}-%{version}
rm -f `find . -name "*.jar"`


%build
export CLASSPATH=$(build-classpath commons-logging)
export OPT_JAR_LIST="ant/ant-junit junit"
pushd lib
ln -sf $(build-classpath commons-io) .
popd
ant package javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 0644 build/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README
%{_javadir}/*.jar

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


