resistance = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
              'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}    # dictionary 형식으로 저항값 선언

color_list = [input() for i in range(3)]
print(int(str(resistance[color_list[0]]) + str(resistance[color_list[1]])) * (10 ** resistance[color_list[2]]))