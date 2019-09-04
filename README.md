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

* count the number of assembly instructions in asm files

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
{"push": 15260, "mov": 11175, "call": 2558, "jmp": 2310, ",": 3540, "inc": 4529, "dec": 4144, "pop": 10730, "sbb": 237, "adc": 290, "add": 974, "sub": 932, "lds": 46, "and": 600, "or": 245, "retn": 1359, ".": 1061, "aaa": 49, "xor": 807, "repne": 33, "scasb": 36, "not": 28, "lea": 1413, "test": 814, "jz": 724, "cmp": 912, "jl": 141, "jge": 66, "movzx": 99, "setnl": 11, "leave": 212, "jb": 82, "stosd": 281, "stosw": 78, "stosb": 30, "jnz": 527, "rep": 192, "shr": 40, "jle": 94, "jbe": 133, "movsx": 10, "movsb": 19, "jnb": 29, "shl": 25, "js": 26, "ja": 112, "nop": 106, "jo": 70, "jno": 74, "cld": 12, "jg": 92, "imul": 11, "pusha": 74, "popa": 77, "in": 19, "clc": 5, "fmul": 2, "xchg": 24, "jns": 14, "fisub": 1, "rcr": 6, "loop": 4, "out": 7, "cli": 14, "aam": 5, "retf": 15, "sahf": 5, "fld": 5, "daa": 5, "lodsb": 7, "fadd": 4, "cmpsb": 9, "loope": 3, "stc": 4, "sal": 3, "idiv": 2, "wait": 6, "lahf": 5, "fldenv": 1, "aad": 4, "fcom": 1, "iret": 10, "cmc": 1, "int": 1, "aas": 8, "fsub": 1, "jecxz": 1, "ficom": 1, "ror": 3, "setnle": 1, "setnz": 3, "neg": 1, "sti": 4, "movsw": 1, "rol": 2, "into": 8, "lock": 2, "jp": 1, "jnp": 1, "xlat": 5, "loopne": 2, "hlt": 2, "fcmovnb": 1, "std": 6, "fidiv": 1, "ficomp": 1}
```
