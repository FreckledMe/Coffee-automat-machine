Automat={
    'Cappuccino':
        {
            'Water':50,'Milk':25,'Coffee':15,'Sugar':10,'Cost':17
        },
    'Latte':
        {
            'Water':60,'Milk':15,'Coffee':10,'Sugar':15,'Cost':9
        },
    'Americano':
        {
            'Water':45,'Milk':30,'Coffee':20,'Sugar':10,'Cost':20
        },
    'Espresso':
        {
            'Water':100,'Milk':25,'Coffee':25,'Sugar':10,'Cost':30
        },
    'HotWater':
        {
            'Water':100,'Cost':5
        },
    'Reserve':
        {
            'Water':500,'Milk':400,'Coffee':30,'Sugar':450
        },
    'Bank':
        {
            1:10,2:15,5:20,10:40
        }
}

def order(a):
    for i in Automat['Reserve'].keys():
        if i ==0:
            print('Uzr menda coffee tayyorlashga massalliq qolmadi')
            break
    while True:
        if a ==1:
            print('Siz Cappuccino tanladingiz!Cappuccino narxi 17 sum')
            print('Pul kiriting:\n')
            pul=int(input())
            y=True

            while y:

                if pul == Automat['Cappuccino']['Cost']:
                    Automat['Reserve']['Water']-=Automat['Cappuccino']['Water']
                    Automat['Reserve']['Coffee']-=Automat['Cappuccino']['Coffee']
                    Automat['Reserve']['Milk']-=Automat['Cappuccino']['Milk']
                    Automat['Reserve']['Sugar']-=Automat['Cappuccino']['Sugar']
                    Automat['Bank'][10]+=1
                    Automat['Bank'][5]+=1
                    Automat['Bank'][2]+=1
                    print('Mana sizga Cappuccino.Yoqimli ishtaha!')
                    print(retry())
                    y = False

                elif pul > Automat['Cappuccino']['Cost']:
                    x=pul-Automat['Cappuccino']['Cost']
                    buyurtma = 'Cappuccino'
                    print(remainder(x,pul,buyurtma))
                    y=False
                else:
                    print('Pulingiz yetmadi!')
                    print('Yana pul kiritish uchun 1 ni bosing')
                    print('Pulinggizni qaytib olish uchun 0 ni bosing')
                    while True:
                        sign = int(input())
                        if sign == 1:
                            pul+=int(input('Pul kiriting'))
                            break
                        elif sign == 0:
                            print('Mana pulinggiz',pul)
                            y = False
                            print(retry())
                            break
                        else:
                            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")


            else:
                continue
        elif a ==2:
            print('Siz Latte tanladingiz!Latte narxi 9 sum')
            print('Pul kiriting:\n')
            pul=int(input())
            y=True

            while y:
                if pul == Automat['Latte']['Cost']:
                    Automat['Reserve']['Water']-=Automat['Latte']['Water']
                    Automat['Reserve']['Coffee']-=Automat['Latte']['Coffee']
                    Automat['Reserve']['Milk']-=Automat['Latte']['Milk']
                    Automat['Reserve']['Sugar']-=Automat['Latte']['Sugar']
                    Automat['Bank'][5]+=1
                    Automat['Bank'][2]+=2
                    print('Mana sizga Latte.Yoqimli ishtaha!')
                    print(retry())
                    y=False


                elif pul > Automat['Latte']['Cost']:
                    x = pul - Automat['Latte']['Cost']
                    buyurtma ='Latte'
                    print(remainder(x, pul,buyurtma))
                    y = False
                else:
                    print('Pulingiz yetmadi!')
                    print('Yana pul kiritish uchun 1 ni bosing')
                    print('Pulinggizni qaytib olish uchun 0 ni bosing')
                    while True:
                        sign = int(input())
                        if sign == 1:
                            pul+=int(input('Pul kiriting'))
                            break
                        elif sign == 0:
                            print('Mana pulinggiz',pul)
                            y = False
                            # print(retry())
                            break
                        else:
                            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")
            else:
                continue
        elif a ==3:
            print('Siz Americano tanladingiz!Americano narxi 20 sum')
            print('Pul kiriting:\n')
            pul=int(input())
            y=True

            while y:
                if pul == Automat['Americano']['Cost']:
                    Automat['Reserve']['Water']-=Automat['Americano']['Water']
                    Automat['Reserve']['Coffee']-=Automat['Americano']['Coffee']
                    Automat['Reserve']['Milk']-=Automat['Americano']['Milk']
                    Automat['Reserve']['Sugar']-=Automat['Americano']['Sugar']
                    Automat['Bank'][10]+=2
                    print('Mana sizga Americano.Yoqimli ishtaha!')
                    print(retry())
                    y=False


                elif pul > Automat['Americano']['Cost']:
                    x = pul - Automat['Americano']['Cost']
                    buyurtma = 'Americano'
                    print(remainder(x, pul,buyurtma))
                    y = False

                else:
                    print('Pulingiz yetmadi!')
                    print('Yana pul kiritish uchun 1 ni bosing')
                    print('Pulinggizni qaytib olish uchun 0 ni bosing')
                    while True:
                        sign = int(input())
                        if sign == 1:
                            pul += int(input('Pul kiriting'))
                            break
                        elif sign == 0:
                            print('Mana pulinggiz', pul)
                            y = False
                            print(retry())
                            break
                        else:
                            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")

            else:
                continue
        elif a ==4:
            print('Siz Espresso tanladingiz!Espresso narxi 30 sum')
            print('Pul kiriting:\n')
            pul=int(input())
            y=True

            while y:
                if pul == Automat['Espresso']['Cost']:
                    Automat['Reserve']['Water']-=Automat['Espresso']['Water']
                    Automat['Reserve']['Coffee']-=Automat['Espresso']['Coffee']
                    Automat['Reserve']['Milk']-=Automat['Espresso']['Milk']
                    Automat['Reserve']['Sugar']-=Automat['Espresso']['Sugar']
                    Automat['Bank'][10]+=3
                    print('Mana sizga Espresso.Yoqimli ishtaha!')
                    print(retry())
                    y=False

                elif pul > Automat['Espresso']['Cost']:
                    x = pul - Automat['Espresso']['Cost']
                    buyurtma = 'Espresso'
                    print(remainder(x, pul,buyurtma))
                    y = False
                else:
                    print('Pulingiz yetmadi!')
                    print('Yana pul kiritish uchun 1 ni bosing')
                    print('Pulinggizni qaytib olish uchun 0 ni bosing')
                    while True:
                        sign = int(input())
                        if sign == 1:
                            pul += int(input('Pul kiriting'))
                            break
                        elif sign == 0:
                            print('Mana pulinggiz', pul)
                            y = False
                            print(retry())
                            break
                        else:
                            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")

            else:
                continue
        elif a ==0:
            print('Siz issiq suv  tanladingiz!Issiq suv narxi 5 sum')
            print('Pul kiriting:\n')
            pul=int(input())
            y=True

            while y:
                if pul == Automat['HotWater']['Cost']:
                    Automat['Reserve']['Water']-=Automat['HotWater']['Water']
                    Automat['Bank'][5]+=1
                    print('Mana sizga issiq suv.Yoqimli ishtaha!')
                    print(retry())
                    y=False

                elif pul > Automat['HotWater']['Cost']:
                    x = pul - Automat['HotWater']['Cost']
                    buyurtma = 'issiq suv'
                    print(remainder(x, pul,buyurtma))
                    y = False
                else:
                    print('Pulingiz yetmadi!')
                    print('Yana pul kiritish uchun 1 ni bosing')
                    print('Pulinggizni qaytib olish uchun 0 ni bosing')
                    while True:
                        sign = int(input())
                        if sign == 1:
                            pul += int(input('Pul kiriting'))
                            break
                        elif sign == 0:
                            print('Mana pulinggiz', pul)
                            y=False
                            print(retry())
                            break
                        else:
                            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")
            else:
                continue
        else:
            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")
