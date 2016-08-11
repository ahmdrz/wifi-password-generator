# wifi-password-generator
### a smart wifi password generator
### Written in python

This projects use iwlist.py , see full source code in <a href="https://github.com/iancoleman/python-iwlist">python-iwlist</a>

<a href="https://github.com/iancoleman">@iancoleman</a>

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


# License 

#### MIT License
#### Copyright (c) 2016 Ahmadreza zibaei

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
