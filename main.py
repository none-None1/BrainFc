import json
import sys
def bf(code):
    s=[]
    matches={}
    tape=[0]*1000000
    for i,j in enumerate(code):
        if j=='[':
            s.append(i)
        if j==']':
            m=s.pop()
            matches[m]=i
            matches[i]=m
    cp=0
    p=0
    while cp<len(code):
        if code[cp]=='+':
            tape[p]=(tape[p]+1)%256
        if code[cp]=='-':
            tape[p]=(tape[p]-1)%256
        if code[cp]==',':
            ch=sys.stdin.read()
            tape[p]=(ord(ch) if ch else 0)%256
        if code[cp]=='.':
            print(chr(tape[p]),end='')
        if code[cp]=='<':
            p-=1
        if code[cp]=='>':
            p+=1
        if code[cp]=='[':
            if not tape[p]:
                cp=matches[cp]
        if code[cp]==']':
            if tape[p]:
                cp=matches[cp]
        cp+=1
def frombf(cmd,delims,src):
    dst=[]
    for i in src:
        if i in '+-,.[]><':
          dst.append(cmd[i])
    if delims:
        return delims[0].join(dst)
    else:
        return ''.join(dst)
def tobf(cmd,delims,src):
    p=0
    r=''
    while(p<len(src)):
        flag=False
        for i,j in cmd.items():
            if src[p:].startswith(j):
                r+=i
                p+=len(j)
                flag=True
        if not flag:
            for i in delims:
                if src.startswith(i):
                    p += len(i)
                    flag = True
            if not flag:
                p+=1
    return r
def bf2lang(bf,fn):
    dst=''
    with open(fn,"r",encoding="utf-8") as f:
        l=json.load(f)
    if 'b' in l:
        dst+=l['b']
    for i in bf:
        if i in '+-,.[]><':
            dst+=l[i]
    if 'e' in l:
        dst += l['e']
    return dst
def execute(fn):
    with open(fn,"r",encoding="utf-8") as f:
        l=json.load(f)
        cmd,delims=l['cmd'],l['delims']
    for i in l['actions']:
        print('Executing action: {}'.format(i))
        if i[0]=='frombf': # Converts from BF to TBS
            print(frombf(cmd,delims,i[1]))
        if i[0]=='tobf': # Converts from TBS to BF
            print(tobf(cmd,delims,i[1]))
        if i[0]=='inter': # Interprets TBS
            bf(tobf(cmd,delims,i[1]))
            print()
        if i[0]=='tolang': # Converts TBS to a non-esoteric language
            print(bf2lang(tobf(cmd,delims,i[1]),i[2]))
        if i[0]=='totbs': # Converts TBS to another TBS
            with open(i[2], "r", encoding="utf-8") as f:
                p=json.load(f)
                cmd2, delims2 = p['cmd'], p['delims']
            print(frombf(cmd2,delims2,tobf(cmd,delims,i[1])))

if __name__=='__main__':
    try:
        execute(sys.argv[1])
    except:
        print("Usage: python main.py <JSON filename>")