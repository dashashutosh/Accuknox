import psutil

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# Function to check CPU usage
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"High CPU usage detected: {cpu_percent}%")

# Function to check memory usage
def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"High memory usage detected: {memory_percent}%")

# Function to check disk usage
def check_disk_usage():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        print(f"High disk usage detected: {disk_percent}%")

# Function to check running processes
def check_running_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    print("Running processes:")
    for process in processes:
        print(f"PID: {process['pid']}, Name: {process['name']}")

# Main function
def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
