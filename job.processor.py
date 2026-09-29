import threading
import time
import uuid

# Store job information
jobs = {}


# Background job function
def background_job(job_id, task_name):
    jobs[job_id]["status"] = "Running"

    print(f"\nJob {job_id} started...")

    # Simulate time-consuming work
    for i in range(5):
        time.sleep(1)
        print(f"Job {job_id}: Processing {i + 1}/5")

    jobs[job_id]["status"] = "Completed"
    jobs[job_id]["log"] = "Task completed successfully."

    print(f"Job {job_id} completed!")


# Submit a new job
def submit_job(task_name):
    job_id = str(uuid.uuid4())[:8]

    jobs[job_id] = {
        "task": task_name,
        "status": "Queued",
        "log": ""
    }

    thread = threading.Thread(
        target=background_job,
        args=(job_id, task_name)
    )

    thread.start()

    print(f"\nJob submitted successfully!")
    print(f"Job ID: {job_id}")

    return job_id


# Check job status
def check_status(job_id):
    if job_id in jobs:
        print("\n--- Job Status ---")
        print("Job ID :", job_id)
        print("Task   :", jobs[job_id]["task"])
        print("Status :", jobs[job_id]["status"])
        print("Log    :", jobs[job_id]["log"])
    else:
        print("Job not found!")


# Main program
while True:
    print("\n===== Background Job Processor =====")
    print("1. Submit Job")
    print("2. Check Job Status")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        submit_job(task)

    elif choice == "2":
        job_id = input("Enter Job ID: ")
        check_status(job_id)

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")