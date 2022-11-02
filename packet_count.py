#!/usr/bin/python3
from bcc import BPF
from time import sleep

program = """
BPF_HASH(packets);

int hello_packet(struct xdp_md *ctx) {
    u64 key = 0;
    u64 counter = 0;
    u64 *p;

    p = packets.lookup(&key);
    if (p != 0) {
        counter = *p;
    }

    counter++;
    packets.update(&key, &counter);
    
    // change to return XDP_PASS; to not drop packets
    return 0;
}
"""

b = BPF(text=program)
# attach to XDP, on interface eth0 , load function , say this is XDP
b.attach_xdp(dev="eth1", fn=b.load_func("hello_packet", BPF.XDP))

while True:
    sleep(1)
    for k, v in b["packets"].items():
        print("key {}: counter {}".format(k.value, v.value))
