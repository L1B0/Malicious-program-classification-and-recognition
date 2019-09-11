import os
import re
from tqdm import tqdm

def pre(now_pwd, root,filename,cmd):
    loc=r'^loc'
    substart=r'^sub.*proc'
    end=r'.*endp'
    #print(filename)
    #r = str(root).split('/')
    destdir = now_pwd + "/ans/" + root
    if not os.path.exists(destdir):
        os.makedirs(destdir)

    if os.path.exists(destdir + '/' + filename + '.ans'):
        # print(filename+"已处理\n")
        return

    flag=False#是否能直接接逗号或者句号
    with open(now_pwd+'/asm/'+root+'/'+filename,'r',encoding='utf-8') as f,open(destdir + '/' + filename + ".ans",'w+',encoding='utf-8') as d:
        for line in f.readlines():
            #print(line)
            index=line.find(";")
            #print("index=",index)
            if index!=-1:
                line=line[:index]
                #print(line)
            if re.match(substart,line) is not None:
                    pass
            elif re.match(loc,line) is not None and flag==True:
                flag=False
                d.write(', ')
            elif re.match(end,line) is not None and flag==True:
                flag = False
                d.write('.\n')
            else:
                words=line.split()
                for word in words:
                    if word in cmd:
                        flag=True
                        d.write(word+' ')
            #print(word)
            #os.system("pause")

def start(now_pwd):

	print("Start asm2word~")
	cmd=['jnc', 'fstp', 'stos', 'jnp', 'lgs', 'lahf', 'int', 'fnstcw', 'shr', 'frndint', 'jnle', 'fimul', 'fdivrp', 'ftst', 'lodsd', 'rcr', 'fbld', 'move', 'cmovnb', 'clc', 'cmovz', 'fcmovne', 'cdq', 'nop', 'and', 'popf', 'inc', 'jle', 'fldpi', 'shl', 'fcomi', 'xadd', 'pushd', 'lfs', 'xor', 'jnb', 'pushf', 'rol', 'fidivr', 'fcmovb', 'fsin', 'cld', 'fsub', 'out', 'not', 'fisub', 'aaa', 'cmps', 'feni', 'fadd', 'jpo', 'fild', 'fldcw', 'iret', 'popad', 'fst', 'popd', 'rcl', 'loopz', 'xlat', 'repe', 'fwait', 'fidiv', 'loope', 'fnstsw', 'setnb', 'mul', 'js', 'scas', 'fxam', 'fsubp', 'esc', 'jg', 'faddp', 'jpe', 'fdivr', 'std', 'fxch', 'jmp', 'cwde', 'fcomp', 'cli', 'sahf', 'fld1', 'mov', 'shld', 'sidt', 'imul', 'stosd', 'ficomp', 'les', 'test', 'sbb', 'setb', 'sal', 'fpatan', 'jc', 'jno', 'retn', 'aad', 'fiadd', 'fabs', 'daa', 'fcmovnb', 'push', 'movsb', 'jae', 'bswap', 'fistp', 'retf', 'fldlg2', 'wait', 'fcompp', 'fstcw', 'lock', 'fldl2e', 'fcmovnbe', 'fucompp', 'jo', 'jna', 'call', 'frstor', 'cmovl', 'pop', 'adc', 'div', 'fclex', 'scasw', 'fmulp', 'ficom', 'fstenv', 'fincstp', 'ffree', 'sar', 'fldz', 'fstsw', 'aam', 'aas', 'cbw', 'fcmovu', 'das', 'finit', 'fsubr', 'fcos', 'fbstp', 'fchs', 'fldln2', 'pusha', 'cmp', 'shrd', 'or', 'loopnz', 'fcom', 'jns', 'repne', 'jcxz', 'pushad', 'jnbe', 'idiv', 'stosb', 'fsave', 'lods', 'fldenv', 'ja', 'fld', 'cmpsb', 'fucomp', 'sti', 'sub', 'repnz', 'fdivp', 'jng', 'setnl', 'cmovle', 'fdiv', 'ror', 'cmovg', 'loopne', 'movsw', 'jz', 'jnl', 'jbe', 'fucom', 'fcmove', 'setnle', 'leave', 'jp', 'lss', 'fscale', 'repz', 'lds', 'jne', 'ret', 'in', 'stc', 'fist', 'bsr', 'jnz', 'fdisi', 'xchg', 'setnz', 'fsubrp', 'repnc', 'jahf', 'bsf', 'fldl2t', 'jl', 'scasb', 'fsetpm', 'add', 'cmpsw', 'jge', 'fmul', 'dec', 'fcmovbe', 'neg', 'popa', 'jnae', 'jb', 'lodsb', 'cwd', 'lea', 'movs', 'setz', 'fsqrt', 'fcmovnu', 'rep', 'movzx', 'repc', 'fnop', 'movsx', 'hlt', 'fdecstp', 'into', 'loop', 'cmpxchg', 'jecxz', 'cmovs', 'fisubr', 'cmc', 'je', 'jnge', 'fcomip', 'stosw']
	
		# print(cmd)
		# os.system("pause")
	
	path= now_pwd + '/asm'

	for file in os.listdir(path):
		for filename in tqdm(os.listdir(path+'/'+file),desc=file):
			#print(root)
			#print(file,filename)
			pre(now_pwd, file,filename,cmd)

