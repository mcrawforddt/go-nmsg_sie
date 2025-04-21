%global debug_package %{nil}
# https://github.com/farsightsec/go-nmsg_sie
%global goipath         github.com/farsightsec/go-nmsg_sie

Name:           go-nmsg_sie
Version:        0.1.1
Release:        1%{?dist}
Summary:        SIE Message Module for go-nmsg

%gometa

License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

%global common_description %{expand:
Provides definitions for message types from sie-nmsg for use with the go-nmsg library.}
%global godocs  README.md

%description
%{common_description}

%package -n %{goname}-devel
Summary:	    %{summary}
BuildArch:      noarch
%description -n %{goname}-devel
%{common_description}

%prep
%setup -q

%install
find .
for file in $(find . -iname "*.go" \! -iname "*_test.go" \! -iname "main.go" ) ; do
    echo "%%dir %%{gopath}/src/%%{goipath}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{goipath}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{goipath}/$file
    echo "%%{gopath}/src/%%{goipath}/$file" >> devel.file-list
done
sort -u -o devel.file-list devel.file-list

%if %{rhel} != 8
%if %{with check}
%check
%gocheck
%endif
%endif

%files -n %{goname}-devel -f devel.file-list

%changelog
