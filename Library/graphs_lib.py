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

        figure, axis = plt.subplots(2)

        axis[0].plot(x_values, self.log_obj.cpu_used, label="CPU used%")
        axis[0].plot(x_values, self.log_obj.cpu_idle, label="CPU Idle%")
        axis[1].plot(x_values, self.log_obj.mem_total, label="Memory Total")
        axis[1].plot(x_values, self.log_obj.mem_used, label="Memory Used")
        axis[1].plot(x_values, self.log_obj.mem_free, label="Memory Free")

        axis[0].set_xticks(x_values, self.log_obj.timestamps)
        axis[0].set_title("CPU% vs Timestamp")
        axis[0].set(xlabel='Timestamp', ylabel="CPU%")

        axis[1].set_xticks(x_values, self.log_obj.timestamps)
        axis[1].set_title("Memory vs Timestamp")
        axis[1].set(xlabel='Timestamp', ylabel="Memory KiB")

        axis[0].legend()
        axis[1].legend()
        #figure.suptitle("Top command output vs timestamp")

        plt.tight_layout()
        plt.show()