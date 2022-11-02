# learn-ebpf
Repository to getting started with eBPF


## A Beginner’s Guide to eBPF Programming - Liz Rice - Full Keynote
https://youtu.be/lrSExTfS-iQ

**Hello**

```bash
chmod +x hello.py
sudo ./hello.py 
b'            bash-7269    [001] d...1  3541.648739: bpf_trace_printk: Hello World!, id: 1000'
b'            bash-7339    [000] d...1  3635.020690: bpf_trace_printk: Hello World!, id: 0'

## other terminal execute command to catch all clones
ls      # check print logs
sudo su # switch to root
ls      # check userID
```

To see how program is loaded 

```bash
sudo strace -e bpf ./hello.py
```

**Maps**

```bash
chmod +x map.py
sudo ./map.py 

No entries yet
ID 0: 1	
ID 1000: 1	ID 0: 1	

## other terminal execute command to catch all clones
ls      # check print logs
sudo su # switch to root
ls      # check userID
```

**BPF verifier**

```bash
chmod +x null.py
sudo ./null.py 
...
R0 invalid mem access 'map_value_or_null'
processed 10 insns (limit 1000000) max_states_per_insn 0 total_states 1 peak_states 1 mark_read 1

HINT: The 'map_value_or_null' error can happen if you dereference a pointer value from a map lookup without first checking if that pointer is NULL.
...
```


## A Beginner's Guide to eBPF Programming for Networking - Liz Rice, Isovalent
https://youtu.be/0p987hCplbk

Requires containers

## A Load Balancer from scratch – Liz Rice, Isovalent
https://youtu.be/L3_AOFSNKK8

Requires containers



# Resources

BCC or libbpf
https://www.pingcap.com/blog/why-we-switched-from-bcc-to-libbpf-for-linux-bpf-performance-analysis/

