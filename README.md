# Test set up for vpp-upf
## Build vpp-upf

```docker build -t vpp_upf:u18 docker/```

```docker run  --privileged -ti vpp_upf:u18```

## Inside container (terminal 1)
```./scripts/rc.local```

```cd upf && ./run.sh```

## Inside container (terminal 2)
```cd pfcp-kitchen-sink/```

```./pfcpclient -r 172.21.16.2:8805 -s examples/session.yaml```

## Inside container (terminal 3)
```cd scripts/```

```data_injection_ul_sgi_pri.py```
