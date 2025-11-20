import time

def countdown(seconds : int) -> None:
    total = seconds
    bar_length = 30

    while seconds:
        mins, secs = divmod(seconds, 60)
        percent = (total - seconds) / total
        filled = int(bar_length * percent)
        bar = '#' * filled + '-' * (bar_length - filled)

        print(f"{mins:02}:{secs:02} [{bar}] {percent*100:6.2f}%", end='\r')
        time.sleep(1)
        seconds -= 1

    print(f"00:00 [{'#' * bar_length}] 100.00% ✅\nTime's up!")


if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("Please enter a valid integer.")