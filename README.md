BrainFc: Conversion for almost any [Trivial brainfuck substitution](https://esolangs.org/wiki/Trivial_brainfuck_substitution) language.

# Usage
```commandline
python main.py <filename>
```
filename is a JSON file that cotains these keys:
1. cmd is a dictionary from brainfuck to the TBS
2. action is all the actions done by the interpreter

Examples:
```json
{
  "cmd": {
    "+": "-",
    "-": "+",
    ",": ".",
    ".": ",",
    "[": "]",
    "]": "[",
    ">": "<",
    "<": ">"
  },
  "delims": [],
  "actions": [
    ["frombf","++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."],
    ["tobf",".],.["],
    ["inter","------]<------------->+[<,<-----------]<---------->+[<-,-,+++++++++++,<-----]<--------->+[<-,"],
    ["tolang","------]<------------->+[<,<-----------]<---------->+[<-,-,+++++++++++,<-----]<--------->+[<-,","C.json"],
    ["totbs","------]<------------->+[<,<-----------]<---------->+[<-,-,+++++++++++,<-----]<--------->+[<-,","TINABD.json"]
  ]
}
```
This specifies [ReverseFuck](https://esolangs.org/wiki/ReverseFuck) in the 'cmd' key and do the following:
1. Convert the BF program `++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.` to ReverseFuck.
2. Convert the ReverseFuck program `.],.[` to BF.
3. Interpret the ReverseFuck program `------]<------------->+[<,<-----------]<---------->+[<-,-,+++++++++++,<-----]<--------->+[<-,`. 
4. Convert the ReverseFuck program `------]<------------->+[<,<-----------]<---------->+[<-,-,+++++++++++,<-----]<--------->+[<-,` to a non-esoteric language C (specified in C.json).
5. Convert the ReverseFuck program `------]<------------->+[<,<-----------]<---------->+[<-,-,+++++++++++,<-----]<--------->+[<-,` to the TBS esolang [THIS IS NOT A BRAINFUCK DERIVATIVE](https://esolangs.org/wiki/THIS_IS_NOT_A_BRAINFUCK_DERIVATIVE).

That's it, have fun! :D