def retry():
    for i in Automat['Reserve'].keys():
        if i ==0:
            print('Uzr menda coffee tayyorlashga massalliq qolmadi')
            break
    print('Cappuccino ichish uchun 1 ni bosing')
    print('Latte ichish uchun 2 ni bosing')
    print('Americano ichish uchun 3 ni bosing')
    print('Espresso ichish uchun 4 ni bosing')
    print('Issiq suv ichish uchun 0 ni bosing')
    a=int(input())
    print(order(a))
def remainder(k,pul,buyurtma):
    for i in Automat['Reserve'].keys():
        if i ==0:
            print('Uzr menda coffee tayyorlashga massalliq qolmadi')
            break
    j = k
    if k >= 10:
        if Automat['Bank'][10] < k//10:
            pass
        else:
            Automat['Bank'][10] -= k//10
            k -= k//10*10
    if k >= 5:
        if Automat['Bank'][5] < k//5:
            pass
        else:
            Automat['Bank'][5] -= k//5
            k -= k//5*5
    if k >= 2:
        if Automat['Bank'][2] < k//2:
            pass
        else:
            Automat['Bank'][2] -= k//2
            k -= k//2*2
    if k >= 1:
        if Automat['Bank'][1] < k:
            pass
        else:
            Automat['Bank'][1] -= 0
            k = 0
    if k == 0:
        print('Qolgan pulingiz:',j,'\n')
        print(retry())
    else:
        while True:
            for i in Automat['Reserve'].keys():
                if i == 0:
                    print('Uzr menda coffee tayyorlashga massalliq qolmadi')
                    break
            print('Menda ayni damda qaytimga pul yetarli emas!')
            print('Qaytiminggizga boshqa coffee taklif etishim uchun 1 ni bosing')
            print('Buyurtmani bekor qilib pulingizni qaytib olish uchun 0 ni bosing')
            a=int(input())
            if a == 1:
                '''Qaytimga boshqa narsa taklif etish algoritmi'''
                satr = []
                if k > Automat['Cappuccino']['Cost']:
                    satr.append('Cappuccino')
                if k > Automat['Latte']['Cost']:
                    satr.append('Latte')
                if k > Automat['Americano']['Cost']:
                    satr.append('Americano')
                if k > Automat['Espresso']['Cost']:
                    satr.append('Espresso')
                if k > Automat['HotWater']['Cost']:
                    satr.append('HotWater')
                if satr == []:
                    print('Uzr qaytiminggiz hech nimaga yetmadi!')
                    print("Qaytimga rozi bo'lsanggiz 1 ni bosing")
                    print("Qaytimni qaytarib olmoqchi bo'lsanggiz buyurtmani bekor qilib hamma pulinggizni qaytarib berishimga to'g'ri keladi")
                    print("Chunki menda bu buyurtmadan qolga qaytimni berishiga yetarli summa yoki kupyura yo'q")
                    print("Buyurtmani bekor qilib hamma pulinggizni qaytarib olish uchun  ni bosing")
                    while True:
                        belgi = int(input())
                        if belgi == 1:
                            print(f'Mana buyurtmanggiz {buyurtma}.')
                            break
                        elif belgi == 0:
                            print('Buyurtma bekor qilindi!\nMana hamma pulingiz',pul)
                            break
                        else:
                            print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")
                else:
                    print(f'Men sizga {i for i in satr} larni taklif qila olaman')
                    if 'Cappuccino' in satr:
                        print('Cappuccino ichish uchun 1 ni bosing')
                    if 'Latte' in satr:
                        print('Latte ichish uchun 2 ni bosing')
                    if 'Americano' in satr:
                        print('Americano ichish uchun 3 ni bosing')
                    if 'Espresso' in satr:
                        print('Espresso ichish uchun 4 ni bosing')
                    if 'HotWater' in satr:
                        print('Issiq suv ichish uchun 0 ni bosing')
                    z = int(input())
                    print(order(z))
                    break
            elif a == 0:
                print('Mana hamma pulingiz',pul)
                print(retry())
                break
            else:
                while True:
                    print("Noto'g'ri raqam kiritdingiz!Qaytadan raqam kiriting:\n")
                    continue

print(retry())
