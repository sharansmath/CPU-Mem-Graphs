import sys
import time
import Library as lib

'''
Coding tips:
1. Use enumarate() instead of range(len(list))
2. Use list comprehention instead of raw for loops 
3. Use sorted(), set()
4. Use libraries like collections/Counter, 
5. Use f-strings for print(v3.6+). print(f"my output {var}")
'''

def main():
    '''
    This is main function and execution starts from here

    :param log_file: Log file name to parse
    :return: Nothing, Display graphs
    '''

    # Read config values
    config_obj = lib.ReadConfig()
    mem_t = config_obj.read_element('memory_threshold')
    print(f"Value of memory threshold= {mem_t}")
    process_list = config_obj.read_element('process_list')
    print(f"Value of memory threshold= {process_list}")

    # Read log file and return values of memory
    log_obj = lib.ReadLog('log_file.txt')
    # FIXME - Below lines to fetch values not required.
    timestamps = log_obj.get_time_stamps()
    cpu_used = log_obj.get_cpu_used()
    cpu_idle = log_obj.get_cpu_idle()
    mem_total = log_obj.get_mem_total()
    mem_used = log_obj.get_mem_used()
    mem_free = log_obj.get_mem_free()

    # Draw graphs
    graph_obj = lib.DrawGraphs(log_obj)
    graph_obj.show_all_graphs()

    # RESUME Here - How to difference y-axis values for 2 categories

if __name__ == "__main__":
    main()
    #print(main.__doc__)