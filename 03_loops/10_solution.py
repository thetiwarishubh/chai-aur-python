import time

def retry_with_backoff(operation):
    max_retries = 5
    delay = 1 

    for attempt in range(1, max_retries + 1):
        try:
            result = operation()
            print("Success on attempt", attempt)
            return result
        except Exception as e:
            print(f"Attempt {attempt} failed:", e)

            if attempt == max_retries:
                print("Max retries reached. Exiting.")
                break

            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2 

def flaky_task():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Done"

retry_with_backoff(flaky_task)