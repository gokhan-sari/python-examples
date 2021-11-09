import time

start = time.time()

evenNumberList = [number for number in range(2, 1001, 2)]
evenNumberTuple = tuple(evenNumberList)

print(evenNumberList)
print(evenNumberTuple)

end = time.time()

print(end - start)
