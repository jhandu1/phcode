# author : @pensiunanhacker
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
NICE = G + '[' + W + '√' + G + '] '
UNLUCKY = R + '[' + W + '!' + R + ']'

banner = """
{}         _xxxx_{}        _________________
{}        xxxxxxxx{}      |                 |
{}       @p~qp~~qMb{}   ._| {}Bash phencdec {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}JM|{}_/
{}      JS^{}\__/{}  qKL
     xXX        xXXx
    xXX          xXXx
   xXX            XXXx
   XXX            XXXX    {}Coded by {}: {}pensiunanhacker
{}  XXX            XXXX    {}Teleg       {}: {}pensiunanhacker
{} __|'\ .        |\{}pH xXX
{} |    `.       | `' \{}Xx
{}_)      \.{}___.{},|     .'
\____   ){}RRRRR{}|   .'
     `-'       `--'
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} ENC      {}[{}2{}]{} DEC
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch p1234.sh")
       os.system("bash " + out + " > p1234.sh")
       os.remove(out)
       os.rename("p1234.sh", out)
       print (NICE + "Done..")

   except KeyboardInterrupt:
       print (UNLUCKY + " ❌")
   except IOError:
       print (UNLUCKY + " not found🔭")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-FVCK " + script + " -o " + output )
       print (NICE + "Done..")
   except KeyboardInterrupt:
       print (UNLUCKY + " 💢")
   except IOError:
       print (UNLUCKY + " ❌")


penhack = raw_input(W + "Choose" + G + " > ")

if penhack == "1" or penhack == "01":
   enkrip()
elif penhack == "2" or penhack == "02":
   dekrip()
else:
   print (UNLUCKY + " ❌")
