FROM ubuntu:18.04
LABEL name="upf" \
      version="u18" \
      description="Image for travelping upf based on VPP"

# Installing hyperscan library for upf plugin
RUN apt-get update
RUN apt-get install git tree htop sudo wget tcpdump iproute2 python3 nano vim net-tools iputils-ping make -y
RUN wget http://archive.ubuntu.com/ubuntu/pool/universe/h/hyperscan/libhyperscan4_4.7.0-1_amd64.deb \
    http://archive.ubuntu.com/ubuntu/pool/universe/h/hyperscan/libhyperscan-dev_4.7.0-1_amd64.deb
RUN dpkg -i *.deb

# Installing and configuring vpp
RUN git clone https://github.com/travelping/vpp.git upf
COPY patches patches/
RUN patch -p1 -d upf < patches/werror_disable.patch && patch -p1 -d upf < patches/startup_path.patch
RUN touch /etc/apt/apt.conf.d/90forceyes
RUN echo  "APT::Get::Assume-Yes "true";" >> /etc/apt/apt.conf.d/90forceyes
RUN echo  "APT::Get::force-yes "true";" >> /etc/apt/apt.conf.d/90forceyes
RUN make install-dep build -C upf/
RUN groupadd vpp
RUN mv upf/init.conf upf/init.conf.bkp
RUN touch upf/init.conf
COPY scripts scripts/
COPY config config/

# Installing go 1.13 for pfcp session injector
RUN wget https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz && tar -xvf go1.13.3.linux-amd64.tar.gz && ls && mv go /usr/local
ENV GOROOT=/usr/local/go
RUN mkdir goproject
ENV GOPATH=/goproject
ENV PATH=$GOPATH/bin:$GOROOT/bin:$PATH

# Installing pfcp session injector
RUN git clone https://github.com/fdangtran/pfcp-kitchen-sink.git
RUN cd pfcp-kitchen-sink/ && go get  github.com/alvaroloes/enumer && go generate ./pkg/pfcp && go build -o pfcpclient cmd/pfcpclient/main.go
RUN apt-get install python3-pip
RUN pip3 install scapy

# docker build -t vpp_upf:u18 docker/
# docker run  --privileged -ti vpp_upf:u18
# docker exec -it 2a9f009a5af9 /bin/bash
