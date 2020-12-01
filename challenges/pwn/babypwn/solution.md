# babypwn
This is a very classic problem.

First thing we can try is running the binary. Go ahead and type anything and press enter. We can guess that it takes in an input and outputs some string.

With that in mind, we can try to disassemble the binary. `gdb` suffices, and you should see this:

```
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401146 <+0>:	push   rbp
   0x0000000000401147 <+1>:	mov    rbp,rsp
   0x000000000040114a <+4>:	sub    rsp,0x50
   0x000000000040114e <+8>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000401155 <+15>:	lea    rax,[rbp-0x50]
   0x0000000000401159 <+19>:	mov    rdi,rax
   0x000000000040115c <+22>:	mov    eax,0x0
   0x0000000000401161 <+27>:	call   0x401050 <gets@plt>
   0x0000000000401166 <+32>:	cmp    DWORD PTR [rbp-0x4],0xdeadbeef
   0x000000000040116d <+39>:	jne    0x401180 <main+58>
   0x000000000040116f <+41>:	mov    edi,0x402010
   0x0000000000401174 <+46>:	mov    eax,0x0
   0x0000000000401179 <+51>:	call   0x401030 <system@plt>
   0x000000000040117e <+56>:	jmp    0x40118f <main+73>
   0x0000000000401180 <+58>:	mov    edi,0x40201b
   0x0000000000401185 <+63>:	mov    eax,0x0
   0x000000000040118a <+68>:	call   0x401040 <printf@plt>
   0x000000000040118f <+73>:	mov    eax,0x0
   0x0000000000401194 <+78>:	leave
   0x0000000000401195 <+79>:	ret
End of assembler dump.
```

Omitting stack frame details (there are good online tutorials for this, go google), let's look at only the key lines.

```
   0x0000000000401155 <+15>:	lea    rax,[rbp-0x50]
   0x0000000000401159 <+19>:	mov    rdi,rax
   0x000000000040115c <+22>:	mov    eax,0x0
   0x0000000000401161 <+27>:	call   0x401050 <gets@plt>
```

Here, we see a `gets` call to read in a string at `[rbp-0x50]`. `gets` doesn't check the number of characters read, so we can perform a simple buffer overflow! But let's continue to see how we can get the flag first. Right after the `gets` call, we have

```
   0x0000000000401166 <+32>:	cmp    DWORD PTR [rbp-0x4],0xdeadbeef
   0x000000000040116d <+39>:	jne    0x401180 <main+58>
```

which means that if `[rbp-0x4]` is equal to `0xdeadbeef`, we will execute the system call:

```
   0x000000000040116f <+41>:	mov    edi,0x402010
   0x0000000000401174 <+46>:	mov    eax,0x0
   0x0000000000401179 <+51>:	call   0x401030 <system@plt>
   0x000000000040117e <+56>:	jmp    0x40118f <main+73>
```

otherwise, we will print some string

```
   0x0000000000401180 <+58>:	mov    edi,0x40201b
   0x0000000000401185 <+63>:	mov    eax,0x0
   0x000000000040118a <+68>:	call   0x401040 <printf@plt>
```

Here, we can already guess that we want to get some value to `0xdeadbeef`. But let's just confirm that. Let's check what are the strings in the system call and print call.

```
gef➤  x/s 0x402010
0x402010:	"cat ./flag"
gef➤  x/s 0x40201b
0x40201b:	"try again"
```

Nice, that confirms our guess. Now, how do we get `[rbp-0x4]` to `0xdeadbeef`? Here comes the buffer overflow: we are reading in at `[rbp-0x50]`, but we can read beyond it's allocated memory, i.e. overflow information into `[rbp-0x4]`. This can be accomplished by sending a string of `(0x50-0x4)` 'A's followed by the target input. Now, if you tried `\xde\xad\xbe\xef`, it wouldn't work unfortunately. Try debugging it in `gdb` and you will see that the input is reversed! This is because of *endianness* (byte order within a word). Hence, you will need to reverse the word `\xef\xbe\ad\de`.

This should get you the flag. Alternatively, if you do not want to manually calculate the required overflow, you can send a cyclic pattern (or just manually create one; an example is given in `solution.py`) and try to match it in `gdb`. Details are left as an exercise for the reader :)
