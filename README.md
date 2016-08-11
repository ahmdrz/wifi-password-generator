# wifi-password-generator
### a smart wifi password generator

This projects use iwlist.py , see full source code in <a href="https://github.com/iancoleman/python-iwlist">python-iwlist</a>


gpass is a projects that use essid and mac address of selected wifi to generate a smart password for login into wireless network or router admin panel.

* easy to use
* automatically generated passwords
* smart
* need to improve

```
>>> python gpass.py 
gpass.py -i <interface> -e <essid> [-m <minsize>]
>>> python gpass.py -i wlp9s0 -e Aiden
Program started ! Scaning...

End of program , 42756 generated ! codes are in output25750.txt
>>> head -n 10 output25750.txt 
0Aiden
Aiden0
00Aide
Aide00
00Aiden
Aiden00
00iden
iden00
001Aid
Aid001
...
A00183
00183Ai
Ai00183
00183Aid
Aid00183
00183Aide
Aide00183
00183Aiden
Aid****183
00183i
i00183
00183id
id00183
00183ide
ide00183
00183iden
iden00183
00183d
d00183
...
18***32*3den
den1839**2*3
1839**2*3e
e18398****
```
