import os
def XO():

    def Printing():
        os.system('clear')
        print('\n')
        for i in range(1, 4):
            for j in range(1, 4):
                if (i, j) in x:
                    print('|','X','|', end='')
                elif (i, j) in o:
                    print('|','O','|', end='')
                else:
                    print('|','-','|', end='')
            print()

    os.system('clear')
    print('\033[92m'+'\'------------------------------\'')
    print('\033[94m|'+'XXX   XXX','\033[93m'+'         //','\033[91m'+'  OOO   |')
    print('\033[94m|'+' XXX XXX ','\033[93m'+'        // ','\033[91m'+' OO OO  |')
    print('\033[94m|'+'  XXXXX  ','\033[93m'+'       //  ','\033[91m'+'OO   OO |')
    print('\033[94m|'+'   XXX   ','\033[93m'+'      //  ','\033[91m'+'OO     OO|')
    print('\033[94m|'+'   XXX   ','\033[93m'+'     //   ','\033[91m'+'OO     OO|')
    print('\033[94m|'+'  XXXXX  ','\033[93m'+'    //     ','\033[91m'+'OO   OO |')
    print('\033[94m|'+' XXX XXX ','\033[93m'+'   //       ','\033[91m'+'OO OO  |')
    print('\033[94m|'+'XXX   XXX','\033[93m'+'  //         ','\033[91m'+'OOO   |')
    print('\033[92m'+'\'------------------------------\'\n')
    
    print('      1. PvP Mode')
    print('      2. PvC Mode (Beta)\n')
    z = int(input('\033[95m'+'Write the number of Option: '))
    
    if z == 2:
        pass

    if z == 1:


#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
# Print Section / Print Section / Print Section / Print Section / Print Section / Print Section / Print Section / Print Section / Print Section
#----------------------------------------------------------------------------------------------------------------------------------------------        
#----------------------------------------------------------------------------------------------------------------------------------------------

        x = []
        o = []

        counter = 0


        while True:
            os.system('clear')
            print('\n')
            for i in range(1, 4):
                for j in range(1, 4):
                    if (i, j) in x:
                        print('\033[94m', end='')
                        print('|','X','|', end='')
                    elif (i, j) in o:
                        print('\033[91m', end='')
                        print('|','O','|', end='')
                    else:
                        print('\033[93m', end='')
                        print('|','-','|', end='')
                print()

    #----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Moves Input Section / Moves Input Section / Moves Input Section / Moves Input Section / Moves Input Section / Moves Input Section /
    #----------------------------------------------------------------------------------------------------------------------------------------------        
    #----------------------------------------------------------------------------------------------------------------------------------------------

            if counter % 2 == 0:
                print('\033[94m')
                print('X\'s turn')
                fir = int(input('Write first number: '))
                sec = int(input('Write second number: '))
                while True:
                    if fir > 3 or fir <= 0:
                        fir = int(input('Write first number: '))
                    elif sec > 3 or sec <= 0:
                        sec = sec = int(input('Write second number: '))
                    else:
                        break
            else:
                print('\033[91m')
                print('O\'s turn')
                fir = int(input('Write first number: '))
                sec = int(input('Write second number: '))
                while True:
                    if fir > 3 or fir <= 0:
                        fir = int(input('Write first number: '))
                    elif sec > 3 or sec <= 0:
                        sec = sec = int(input('Write second number: '))
                    else:
                        break

            while True:
                if (fir, sec) in x or (fir, sec) in o:
                    print('This position is almost captured !')
                    fir = int(input('Write first number: '))
                    sec = int(input('Write second number: '))
                else:
                    if counter % 2 == 0:
                        x.append((fir, sec))
                        counter += 1
                        break
                    else:
                        o.append((fir, sec))
                        counter += 1
                        break


    #----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Moves Sorting Section / Moves Sorting Section / Moves Sorting Section / Moves Sorting Section / Moves Sorting Section / Moves Sorting Section
    #----------------------------------------------------------------------------------------------------------------------------------------------        
    #----------------------------------------------------------------------------------------------------------------------------------------------

        
            x_dic_ryad = {}
            x_dic_column = {}
            o_dic_ryad = {}
            o_dic_column = {}

            for i in x:    
                if i[0] in x_dic_ryad.keys():
                    x_dic_ryad[i[0]] += 1
                else:
                    x_dic_ryad[i[0]] = 1

                if i[1] in x_dic_column.keys():
                    x_dic_column[i[1]] += 1
                else:
                    x_dic_column[i[1]] = 1
            
            print(x_dic_ryad)
            print(x_dic_column)

            for i in o:
                if i[0] in o_dic_ryad.keys():
                    o_dic_ryad[i[0]] += 1
                else:
                    o_dic_ryad[i[0]] = 1
                    
                if i[1] in o_dic_column.keys():
                    o_dic_column[i[1]] += 1
                else:
                    o_dic_column[i[1]] = 1

    #---------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------------
    #  Game Over / Section Game / Over Section / Game Over Section / Game Over Section / Game Over Section / Game Over Section / Game Over Section
    #---------------------------------------------------------------------------------------------------------------------------------------------        
    #---------------------------------------------------------------------------------------------------------------------------------------------
        
            o1 = list(filter(lambda x: x == 3, o_dic_ryad.values()))
            o2 = list(filter(lambda x: x == 3, o_dic_column.values()))
            x1 = list(filter(lambda x: x == 3, x_dic_ryad.values()))
            x2 = list(filter(lambda x: x == 3, x_dic_column.values()))

            if ((3,3) in x) and ((2,2) in x) and ((1,1) in x):
                print('\033[94m')
                Printing()
                print('X is winner!')
                return '\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            
            elif ((1,3) in x) and ((2,2) in x) and ((3,1) in x):
                print('\033[94m')
                Printing()
                print('X is winner!')
                return '\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            
            if ((3,3) in o) and ((2,2) in o) and ((1,1) in o):
                print('\033[91m')
                Printing()
                print('O is winner!')
                return '\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            
            elif ((1,3) in o) and ((2,2) in o) and ((3,1) in o):   
                print('\033[91m')       
                Printing()
                print('O is winner!')
                return '\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            
            if (3 in x1) or (3 in x2):
                print('\033[94m')
                Printing()
                print('X Is Winner!')
                return f'\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            
            elif len(x) == 5:
                print('\033[93m')
                Printing()
                print('Draw!')
                return f'\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            
            elif (3 in o1) or (3 in o2):
                print('\033[91')
                Printing()
                print('O Is Winer!')
                return f'\U0001F1EC\U0001F1E6\U0001F1F2\U0001F1EA \U0001F1F4\U0001F1FB\U0001F1EA\U0001F1F7'
            


print(XO())