import os
LOADING_BAR_SIZE = 50

def showProgressBar(current, total):
    percent = LOADING_BAR_SIZE * ((current + 1) / total)
    bar = "#" * int(percent) + "-" * (LOADING_BAR_SIZE - int(percent))
    print(f"\t[{bar}] - ({(100/LOADING_BAR_SIZE)*percent:.2f}%)")
    