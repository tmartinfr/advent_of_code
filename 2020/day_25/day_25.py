loop_size = 8
#pub = 5764801
#pub = 14788856  # loop size : 761420
#pub = 19316454  # loop size : 16203426
subject = 7
subject = 19316454

value = 1
# loop_size = 0
# while True:
#     loop_size += 1
for _ in range(0, 761420):
    value *= subject
    value %= 20201227
    # if value == pub:
    #     break

#assert value == pub
#print(loop_size)
print(value)
