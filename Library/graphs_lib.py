import matplotlib.pyplot as plt

class DrawGraphs:
    def __init__(self, log_obj):
        self.log_obj = log_obj

    def show_all_graphs(self):
        x_timestamps = self.log_obj.timestamps
        y_cpu_used = self.log_obj.cpu_used
        y_cpu_idle = self.log_obj.cpu_idle
        y_mem_total = self.log_obj.mem_total
        y_mem_used = self.log_obj.mem_used
        y_mem_free = self.log_obj.mem_free

        x_values = range(len(self.log_obj.timestamps))
        plt.plot(x_values, self.log_obj.cpu_used, label="CPU Used%")
        plt.plot(x_values, self.log_obj.cpu_idle, label="CPU Idle%")
        plt.plot(x_values, self.log_obj.mem_total, label="Memory Total")
        plt.plot(x_values, self.log_obj.mem_used, label="Memory Used")
        plt.plot(x_values, self.log_obj.mem_free, label="Memory Free")

        plt.xlabel("Timestamp")
        plt.ylabel("CPU% and Mem-Kb")
        plt.legend()
        plt.title("Top command output vs timestamp")

        plt.show()