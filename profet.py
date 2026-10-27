while 1==1:
  a = int(input("item cost: "))
  b = int(input("selling price: "))
  if a < b:
    print("profit")
    c = b - a
    print("The profit is:", c)
  elif a > b:
    print("loss")
    d = a - b
    print("The loss is:", d)
  else:
    print("no profit, no loss")