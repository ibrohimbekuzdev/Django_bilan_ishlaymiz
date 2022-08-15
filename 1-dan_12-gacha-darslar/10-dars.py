#  tuple malumotlar turi

a = (1,225,5847,887)
b = list(a)

print(b)
b.insert(1,2)
b.insert(2,3)

print(b)
c = tuple(b)

print(c)
d = list

yil = int(input("yil kiriting : "))

if yil % 4 == 0:
        if yil% 100 != 0 or yil  % 400 ==0:
            print("366 kun bor, kabisa yili")
        else:
               print('365 kun bor kabisa yili emas')
else:
     print("365 kun bor kabisa yili emas")
