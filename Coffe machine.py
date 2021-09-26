coffee = {
    'Reserve': {
        'shakar': 3000,
        'shokolad': 3000,
        'sut': 5000,
        'suv': 5000,
        'Americano': 2000,
        'Latte': 2000,
        'Espresso': 2000,
        'Cappucino': 2000
    },
    'Tangalar': {
        '100': 0,
        '50': 0,
        '10': 0
    },
    'Qahvalar': {
        'Americano': 3000,
        'Latte': 4000,
        'Cappucino': 4000,
        'Espresso': 3000,
    },
    'Americano': {
        'shokolad': 30,
        'Americano': 30,
        'suv': 150,
        'shakar': 10,
        'narxi': 150
    },
    'Latte': {
        'shokolad': 30,
        'Latte': 20,
        'suv': 50,
        'sut': 100,
        'shakar': 10,
        'narxi': 160
    },
    'Cappucino': {
        'shokolad': 50,
        'Cappucino': 40,
        'suv': 20,
        'sut': 100,
        'shakar': 10,
        'narxi': 180
    },
    'Espresso': {
        'Espresso': 30,
        'shokolad': 50,
        'sut': 100,
        'shakar': 15,
        'narxi': 200
    }
}


def qaytim_tanga(pul):
    print()
    for i in coffee['Tangalar'].keys():
        if pul >= int(i):
            if coffee['Tangalar'][i] - pul // int(i)<0:
                pul -= coffee['Tangalar'][i]
                coffee['Tangalar'][i] = 0
                continue
            print(i + " so'mlik", pul // int(i))
            coffee['Tangalar'][i] -= pul // int(i)
            pul -= pul // int(i) * int(i)


def tekshir(kofe, shakar):
    for i in coffee[kofe].keys():
        if i == 'narxi':
            continue
        if i == 'shakar' and shakar and coffee['Reserve'][i] - coffee[kofe][i] >= 0:
            continue
        if i == 'shakar' and not shakar and coffee['Reserve'][i] - coffee[kofe][i] <= 0:
            continue
        if coffee['Reserve'][i] - coffee[kofe][i] <= 0:
            return False
    return True


def ayir(pul, kofe, shakar):
    for i in coffee[kofe].keys():
        if i == 'narxi':
            pul -= coffee['Qahvalar'][kofe]
            continue
        if not shakar and i == 'shakar':
            continue
        coffee['Reserve'][i] -= coffee[kofe][i]
    print(kofe + ' tayyor.Yoqimli ishtaha')


def qaytim(pul):
    tanga = pul
    for i in coffee['Tangalar'].values():
        if tanga >= i:
            tanga -= tanga // i * i
    if tanga != 0:
        print('Menda ' + str(tanga) + ' pul yetmayapti')
        a = int(input('1.Qolgan pulga roziman\n0.Hamma pulni qaytarib olish va buyurtmani bekor qilish\n'))
        return a
    return 1


def qolgan_pul(pul, kofe):
    s = 0
    for i in coffee['Qahvalar'].values():
        if pul >= i:
            s += 1
    if s == 0:
        tanga = pul
        for i in coffee['Tangalar'].keys():
            if tanga >= int(i):
                tanga -= tanga // int(i) * int(i)
        if tanga != 0:
            print('Menda ' + str(tanga) + ' pul yetmayapti')
            s = int(input('1.Qolgan pulga roziman\n0.Hamma pulni qaytarib olish va buyurtmani bekor qilish\n'))
            if s == 1:
                print(kofe + ' tayyor yoqimli ishtaha')
                print('Mana pulinggiz: ')
                qaytim_tanga(pul - tanga)
            else:
                print('Mana qolgan pulingiz: ')
                qaytim_tanga(pul)
        else:
            print('Mana qolgan pulinggiz: ')
            qaytim_tanga(pul)
        print(coffee)
        main()
    else:
        print('1.Qaytimni qaytarib olish\n2.Qaytimga boshqa narsa taklif qilaman')
        while 1:
            c = int(input())
            if c == 1:
                print('Mana qolgan pulinggiz: ')
                qaytim_tanga(pul)
                print(coffee)
                main()
                break
            elif c == 2:
                taklif(pul)
                print(coffee)
                main()
                break
            else:
                print("Noto'g'ri raqam kiritdinggiz.qaytadan urinib ko'ring")


def taklif(pul):
    tartib = 1
    yangi_royxat = []
    print('Qaytimga shularni taklif qila olaman')
    for i in coffee['Qahvalar'].keys():
        if pul >= coffee['Qahvalar'][i]:
            print(str(tartib) + '.' + i)
            tartib += 1
            yangi_royxat.append(i)
    while 1:
        nomer = int(input('Mos raqamni kiriting: '))
        if 1 <= nomer <= tartib:
            break
        else:
            print("Noto'g'ri raqam kiritdinggiz.Qaytadan urinib ko'ring")
    for i in coffee[yangi_royxat[nomer - 1]].keys():
        if i == 'narxi':
            pul -= coffee['Qahvalar'][yangi_royxat[nomer - 1]]
            continue
        coffee['Reserve'][i] -= coffee[yangi_royxat[nomer - 1]][i]
    print(yangi_royxat[nomer - 1] + ' tayyor.Yoqimli ishtaha')
    qolgan_pul(pul, kofe)


def takror(pul, kofe, shakar):
    hammasi = pul
    if pul == coffee['Qahvalar'][kofe]:
        if tekshir(kofe, shakar):
            ayir(pul, kofe, shakar)
            pul -= coffee['Qahvalar'][kofe]
            print(coffee)
            main()
        else:
            print('Uzr menda ' + kofe + ' tayyorlash uchun yetarlicha mahsulot mavjud emas')
            print('Boshqa qahva tanlab koring')
            main()
    elif pul < coffee['Qahvalar'][kofe]:
        print('Pulinggiz yetmadi\n1.Yana pul kiritish\n2.Buyurtmani bekor qilish va pulni qaytarib olish')
        while 1:
            b = int(input())
            if b == 1:
                print('Pul kiriting: ')
                for i in coffee['Tangalar'].keys():
                    a = int(input(i + " so'mlik "))
                    pul += a * int(i)
                takror(pul, kofe)
                break
            elif b == 2:
                print('Mana pulinggiz: ')
                qaytim_tanga(pul)
                print(coffee)
                main()
                break
            else:
                print("Noto'g'ri raqam kiritdinggiz.Qaytadan urinib ko'ring")

    elif pul > coffee['Qahvalar'][kofe]:
        if tekshir(kofe, shakar):
            pul -= coffee['Qahvalar'][kofe]
            ayir(pul, kofe, shakar)
            qolgan_pul(pul, kofe)
            qaytim_tanga(pul)
        else:
            print('Uzr menda ' + kofe + ' tayyorlash uchun yetarlicha mahsulot mavjud emas')
            print('Boshqa qahva tanlab koring')
            main()


def main():
    print('Qanday qahva ichmoqchisiz?')
    k = 1
    for i, j in zip(coffee['Qahvalar'].keys(), coffee['Qahvalar'].values()):
        print(f'{k}.{i} narxi {j} so\'m')
        k += 1
    print()
    while 1:
        mos = int(input('Mos raqamni kiriting: '))
        if 1 <= mos <= len(list(coffee['Qahvalar'].keys())):
            break
        else:
            print("Noto'g'ri raqam kiritdinggiz.qaytadan urinib ko'ring")
    print(list(coffee['Qahvalar'].keys())[mos - 1])
    pul = 0
    shakar = int(input('1.Shakarli\n0.Shakarsiz\n'))
    print('Pul kiriting: ')
    for i in coffee['Tangalar'].keys():
        a = int(input(i + " so'mlik "))
        coffee['Tangalar'][i] += a
        pul += a * int(i)
    kofe = list(coffee['Qahvalar'].keys())[mos - 1]
    takror(pul, kofe, shakar)
main()