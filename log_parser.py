import sys
from collections import defaultdict

date_key = "date"
time_key = "time"
level_key = "level"
message_key = "message"

# for case we cannot parse log line for some reasons
FALLBACK_LOG_LINE = {
    date_key: "INVALID", 
    time_key: "INVALID", 
    level_key: "INVALID", 
    message_key: "INVALID"
    }


def main(path_to_log: str, level: str = None):
    print(f"Trying to read logs  from file {path_to_log}.....")

    try:
       logs = load_logs(path_to_log)

       # calculate and output statistics by all log levels
       logs_by_levels_stats = count_logs_by_level(logs)

       # extra linebreak for readability
       print("\n")
       print("Here's your statistics:")
       display_log_counts(logs_by_levels_stats)


       # let's also show detailed logs by specified level
       if level is not None:
           # extra linebreak for readability
           print("\n")

           level_logs = filter_logs_by_level(logs, level)
           display_detailed_log_for_level(level, level_logs)
    except FileNotFoundError:
        print("File is not exist, make sure you provided correct path")
    except Exception:
        print("Unexpected error occured")


# reads file, uses parse_log_line in loop, returns details about each log line
def load_logs(file_path: str) -> list:
    result = []
    with open(file_path, mode = "r", encoding="utf-8") as file:
        result = [parse_log_line(raw_line) for raw_line in file.readlines()]

    return result
    

# returns parsed date/time/level/message as dict
def parse_log_line(line: str) -> dict:
    line = line.strip()

    try:
        if len(line) == 0:
            return FALLBACK_LOG_LINE
        
        date, time, level, *message_parts = line.split()
        message = " ".join(message_parts)

        return {
            date_key: date,
            time_key: time,
            level_key: level,
            message_key: message
        }
    except Exception as err:
        print(f"Internal log: exception happened when trying to parse line {line}")
        return FALLBACK_LOG_LINE


# returns logs filtered by level
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: level == log[level_key].lower(), logs))


# returns count of messages by each level
def count_logs_by_level(logs: list) -> dict:
    result = defaultdict(int)

    for log in logs:
        result[log[level_key].lower()] += 1

    return dict(result)


# outputs table with result
def display_log_counts(counts: dict):
    if len(counts) == 0:
        print("No logs found")

    level_title = "Log level"
    count_by_level = "Count"
    vertical_divider = "|"
    row_length = 15 # should be enough for most cases

    # print title
    print(f"{level_title:<{row_length}} {vertical_divider} {count_by_level:<{row_length}}")

    # print horizontal divider
    horizontal_divider = "-" * row_length
    print(f"{horizontal_divider} {vertical_divider} {horizontal_divider}")

    # print counts
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    for log_level in sorted_counts:
        level_count = sorted_counts[log_level]
        formatted_log_level = log_level.upper()
        print(f"{formatted_log_level:<{row_length}} {vertical_divider} {level_count:<{row_length}}")
    

# outputs all logs by level, if any
def display_detailed_log_for_level(level: str, level_logs: list):
    if len(level_logs) == 0:
        print(f"No logs found by level \'{level}\'")
        return
    
    print(f"Detailed logs by level \'{level.upper()}\':")
    for log in level_logs:
        print(f"{log[date_key]} {log[time_key]} - {log[message_key]}")

    

if __name__ == "__main__":
    # we expect first arg after script name is gonna be path to the log file
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
        
        # user can specify if he wants to see detailed logs by some level
        optional_log_level = sys.argv[2] if len(sys.argv) > 2 else None

        main(dir_path, optional_log_level)
    else:
        print("No path found. Make sure to put path to log file as the first parameter of this script")