import sys
import argparse
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.split()
    return {'date': parts[0], 'time': parts[1], 'level': parts[2], 'message': ' '.join(parts[3:])}

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    return Counter(log['level'] for log in logs)

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Аналізатор файлів логів")
    parser.add_argument('logfile', type=str, help="Шлях до файлу логів")
    parser.add_argument('-l', '--level', type=str, help="Рівень логування для фільтрації (INFO, ERROR, DEBUG, WARNING)")
    args = parser.parse_args()

    logs = load_logs(args.logfile)
    if args.level:
        logs = filter_logs_by_level(logs, args.level)
        for log in logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        display_log_counts(count_logs_by_level(logs))




#Запуск

#python log_analyzer.py path/to/your/logfile.log


#python log_analyzer.py path/to/your/logfile.log -l error


