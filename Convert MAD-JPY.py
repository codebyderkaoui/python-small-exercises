option = input("choose:\n 1: MAD to JPY\n 2: JPY to MAD\n")
if option == "1":
   txt = input("MAD: ")
   mad = int(txt)
   jpy = mad * 15.33
   print("JPY:",jpy)
elif option == "2":
   txt = input("JPY: ")
   jpy = int(txt)
   mad = jpy * 0.065
   print("MAD:",mad)
else:
    print("error")