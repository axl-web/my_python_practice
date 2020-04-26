def hanoi(disks, source,middle, destination):
    if disks>=1:
        hanoi(disks-1,source,destination,middle)
        print("mover disco de torre ",source," a ",destination)
        hanoi(disks-1,middle,source,destination)
hanoi(3,1,2,3)