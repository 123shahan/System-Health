import psutil
import logging
from datetime import datetime
import time

# Define thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        alert(f"CPU usage is high: {usage}%")
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        alert(f"Memory usage is high: {usage}%")
    return usage

def check_disk_space():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        alert(f"Disk space usage is high: {usage}%")
    return usage

def check_running_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
    return processes

def alert(message):
    print(message)
    logging.info(message)

def main():
    print("Starting system health monitoring...")

    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_space()
        running_processes = check_running_processes()
        
        # Log current system health
        logging.info(f"CPU usage: {cpu_usage}%")
        logging.info(f"Memory usage: {memory_usage}%")
        logging.info(f"Disk space usage: {disk_usage}%")
        logging.info(f"Number of running processes: {len(running_processes)}")
        
        # Wait before checking again
        time.sleep(10)  # Check every 60 seconds

if __name__ == "__main__":
    main()

