import psutil

def get_size(bytes,sufix = "8"):
    factor = 1028
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{sufix}"
        bytes /= factor

