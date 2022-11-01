#
# Hello World eBPF program
# https://github.com/lizrice/ebpf-beginners/blob/main/hello.py
#
from bcc import BPF

program = """
int hello_world(void *ctx) {
    bpf_trace_printk("Hello World  !\\n");
    return 0;
}
"""

b = BPF(text=program)
syscall = b.get_syscall_fnname("clone")
b.attach_kprobe(event=syscall, fn_name="hello_world")

b.trace_print()