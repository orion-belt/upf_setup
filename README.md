# Test set up for vpp-upf
## Build vpp-upf

docker build -t vpp_upf:u18 docker/

docker run  --privileged -ti vpp_upf:u18

## Inside container
./scripts/rc.local

cd upf && ./run.sh

## Inside container (another terminal)
cd pfcp-kitchen-sink/ <br/>
./pfcpclient -r 172.21.16.2:8805 -s examples/session.yaml

