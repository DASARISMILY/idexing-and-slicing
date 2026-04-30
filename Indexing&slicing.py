Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing

>>> #positive
>>> a="vijayawada"
>>> a[4]
'y'
>>> a[10]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[10]
IndexError: string index out of range
>>> a[0]
'v'
>>> a[7]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
>>> a="i am in codegnan"
>>> a[0]
'i'
>>> a[2]+a[3]
'am'
>>> a[1]
' '
>>> a[1]+a[4]+a[7]
'   '
>>> a[8]+a[9]+a[10]+a[11]
'code'
>>> 
>>> a="I love python"
>>> a[3]+a[4]+a[5]+a[6]
'ove '
>>> a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'
>>> a="vijayawada is a royal city"
'
>>> a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
>>> a[22]+a[23]+a24]+a[25]
SyntaxError: unmatched ']'
>>> a[22]+a[23]+a[24]+a[25]
'city'
>>> a[11]+a[12]
'is'
>>> 
>>> # Negative indexing
>>> a="vizag is a city of destiny"
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a[-1]+a[-2]+a[-3]+a[-4+a[-5]+a[-6]+a[-7] a[-1]+a[-2]+a[-3]+a[-4+a[-5]+a[-6]+a[-7]
                                                             
SyntaxError: '[' was never closed
SyntaxError: '[' was never closeda[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
                                                             
SyntaxError: invalid syntax
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
                                                             
'ynitsed'
a="codegnan it solutions"
                                                             
a[-1]+a[-2]+a[-3]+a[-4]+a[-4]+a[-6]+a[-7]
                                                             
'snoiiul'
'snoiiul'
                                                             
'snoiiul'
a[-12]+a[-11]
                                                             
'it'
a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
                                                             
'codegnan'
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
                                                             
'solutions'

# slicing
                                                             
a="codegnan"
                                                             
a[0:4]
                                                             
'code'
a[4:8]
                                                             
'gnan'
a[:4]
                                                             
'code'
a[4:]
                                                             
'gnan'
a[0:3]
                                                             
'cod'
a="work hard until you succeed"
                                                             
a[19:27]
                                                             
' succeed'
a[10:15]
                                                             
'until'
a[5:9]
                                                             
'hard'
a[[0:4]
  
SyntaxError: invalid syntax
a[0:4]
  
'work'
a[16:19]
  
'you'
a="i am learning pythin course"
  
a[14:20]
  
'pythin'
a[21:27]
  
'course'
a[5:13]
  
'learning'
a[2:4]
  
'am'
a[21:}
  
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[21:]
  
'course'
a[5:10]
  
'learn'
a[5:12]
  
'learnin'

#negative slicing
  
a="simple is better than ugly"
  
a[-7:]
  
'an ugly'
a[-20:-13]
  
' is bet'
a="simple is better than complex"
  
a[-7:]
  
'complex'
a[-20:-13]
  
' better'
a[-29:-23]
  
'simple'
a=beautiful is better than ugly"
  
SyntaxError: unterminated string literal (detected at line 1)
a="beautiful is better than ugly"
  
a[-29:-20]
  
'beautiful'
a[-4:]
  
'ugly'
a[-4:-1]
  
'ugl'
a[-4:0]
  
''
a[-19:-17]
  
'is'
