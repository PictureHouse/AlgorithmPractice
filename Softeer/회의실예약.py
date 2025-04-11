# [21년 재직자 대회 예선] 회의실 예약

import sys

room_num, reservation_num = map(int, input().split())

rooms = []
for i in range(0, room_num):
    tmp = [0 for i in range(10)]
    tmp[0] = input()
    rooms.append(tmp)
rooms.sort()

for i in range(0, reservation_num):
    new_reservation = input().split()
    for room in rooms:
        if room[0] == new_reservation[0]:
            for i in range(int(new_reservation[1]) - 8, int(new_reservation[2]) - 8):
                room[i] += 1
            break

for room in rooms:
    print("Room " + room[0] + ":")
    
    available_count = 0
    for i in range(1, 10):
        if room[i-1] != 0 and room[i] == 0:
            available_count += 1
    if available_count == 0:
        print("Not available")
    else:
        print(f"{available_count} available:")
        queue = []
        for i in range(1, 10):
            if room[i-1] != 0 and room[i] == 0:
                queue.append(i)
            elif room[i-1] == 0 and room[i] != 0:
                start = queue.pop() + 8
                end = i + 8
                print(f"{start:02d}-{end:02d}")
        if len(queue) != 0:
            start = queue.pop() + 8
            end = 18
            print(f"{start:02d}-{end:02d}")

    if room != rooms[-1]:
        print('-----')
