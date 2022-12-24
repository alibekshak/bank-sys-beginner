
# baza = {
#     "login1" : {
#         "phone" : "+77071232323",
#         "name" : "Jon",
#         "balance" : 9999, 
#         "password" : "123qweasd"
#     }, 
#     "login2" :{
#         "phone" : "+77776883221",
#         "name" : "Nik",
#         "balance" : 9350, 
#         "password" : "123QWEASD"
#     }
# }

# m = None

# while True:
#     if m is None:
#         print(" Добро пожаловать! ")
#         a = int(input("""
#         1 - Зарегистрироваться
#         2 - Авторизоваться
#         3 - Перевод баланса
#         4 - Список пользователей
#         5 - Информация
#         6 - Номер телефона   
#         7 - Выйти
#         Выберите операцию:
#     """))
#     if a == 1:
#         login = input("Введите логин: ")
#         name = input("Введите имя: ")
#         phone = input("Введите номер телефона: ")
#         password = int(input("Введите пароль: "))
#         password1 = int(input("Введите пароль повторно: "))
#         while password != password1 or len(password) < 8:
#             password = input("Создать пароль не меньше 8:")
#             password1 = input("Повтарите свой пароль")
#         else:
#             baza.update({
#                 login: {
#                     "phone" : phone,
#                     "name" : name,
#                     "balance" : 1000,
#                     "password" : password
#                 }
#             })
#             print(baza)
   
#     elif a == 2:
#         if m is None:
#             login = input("Введите логин: ")
#             password = int(input("Введите пароль: "))
#             if login in baza.keys and password == baza[login]["password"]:
#                 print("Вы авторизованы")
#             else:
#                 print("Неверный логин или пароль")

#     elif a ==3:
#         if m is not None:
#                 sum = str(input("Введите сумму: "))
#                 if sum < baza[login]["balance"]:
#                     logbalans = input("Введите логин получателя: ")
#                     if logbalans in baza[login]:
#                         sum += logbalans["balance"]
#                         print(logbalans["balance"])

#                     else:
#                         print("Такого логина не существует")
                
#                 else:
#                     print("Сумма перевода превышает Ваш текуший баланс")


#     elif a == 4:
#         login = input("Введите логин: ")
#         password = int(input("Введите пароль: "))
#         if login in baza.keys and password == baza[login]["password"]:
#             print(baza[login]["name"])
#         else:
#             print("Неверный логин или пароль")


#     elif a == 5:
#         login = input("Введите логин: ")
#         password = int(input("Введите пароль: "))
#         if login in baza.keys() and password == baza[login]["password"]:
#             print(baza.keys())
#         else:
#             print("Неверный логин или пароль")

#     elif a == 6:
#         login = input("Введите логин: ")
#         password = int(input("Введите пароль: "))
#         if login in baza.keys() and password == baza[login]["password"]:
#             print(baza[login]["phone"])
#         else:
#             print("Неверный логин или пароль")

#     elif a ==7:
#         print("До скорой встречи")
#         break