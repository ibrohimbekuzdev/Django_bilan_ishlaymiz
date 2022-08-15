# a1 = int(input("raqam kiriting : "))
# a2 = int(input("raqam kiriting : "))
# a3 = int(input("raqam kiriting : "))
# if a1 > a2 :
#     print(f"2-kiritgan soninggiz kichkina : {a2}")
# elif a3 > a1 :
#     print(f"1-kiritgan sonning kichkina : {a1} ")
# elif a2 > a3:
#     print(f"3-kiritgan soninggiz kichkina : {a3}")
# else:
#     print(f"uchala son ham teng : birinch son :{a1} ikkinch son {a2} uchinchi son {a3}")


# a = {11,22,33,44,55,66,77,88,99}
# a0 = {11,22,33,44,55,66,77,88,99}
#
# print(type(a) , a)
# a1 = [11,22,33,44,55,66,77,88,99]
# a2 = [99,88,77,66,55,44,33,22,11]
# '''a.add apendga oxshash funcsiya set ishlash uchun'''
# '''a.remove 1 raqam bita soz qilib beradigan funksiya '''
# '''a.pop tasadifiy o`chirish yoki ixtiyoriy uchirish '''
# '''a.clear hamma sini uchirish bittada hammasini uchirish uchun'''
# '''a.union setlarni birbiriga qo`shish funksiyasi union belgisi ^ '''
# """ ikkila set ni qoshib ichida gi 2ta birhil malumotlarni ekranga chiqarish chiqarish: yozilishi intersection"""
# '''&  z = y.difference()'''
# '''difference_uptade() uzlashtirish'''
#







# name1 = {'ibrohim','raximjanov','python','pycharm','jasur'}
# name = {1,2,3,4,5,6,7,8,9}
# name.add(10)
# name.add(11)
# name.add(12)
# name.add(13)
# name.add(14)
# name.add(15)
# print(name)
# name.pop()
# name.pop()
# name.pop()
# name.pop()
# name.pop()
# name.pop()
# name.pop()
# name.pop()
# name.pop()
# name1.remove('pycharm')
# print(name1)
# name1.remove('python')
# print(name1)
# name1.remove('raximjanov')
# name.discard("Jasur")
# print(name1)
# name.clear()
# print(name)
# name1.clear()
# print(name1)
#
# for i in name:
#    print(i)
# for z in name1:
#     print(z)
#
#
#
#
#
# namea = {1, 3, 11, 6, 20}
# nameb= {1, 3, 13, 15, 18}
#
# a = namea.union(nameb)
# b = namea | nameb
# print(a,'\n',b)
#
#
# a = namea.intersection(nameb)
# b = namea & nameb
# print(a,b)
#
#
# a = nameb.difference(name1)
# b = nameb - namea
# print(b)
#
# a = nameb.symmetric_difference(namea)
# b = name1 ^ namea






thisisdict = {
    'rangi': 'oq',
    'model': 'malibu',
    'yil': 2022,
    'narx': 4400

}
# print(type(thisisdict.get('rangi')))
# thisisdict['rangi'] = 'ko`k'
# thisisdict['yil'] = 2020
# '''values() qiymat bilan ishlash va keys() kalit bilan ishlash yoki qiymat ,kalit bilan birga ishlash'''
# for i in thisisdict.keys():
#     print(i)
#
# for i, j in thisisdict.items():
#     print(f"{i} : {j}")


# thisisdict['yurgani'] = '5555 k/m'
# print('''o`zgartirish tugrirogi qo`shish''',thisisdict)
# thisisdict.pop('rangi')
# print(thisisdict)
#
# del thisisdict['model']
# print(thisisdict)
# thisisdict.popitem()
# print(thisisdict)  ,'''discovryni  oxirgi  elmentni  o`chiradi'''
# print(thisisdict,thisisdict.clear())

# avto = {
#     'Viloyat': 'nomongon',
#     'bolalar': {
#         'ism': "ibrohim",
#         'familya': 'raximjanov1704',
#         'sharif': 'ULUG`BEK O`gli'
#     },
#     'Markaz': 'Namangan',
#     'maktablar':{
#         '1-MIKRAYON': '56-maktab',
#         '2-MIKRAYON': '48-maktab'
#     },
#     "bog'chalar": [13,31,23,55]
# }
# z = avto['bolalar']
# x = z['familya']
# print(x)




# avto = {
#     'malumoti':"xaqida",
#     'model': 'malibu',
#     'rang': 'qora',
#     'yili': '2017',
#     'yurgani' : 1500
# }
# avto.pop("yili")
# print(avto)
# avto.popitem()
#
#
# del avto["rang"]
# print(avto)
# avto['sotiladi'] = '5000'
# print(avto)
# print(avto.get("model"))

a = str(input("maxsulot kiriting : "))
b = {
    'anor':10000,
    'qulupnay':12000,
    'olma':5000
}
if a=="anor":
    print(b.get('anor'))
elif a=="qulupnay":
    print(b.get('qulupnay'))
elif a=="olma":
    print(b.get("olma"))

























