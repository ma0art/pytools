# process_tracker.py
import time

# グローバル変数を使用して開始時刻を保持
start_time = None

def tracker_start():
    global start_time
    start_time = time.time()

def tracker_end():
    global start_time
    if start_time is None:
        print("Error: tracker_start() was not called.")
        return

    end_time = time.time()
    duration = end_time - start_time
    print(f"Processed in {duration} seconds.")

    # 次の計測のために開始時刻をリセット
    start_time = None