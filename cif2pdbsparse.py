import sys
import os
pymolpath="YOURPATHTOPYMOL"
sys.path.append(pymolpath+"/lib/python3.6/site-packages/")
from pymol import cmd
f = open("pdblist", 'r')
pdblist=f.readlines()
f2 = open("hugesize.txt")
hugelist=f2.readlines()
for pdbname in pdblist:
    filename = pdbname.replace('\n', '')
    bname = os.path.basename(pdbname)
    hugename=bname.split(".")[0]+"\n"
    if (hugename in hugelist):
        print("Ignored because it's huge")
    else:
        cmd.delete("all")
        filename = pdbname.replace('\n', '')
        print(filename)
        cmd.load(filename)
        ad=cmd.get_chains("all")
        cmd.alter("all","type='ATOM'")
        for n in ad:
            nm=cmd.select("polymer.protein and chain "+n)
            if (nm>0):
                bname = os.path.basename(filename)
                #cmd.save(bname+"chain"+n+".pdb","sele")
                cmd.save(filename + "_chain" + n + ".pdb", "sele")
