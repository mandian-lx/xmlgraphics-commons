Name:           xmlgraphics-commons
Version:        1.4
Release:        5
Summary:        XML Graphics Commons

Group:          Development/Java
License:        ASL 2.0
URL:            http://xmlgraphics.apache.org/
Source0:        http://apache.skknet.net/xmlgraphics/commons/source/%{name}-%{version}-src.tar.gz
Patch0:         %{name}-java-7-fix.patch

BuildArch:      noarch
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit
BuildRequires:  apache-commons-io >= 0:1.1
BuildRequires:  apache-commons-logging >= 0:1.0.4
Requires:	apache-commons-logging >= 0:1.0.4
Requires:       apache-commons-io >= 0:1.1
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

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
%patch0 -p0 

# create pom from template
sed "s:@version@:%{version}:g" %{name}-pom-template.pom \
    > %{name}.pom

%build
export CLASSPATH=$(build-classpath commons-logging)
export OPT_JAR_LIST="ant/ant-junit junit"
pushd lib
ln -sf $(build-classpath commons-io) .
popd
ant package javadocs

%install
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -Dpm 0644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 %{name}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.apache.xmlgraphics %{name} %{version} JPP %{name}

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%doc LICENSE NOTICE README
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}


