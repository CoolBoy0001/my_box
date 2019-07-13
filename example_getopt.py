import getopt
import sys
VERSION = "1.0.0"
def help():
   print("[*] Help info")
   print("[*] python %s -f 123.txt"%(sys.argv[0]))
   print("[*] python %s -h"%(sys.argv[0]))
   print("[*] python %s --help"%(sys.argv[0]))
   print("[*] python %s -v"%(sys.argv[0]))
   print("[*] python %s --version"%(sys.argv[0]))

def version():
    print("[*] Version is %s "%(VERSION))

def func():
     print("I am a  func")
def func_e():
     print("I am a  func_e")

'''
getopt.getopt:
    para1: sys.argv[1:]   para2: short_key  para3: long_key
    example: shrot_key: -h  long_key: --help
    para2: short_key(-h[if key with : then value cannot  be null  ])
'''
opts,args = getopt.getopt(sys.argv[1:],'-h,-v,-f:,-e:',['help','version','func:'])
print(opts)

for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        help()
        sys.exit()#for only help

    elif opt_name in ('-v','--version'):
        version()
        sys.exit()#for only help

    elif opt_name in ('-f','--func'):
        for i in range(int(opt_value)):
            print(i)
            func()

    elif opt_name in ('-e'):
        loop = int(opt_value)
        for i in range(loop):
            func_e()
sys.exit()
