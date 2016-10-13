import os

filename=30
for i in range(12):
    os.system('mv '+str(filename)+'.gif '+str((i+3)%12)+'.gif')
    filename=filename+1