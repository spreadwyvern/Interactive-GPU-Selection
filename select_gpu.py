print('===== status of GPUs =====')
from pynvml import *
import os
nvmlInit()
available_gpus = []
for i in range(nvmlDeviceGetCount()):
    handle = nvmlDeviceGetHandleByIndex(i)
    
    meminfo = nvmlDeviceGetMemoryInfo(handle)
    print("%s: %0.1f MB free, %0.1f MB used, %0.1f MB total" % (nvmlDeviceGetName(handle), 
                                                                meminfo.free/1024.**2, 
                                                                meminfo.used/1024.**2, 
                                                                meminfo.total/1024.**2))
    if meminfo.used == 0:
        available_gpus.append(i)
nvmlShutdown()
print('===== available GPUs ===== \n GPU {}'.format(available_gpus))

# input desired number of GPUs
print('Desired number of GPUs: ')
n_gpus = int(input())
print('===== acquired GPUs =====')
use_gpu = available_gpus[:n_gpus]
if n_gpus <= len(available_gpus):
    os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(str(x) for x in use_gpu)
    print('Training on GPU {}'.format(use_gpu))
else:
    print('Not enough available GPUs!!')
    raise ValueError("n_gpus must be smaller than the number of available GPUs")