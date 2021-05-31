import re

class ReadLog:
    def __init__(self, log_file, process="Xorg"):
        # List of values to be extracted
        self.timestamps = []
        self.cpu_used = []
        self.cpu_idle = []
        self.mem_total = []
        self.mem_used = []
        self.mem_free = []
        self.process_mem = []
        self.process_cpu = []

        # open and read log file
        temp_count = 0
        with open(log_file) as fd:
            for line in fd:
                if re.match("top - ", line):
                    temp_count+=1
                    print("In top output counter={}".format(temp_count))
                    # Should have hit 1st line of top output
                    # extract time stamp
                    pattern = re.compile(r'top - (\d+:\d+:\d+) up')
                    group1 = pattern.search(line)
                    print("Timestamp group=",group1.groups(1)[0])
                    self.timestamps.append(group1.groups(1)[0])

                    # extract cpu used, idle
                    fd.readline() # skip 1 line
                    line = fd.readline() # read CPU line
                    if re.match(r'%Cpu', line):
                        pattern = re.compile(r'(\d+.\d+) us.* (\d+.\d+) id')
                        group2 = pattern.search(line)
                        print("Group2 values={}, {}".format(group2.groups(1)[0], group2.groups(1)[1]))
                        self.cpu_used.append(group2.groups(1)[0])
                        self.cpu_idle.append(group2.groups(2)[1])

                    # extract memory total, used, free
                    line = fd.readline() # read MEM line
                    if re.match(r'KiB Mem', line):
                        pattern = re.compile(r'(\d+) total,\s+(\d+) used,\s+(\d+) free')
                        group3 = pattern.search(line)
                        print("Group3 values={}, {}, {}".format(group3.groups(1)[0], group3.groups(1)[1], group3.groups(1)[2]))
                        self.mem_total.append(group3.groups(1)[0])
                        self.mem_used.append(group3.groups(2)[1])
                        self.mem_free.append(group3.groups(2)[2])

                    # extract process's %cpu and %mem
                    # FIXME

        print(self.timestamps)
        print(self.cpu_used)
        print(self.cpu_idle)
        print(self.mem_total)
        print(self.mem_used)
        print(self.mem_free)

    def get_time_stamps(self):
        return self.timestamps

    def get_cpu_used(self):
        return self.cpu_used

    def get_cpu_idle(self):
        return self.cpu_idle

    def get_mem_total(self):
        return self.mem_total

    def get_mem_used(self):
        return self.mem_used

    def get_mem_free(self):
        return self.mem_free

