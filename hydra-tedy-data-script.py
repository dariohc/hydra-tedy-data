file = open("10-test-I-TVC-Sine-Z.unv", "r")
file_out = open('output.txt', 'w')
search_string = "Time for "
for k in range(1000000):
   current_line = file.readline()
   if current_line.rfind(search_string) >= 0:
        file_out.write(current_line[len(search_string):])
        print ("I'm here writing the sensor")
        for j in range(4) : file.readline()
        my_list = list(file.readline().split())
        file_out.write(my_list[5] + '\n\n')

file.close()
file_out.close()