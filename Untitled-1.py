import psutil

print(psutil.cpu_times().user)
print(psutil.cpu_count())
print(psutil.virtual_memory())
print(psutil.users())
msg = "Hello World"
print(msg)
