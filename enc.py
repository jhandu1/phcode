# author : @Syhrularv_
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
good = G + '[' + W + '√' + G + '] '
bakekok = R + '[' + W + '!' + R + ']'

banner = """
{}         _nnnn_{}        _________________
{}        dMMMMMb{}      |                 |
{}       @p~qp~~qMb{}   ._| {}bash phcode {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}JM|{}_/
{}      JS^{}\__/{}  qKL
     dMM        MMMb
    dMM          MMMb
   MMM            MMMb
   MMM            MMMM    {}Coded by {}: {}pensiunanhacker
{}   MMM            MMMM    {}YT       {}: {}pensiunanhacker
{} __|'\ .        |\{}dS qML
{} |    `.       | `' \{}Zq
{}_)      \.{}___.{},|     .'
\____   ){}MMMMMM{}|   .'
     `-'       `--'
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} Encript      {}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dec1():
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

       os.system("touch ph1234.sh")
       os.system("bash " + out + " > ph1234.sh")
       os.remove(out)
       os.rename("ph1234.sh", out)
       print (good + "Done..")

   except KeyboardInterrupt:
       print (bakekok + " Stopped!")
   except IOError:
       print (bakekok + " File Not Found!")

def enc1():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (good + "Done..")
   except KeyboardInterrupt:
       print (bakekok + " Stopped!")
   except IOError:
       print (bakekok + " File Not Found!")


code1 = raw_input(W + "Choose" + G + " > ")

if code1 == "1" or code1 == "01":
   enc1()
elif code1 == "2" or code1 == "02":
   dec1()
else:
   print (bakekok + " Wrong input")
