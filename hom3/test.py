import time
import os.path
import psutil
import json

# read config.txt
type_of_file = None
time_int = None
i = 0


class Def_setings():
    def defenition(self):
        global type_of_file, time_int
        with open('config.txt', 'r') as out:
            for line in out:
                type_f = out.readline()
                time_interval = out.readline()

        for i in type_f:
            if not i.isalpha() and i != ' ':
                type_f = type_f.replace(i, '')

        type_of_file = (type_f.split()[1].strip())

        # interval time definition
        for i in time_interval:
            if not i.isdigit() and i != ' ':
                time_interval = time_interval.replace(i, '')

        time_int = (time_interval.split()[0].strip())


# set class-checker
class F_checker():
    def check(self):
        if os.path.exists("output.txt") == 0:
            with open("output.txt", "w"):
                pass

        if os.path.exists("output.json") == 0:
            with open("output.json", "w"):
                pass


if __name__ == '__main__':
    ch = F_checker()
    read = Def_setings()
    ch.check()
    read.defenition()

# scheduler

while True:
    Time = time.strftime("%m-%d-%Y %H:%M:%S", time.gmtime())
    cpu = psutil.cpu_stats()
    mem = psutil.virtual_memory()
    vmem = psutil.swap_memory()
    io = psutil.disk_io_counters(perdisk=False)
    net = psutil.net_if_stats()
    i += 1
    if type_of_file == "txt":
        with open("output.txt", "a") as out:
            out.write("SNAPSHOT {} :{}:".format(i, Time))
            out.write("\n{},\n{},\n{},\n{},\n{}\n".format(cpu, mem, vmem, io, net))
    elif type_of_file == "json":
        with open("output.json", "a") as out:
            json.dumps("SNAPSHOT {} :{}:".format(i, Time, file, indent=4))
            json.dumps("\n{},\n{},\n{},\n{},\n{}\n".format(cpu, mem, vmem, io, net, file, indent=4))

    time.sleep(int(time_int) * 60)
