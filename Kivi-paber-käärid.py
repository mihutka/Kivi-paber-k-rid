import random
while True:
 print("Игра камень-ножница-бумага")
 print ("Выбери режим игры:")
 print("Игрок и робот - цифра 1")
 print("Игрок и игрок - цифра 2")
 print("Выйти из игры - цифра 3")
 rezim_igri = int(input("Напишите цифру: "))
 if rezim_igri == 1:
    print("Вы выбрали режим игры с роботом")
    rounds = int (input("Выберите количество раундов: "))
    igrok1_result = 0
    robot_result = 0
    draw_result = 0
    results = []
    for i in range (1, rounds + 1):
     list_igri = ["камень", "ножницы" , "бумага"]
     print("Раунд: " + str(i))
     print("Выберите камень, ножницы или бумагу")
     igrok1 = str(input(""))
     robot_choice = random.choice(list_igri)
     print("Робот выбрал: " + str(robot_choice))
     if (igrok1 == "камень" and robot_choice == "ножницы") or \
       (igrok1 == "ножницы" and robot_choice == "бумага") or \
       (igrok1 == "бумага" and robot_choice == "камень"):
        print ("Вы победили робота")
        igrok1_result += 1
        
     elif igrok1 == robot_choice:
        print("Ничья")
        draw_result += 1
     else:
        print("Вы проиграли")
        robot_result += 1
    
    results.append(("Проигранные раунды", robot_result))
    results.append(("Выигранные раунды", igrok1_result))
    results.append(("Ничья", draw_result ))
    print(results)
 elif rezim_igri == 2:
   print("Вы выбрали режим игры с двумя игроками")
   name1 = str(input("Введите имя первого игрока: "))
   name2 = str(input("Введите имя второго игрока: "))
   rounds = int(input("Выберите количество раундов: "))
   name1_result = 0
   name2_result = 0
   draw_result = 0
   results = []
   for a in range (1, rounds + 1):
      list_igri = ["камень", "ножницы", "бумага"]
      print("Раунд" + str(a))
      print("Ход первого игрока, выберите камень, ножницы, или бумагу")
      igrok1 = str(input(""))
      print("Ход второго игрока, выберите камень, ножницы, или бумагу")
      igrok2 = str(input(""))
      if (igrok1 == "камень" and igrok2 == "ножницы") or \
       (igrok1 == "ножницы" and igrok2 == "бумага") or \
       (igrok1 == "бумага" and igrok2 == "камень"):
        print ("Победил первый игрок")
        name1_result += 1
        
      elif igrok1 == igrok2:
        print("Ничья")
        draw_result += 1
      else:
        print("Победил второй игрок")
        name2_result += 1
   results.append(("Победы первого игрока:", name1 , name1_result))
   results.append(("Победы второго игрока:" , name2 , name2_result))
   results.append(("Ничья", draw_result))
   print(results)
 elif rezim_igri == 3:
        print("Выход из игры.")
        break
 else:
     print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
      
      
   
   


    
       
        

    
    
    
    