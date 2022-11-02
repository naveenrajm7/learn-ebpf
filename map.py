#!/usr/bin/python3

# Hello World eBPF program
# https://github.com/lizrice/ebpf-beginners/blob/main/hello.py

from time import sleep
from bcc import BPF

program = """
BPF_HASH(clones);


int hello_world(void *ctx) {
    u64 uid;
    u64 counter = 0;
    u64 *p;

    // Get userID of syscall , top 4 bytes GroupID, bottom 4 bytes UserID
    uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;

    // lookup in hash table
    p = clones.lookup(&uid);

    // check for null pointer before dereferencing pointer
    if (p !=0 ) {
        counter = *p;
    }

    counter++;
    clones.update(&uid, &counter);
    
    return 0;
}
"""

b = BPF(text=program)
syscall = b.get_syscall_fnname("clone")
b.attach_kprobe(event=syscall, fn_name="hello_world")

while True:
    sleep(2)
    s = ""
    if len(b["clones"].items()):
        for k,v in b["clones"].items():
            s += "ID {}: {}\t".format(k.value, v.value)
        print(s)
    else:
        print("No entries yet")
