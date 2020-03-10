import msvcrt 

while True:
   n = ord(msvcrt.getch())
   if n == 224:
      key = ord(msvcrt.getch())
      print("SPECIAL: " + str(key))
   else:
      print(n)

