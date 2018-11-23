import psutil
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

psutil.cpu_times()
for i in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# all the size return byte type
psutil.virtual_memory()
psutil.swap_memory()

# Process
processes = psutil.pids()
p = psutil.Process(1)
# name of process
p.name()
# executed path of process
p.exe()
# process working dir
p.cwd()
p.cmdline()
p.ppid()
p.parent()
p.children()
p.status()
p.username()
p.create_time()
p.terminal()
p.cpu_times()
p.memory_info()
p.open_files()
p.connections()
p.num_threads()
p.threads()
p.environ()
p.terminate()

# psutil.test()
# just behave like ps
