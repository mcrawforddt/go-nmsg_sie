%global debug_package %{nil}

# https://github.com/farsightsec/go-nmsg_sie
%global goipath         github.com/farsightsec/go-nmsg_sie
Version:                0.1.1

%gometa

%global common_description %{expand:
Provides definitions for message types from sie-nmsg for use with the go-nmsg library.}

%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        SIE Message Module for go-nmsg

License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%package -n devel
Summary:	%{summary}
BuildArch:  noarch
%description -n devel
%{common_description}

%prep
%setup -q

#%generate_buildrequires
#%go_generate_buildrequires

%build
mkdir -p %{gobuilddir}/src/%{goipath}
rmdir %{gobuilddir}/src/%{goipath}
ln -s $PWD %{gobuilddir}/src/%{goipath}
export GO111MODULE=off
export GOPATH=/usr/share/gocode:%{gobuilddir}

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

%files -n devel -f devel.file-list

%changelog
