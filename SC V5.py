def Calc():

  while True:
      
      num1 = input('(Press q to quit / h for history) First number: ')
      if num1 == 'q':
        result = 'stop'
        print('Calculator closed, reopen to use again')
        break

      elif num1 == 'h':
        for calculation in history:
          print(calculation)
        continue

      try:
        num1 = float(num1)
      except:
        print('Invalid number')
        return
        
      opr = input('Operation? (+,-, *, /, ^, %): ')
      if opr not in ['+', '-', '*', '/', '^', '%']:
        print('Invalid operator')
        return
      
      try:
        num2 = float(input('Second number: '))
      except:
        print('invalid number')
        return
      
      if opr == '+':
          sol = num1 + num2
          print(f'{num1} + {num2} = {sol}')
          history.append(f'{num1} {opr} {num2} = {sol}')
      
      elif opr == '-':
          sol = num1 - num2
          print(f'{num1} - {num2} = {sol}')
          history.append(f'{num1} {opr} {num2} = {sol}')
      
      elif opr == '*':
          sol = num1 * num2
          print(f'{num1} x {num2} = {sol}')
          history.append(f'{num1} {opr} {num2} = {sol}')
      
      elif opr == '/':
          if num2 == 0:
              print("Undefined")
          else:
              sol = num1 / num2
              print(f'{num1} ÷ {num2} = {sol}')
              history.append(f'{num1} {opr} {num2} = {sol}')
      
      elif opr == '^':
          sol = num1 ** num2
          print(f'{num1} ^ {num2} = {sol}')
          history.append(f'{num1} {opr} {num2} = {sol}')
      
      elif opr == '%':
          if num2 == 0:
              print("Undefined")
          else:
              sol = num1 % num2
              print(f'{num1} % {num2} = {sol}')
              history.append(f'{num1} {opr} {num2} = {sol}')

history = []

Calc()