import sys

from Grantt_Information import ProcessGrantInfo

sys.path.append(".")


class MLFQ:
    processes = []
    grantt_chart = []
    current_cpu_time = 0
    ClassName = 'MLFQ'

    def __init__(self, processes):
        self.processes = processes

    def get_arrival_times(self):
        _temp = {}
        for process in self.processes:
            _temp[str(process.process_id)] = process.arrival_time
        return _temp

    def cpu_process(self):
        first_time_quantum = 8
        sec_time_quantum = 16
        self.two_queue_with_diff_quantum(first_time_quantum, sec_time_quantum)
        self.fcfs_queue()
        return self.grantt_chart

    def two_queue_with_diff_quantum(self, fist_time_quantum, second_time_quantum):
        done_first_time_quantum = []
        is_sec_burst_allowed = False
        processes_count = len(self.processes)
        prev_cpu_time = 0
        started = False
        ready_processes_queue = []
        processes_next_ready_queue = self.get_arrival_times()
        cycle = 1
        total_counter = 0
        while True:
            if cycle == 1:
                time_quantum = fist_time_quantum
            else:
                time_quantum = second_time_quantum

            if not started:
                first_process = self.processes[0]
                self.processes.remove(first_process)
                ready_processes_queue.append([first_process, 0])
                for process in self.processes.copy():
                    if process.arrival_time == first_process.arrival_time:
                        ready_processes_queue.append([process, 0])
                        self.processes.remove(process)
                started = True

            if len(ready_processes_queue) == 0 and not is_sec_burst_allowed:
                self.current_cpu_time += 1
                continue

            elif len(ready_processes_queue) == 0 and is_sec_burst_allowed:
                ready_processes_queue.append([self.processes.pop(0), 0])

            sub_count = ready_processes_queue[0][1]
            current_process = ready_processes_queue[0][0]
            pre_current_process = current_process.cpu_burst_time1 + current_process.cpu_burst_time2 + current_process.io_time
            if current_process.cpu_burst_time1 > 0 and current_process.arrival_time <= self.current_cpu_time:
                not_entered = True
                for element in self.grantt_chart:
                    if element.process.process_id == current_process.process_id:
                        not_entered = False
                if not_entered:
                    self.grantt_chart.append(ProcessGrantInfo(current_process,
                                                              max(current_process.arrival_time, self.current_cpu_time),
                                                              # first cpu start
                                                              -1,  # io start time
                                                              -1,  # sec cpu start
                                                              -1,  # first cpu end
                                                              -1,  # io end time
                                                              -1))  # sec cpu end

                current_process.cpu_burst_time1 -= time_quantum
                sub_count += 1
                if current_process.cpu_burst_time1 < 0:
                    self.current_cpu_time += (current_process.cpu_burst_time1 + time_quantum)
                else:
                    self.current_cpu_time += time_quantum

            if current_process.cpu_burst_time1 <= 0 and current_process.arrival_time <= self.current_cpu_time and \
                    processes_next_ready_queue[str(current_process.process_id)] <= self.current_cpu_time:
                if current_process.io_time > 0:
                    ready_processes_queue[0][1] = 0  # sub_count = 0
                    sub_count = 0
                    processes_next_ready_queue[
                        str(current_process.process_id)] = self.current_cpu_time + current_process.io_time

                    for info in self.grantt_chart:
                        if info.process.process_id == current_process.process_id:
                            info.process = current_process
                            info.io_start_time = self.current_cpu_time
                            info.cpu_end_time1 = self.current_cpu_time
                            info.io_end_time = self.current_cpu_time + current_process.io_time
                            if current_process.cpu_burst_time2 <= 0:
                                info.cpu_start_time2 = -1
                                info.cpu_end_time2 = -1
                            break
                    current_process.io_time = 0

                elif current_process.cpu_burst_time2 > 0 and current_process.cpu_burst_time1 <= 0 and is_sec_burst_allowed:
                    if sub_count == 0:
                        for info in self.grantt_chart:
                            if info.process.process_id == current_process.process_id:
                                info.cpu_start_time2 = self.current_cpu_time
                    if processes_next_ready_queue[str(current_process.process_id)] <= self.current_cpu_time:
                        current_process.cpu_burst_time2 -= time_quantum
                        sub_count += 1
                        if current_process.cpu_burst_time2 < 0:
                            self.current_cpu_time += (current_process.cpu_burst_time2 + time_quantum)
                        else:
                            self.current_cpu_time += time_quantum
                    if current_process.cpu_burst_time2 <= 0:
                        for info in self.grantt_chart:
                            if info.process.process_id == current_process.process_id:
                                info.process = current_process
                                info.cpu_end_time2 = self.current_cpu_time
                                break

            current_process_value = current_process.cpu_burst_time1 + current_process.cpu_burst_time2 + current_process.io_time
            if pre_current_process != current_process_value:
                ready_processes_queue.pop(0)
                total_counter += 1
                if current_process.cpu_burst_time2 > 0 or current_process.cpu_burst_time1 > 0 or current_process.io_time > 0:
                    ready_processes_queue.append([current_process, sub_count])

            if len(self.processes) <= 0 and len(ready_processes_queue) <= 0:
                break

            # counter = 0
            # for each in ready_processes_queue:
            #     if each[1] > 0:
            #         counter += 1
            # if counter == processes_count:
            #     if is_sec_burst_allowed:
            #         break
            #     is_sec_burst_allowed = True
            #     for each in ready_processes_queue:
            #         self.processes.append(each[0])
            #     ready_processes_queue.clear()
            #     done_first_time_quantum.clear()
            #     continue

            # if len(self.processes) == 0 and len(ready_processes_queue) == processes_count:
            if len(ready_processes_queue) == processes_count and total_counter == processes_count:
                if not is_sec_burst_allowed:
                    is_sec_burst_allowed = True
                    for each in ready_processes_queue:
                        self.processes.append(each[0])
                    self.sort()
                    ready_processes_queue.clear()
                    done_first_time_quantum.clear()
                    cycle = 2
                    continue
                else:
                    break
            # else:

            if prev_cpu_time == self.current_cpu_time:
                self.current_cpu_time += 1
            prev_cpu_time = self.current_cpu_time

            _temp = []
            new_queue = False
            for process in self.processes.copy():
                if process.arrival_time <= self.current_cpu_time:
                    _temp.insert(0, [process, 0])
                    self.processes.remove(process)
                    new_queue = True

            if new_queue:
                for process_info in _temp:
                    ready_processes_queue.insert(0, process_info)
            _temp.clear()

    def fcfs_queue(self):
        for process_info in self.grantt_chart:
            if process_info.cpu_start_time1 < 0:
                process_info.cpu_start_time1 = self.current_cpu_time

            if process_info.cpu_end_time1 < 0:
                process_info.cpu_end_time1 = process_info.cpu_start_time1 + process_info.process.cpu_burst_time1
                self.current_cpu_time += process_info.process.cpu_burst_time1

            if process_info.io_start_time < 0:
                process_info.io_start_time = process_info.cpu_end_time1

            if process_info.io_end_time:
                process_info.io_start_time = process_info.io_start_time + process_info.process.io_time
                self.current_cpu_time += process_info.io_end_time

            if process_info.cpu_start_time2 < 0:
                if process_info.io_end_time <= self.current_cpu_time:
                    process_info.cpu_start_time2 = self.current_cpu_time
                else:
                    process_info.cpu_start_time2 = process_info.io_end_time + self.current_cpu_time
                    self.current_cpu_time += process_info.io_end_time

            elif process_info.cpu_end_time2 < 0:
                process_info.cpu_end_time2 = self.current_cpu_time + process_info.process.cpu_burst_time2
                self.current_cpu_time += process_info.process.cpu_burst_time2

    def sort(self):
        sorted_processes = []
        arrival_times = []
        for process in self.processes:
            arrival_times.append(process.arrival_time)
        arrival_times.sort()
        for arrival_time in arrival_times:
            for process in self.processes.copy():
                if process.arrival_time == arrival_time:
                    sorted_processes.append(process)
                    self.processes.remove(process)
        self.processes.clear()
        self.processes = sorted_processes.copy()