import os

filename=1
for i in range(16):
    os.system('mv '+str(filename)+'.png p'+str(i+1)+'.png')
    filename=filename+1