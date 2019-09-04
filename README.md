# Malicious-program-classification-and-recognition

## 1. How to use it

### 1.1 prepare your malicious program and rename its parent dic to 'malicious'

```powershell
PS F:\大四上\小学期\test> ls


    目录: F:\大四上\小学期\test


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         2019/9/4     10:22                malicious


PS F:\大四上\小学期\test> cd .\malicious\
PS F:\大四上\小学期\test\malicious> ls


    目录: F:\大四上\小学期\test\malicious


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         2019/9/4     10:49                backdoor.farfli
d-----         2019/9/4     10:21                rootkit.heur
d-----         2019/9/4     10:21                trojan.downloader
d-----         2019/9/4     10:22                trojan.generic
d-----         2019/9/4     10:22                trojan.pws
d-----         2019/9/4     10:23                variant.graftor
```

### 1.2 import this module

```python3
>>> from maliciousClassify import batchprocess as bp
>>> from maliciousClassify import pre
>>> from maliciousClassify import count
```

#### batchprocess

* Disassemble a batch of executable files

> bp.start(ida_path, malicious_parent_path)

```python3
>>> from maliciousClassify import batchprocess as bp
>>> bp.start('C:\\Program Files (x86)\\IDA\\ida.exe','F:\\大四上\\小学期\\test')
backdoor.farfli
[1]create Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.asm
remove Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.idb
move Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.asm
pass Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.asm~
pass Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.asm~
[2]create Virusshare_00ba9539ed686d7544c871504288fecf.asm
remove Virusshare_00ba9539ed686d7544c871504288fecf.idb
move Virusshare_00ba9539ed686d7544c871504288fecf.asm
pass Virusshare_00ba9539ed686d7544c871504288fecf.asm~
pass Virusshare_00ba9539ed686d7544c871504288fecf.asm
```

```powershell
PS F:\大四上\小学期\test> ls


    目录: F:\大四上\小学期\test


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         2019/9/4     10:27                asm
d-----         2019/9/4     10:22                malicious
```

#### pre

* transfer the asm file to word file

> pre.start(asm_parent_path)

```python3
>>> from maliciousClassify import pre
>>> pre.start('F:\\大四上\\小学期\\test')
Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.asm
Virusshare_00ba9539ed686d7544c871504288fecf.asm
Virusshare_00be1abb0ab6b331f58401d6498f9c46.asm
Virusshare_00bfb0476179651f9d6d5d78e05015db.asm
Virusshare_00c1c2568c63b25734f292716a296d90.asm
Virusshare_00c260d6b6702715e37d9ec0888d12cc.asm
Virusshare_00c5d95f4e64f5cba264c110cd73040a.asm
Virusshare_00cb353b9e71db4bd3c557a609f3cac2.asm
Virusshare_00cfbc769a3be6a1526df8b172107ccb.asm
Virusshare_00d2c93edbab74d9f933f6a3244c5f23.asm
Virusshare_00d34e3574bff764d22ff87686c561f5.asm
```

```powershell
PS F:\大四上\小学期\test> ls


    目录: F:\大四上\小学期\test


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         2019/9/4     10:39                ans
d-----         2019/9/4     10:27                asm
d-----         2019/9/4     10:22                malicious
```

#### count

* count the number of assembly instructions in asm files and sort it

> count.start(ans_parent_path)

```python3
>>> from maliciousClassify import count
>>> count.start('F:\\大四上\\小学期\\test')
Virusshare_00b84b8db26c0a5b8a4708e9e12a7739.asm.ans
Virusshare_00ba9539ed686d7544c871504288fecf.asm.ans
Virusshare_00be1abb0ab6b331f58401d6498f9c46.asm.ans
Virusshare_00bfb0476179651f9d6d5d78e05015db.asm.ans
Virusshare_00c1c2568c63b25734f292716a296d90.asm.ans
Virusshare_00c260d6b6702715e37d9ec0888d12cc.asm.ans
Virusshare_00c5d95f4e64f5cba264c110cd73040a.asm.ans
Virusshare_00cb353b9e71db4bd3c557a609f3cac2.asm.ans
Virusshare_00cfbc769a3be6a1526df8b172107ccb.asm.ans
Virusshare_00d2c93edbab74d9f933f6a3244c5f23.asm.ans
Virusshare_00d34e3574bff764d22ff87686c561f5.asm.ans
```

```powershell
PS F:\大四上\小学期\test> ls


    目录: F:\大四上\小学期\test


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         2019/9/4     10:39                ans
d-----         2019/9/4     10:27                asm
d-----         2019/9/4     10:22                malicious
-a----         2019/9/4     10:43           1226 count.txt

PS F:\大四上\小学期\test> cat .\count.txt
[[15260, "push"], [11175, "mov"], [10730, "pop"], [4529, "inc"], [4144, "dec"], [3540, ","], [2558, "call"], [2310, "jmp"], [1413, "lea"], [1359, "retn"], [1061, "."], [974, "add"], [932, "sub"], [912, "cmp"], [814, "test"], [807, "xor"], [724, "jz"], [600, "and"], [527, "jnz"], [290, "adc"], [281, "stosd"], [245, "or"], [237, "sbb"], [212, "leave"], [192, "rep"], [141, "jl"], [133, "jbe"], [112, "ja"], [106, "nop"], [99, "movzx"], [94, "jle"], [92, "jg"], [82, "jb"], [78, "stosw"], [77, "popa"], [74, "pusha"], [74, "jno"], [70, "jo"], [66, "jge"], [49, "aaa"], [46, "lds"], [40, "shr"], [36, "scasb"], [33, "repne"], [30, "stosb"], [29, "jnb"], [28, "not"], [26, "js"], [25, "shl"], [24, "xchg"], [19, "movsb"], [19, "in"], [15, "retf"], [14, "jns"], [14, "cli"], [12, "cld"], [11, "setnl"], [11, "imul"], [10, "movsx"], [10, "iret"], [9, "cmpsb"], [8, "into"], [8, "aas"], [7, "out"], [7, "lodsb"], [6, "wait"], [6, "std"], [6, "rcr"], [5, "xlat"], [5, "sahf"], [5, "lahf"], [5, "fld"], [5, "daa"], [5, "clc"], [5, "aam"], [4, "sti"], [4, "stc"], [4, "loop"], [4, "fadd"], [4, "aad"], [3, "setnz"], [3, "sal"], [3, "ror"], [3, "loope"], [2, "rol"], [2, "loopne"], [2, "lock"], [2, "idiv"], [2, "hlt"], [2, "fmul"], [1, "setnle"], [1, "neg"], [1, "movsw"], [1, "jp"], [1, "jnp"], [1, "jecxz"], [1, "int"], [1, "fsub"], [1, "fldenv"], [1, "fisub"], [1, "fidiv"], [1, "ficomp"], [1, "ficom"], [1, "fcom"], [1, "fcmovnb"], [1, "cmc"]]
```
