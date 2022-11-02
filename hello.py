#!/usr/bin/python3

# Hello World eBPF program
# https://github.com/lizrice/ebpf-beginners/blob/main/hello.py

from bcc import BPF

program = """
int hello_world(void *ctx) {
    u64 uid;

    // Get userID of syscall , top 4 bytes GroupID, bottom 4 bytes UserID
    uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;

    bpf_trace_printk("Hello World!, id: %d\\n", uid);

    return 0;
}
"""

b = BPF(text=program)
syscall = b.get_syscall_fnname("clone")
# Attach to kprobe
b.attach_kprobe(event=syscall, fn_name="hello_world")
b.trace_print()