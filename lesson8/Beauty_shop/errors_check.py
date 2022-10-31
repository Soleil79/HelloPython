def checkNum(inputText):
    OK = False
    while not OK:
        try:
            number = int(inputText)
            if number < 0:
                print('The data is incorrect!')
                quit()
            OK = True
        except ValueError:
            print('Error') 
      
    return number