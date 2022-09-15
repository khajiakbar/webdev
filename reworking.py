# yosh = int(input("yoshinizni kuriting= "))
#
# if yosh < 3:
#     print("kichkina bolalarga tekin")
# elif yosh >= 12:
#     print("bolalarga 15min")
# elif yosh > 60:
#     print('sizga kirish tekin')

kun = input('Bugungi kun ')
harorat = float(input('Havo harorati '))

if (kun.lower()== 'yakshanba' or kun.lower()=='shanba') and harorat >= 30:
    print("Cho'milgani ketdik")
elif(kun.lower()== 'yakshanba' or kun.lower()=='shanba') and harorat < 30:
    print('havo sovuq uyda qolamiz')
else:
    print('ish kuni')
    