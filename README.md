# Malicious-program-classification-and-recognition

## How to use it

### 1. prepare your malicious program and rename its parent dic to 'malicious'

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

### 2. import this module

```python3
>>> from maliciousClassify import batchprocess as bp
>>> from maliciousClassify import pre
>>> from maliciousClassify import count
```

### batchprocess

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

### pre

* transfer the asm file to word file

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

### count

* count the number of assembly instructions in asm files

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
