# Test set up for vpp-upf
## 1. Build vpp-upf

```docker build -t vpp_upf:u18 docker/```

```docker run  --privileged -ti vpp_upf:u18```<br>
Or<br>
You can directly use prebuilt docker image<br>

```docker pull rohankharade/vpp_upf:v1```

```docker run  --privileged -ti rohankharade/vpp_upf:v1```

## 2. Networking<br>
This script will create 4 veth pairs viz. It is veth pair interface, so one end of interface is at vpp-upf and one end at host container.<br>
1.N3 (172.20.16.3 <----> 172.20.16.2)<br>
2.N4 (172.21.16.3 <----> 172.21.16.2)<br>
3.N6-pri (172.22.16.3 <----> 172.22.16.2)<br>
4.N6-sec (172.22.16.3 <----> 172.23.16.2)<br>
Note 1- .3 ip is at host and .2 ip is at vpp-upf<br>
Note 2- There are two n6 interfaces but you can have one also. <br>

```./scripts/rc.local```

## 3. Run VPP-UPF (terminal 1)

```cd upf && ./run.sh```

## 4. Run PFCP session injector (terminal 2)
```cd pfcp-kitchen-sink/```

```./pfcpclient -r 172.21.16.2:8805 -s examples/session.yaml```

## 5. Inject data flow (terminal 3)

```cd scripts/```

```data_injection_ul_sgi_pri.py```


## 5. Verify (terminal 1)
See packet processing at UPF nodes -


```show trace```
