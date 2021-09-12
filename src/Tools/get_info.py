import os
import psutil
from datetime import datetime
from time import strftime

## CPU

def get_size(bytes):
    factor = 1028
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}"
        bytes /= factor

