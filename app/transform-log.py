import json, os, argparse

class LogEntry:
    def __init__(self, timestamp, speaker, message=None):
        self.timestamp = timestamp
        self.speaker = speaker
        self.message = message

def transform_log(file_path):
    file_name = os.path.basename(file_path).split(".")[0]
    to_file = f'./logs/{file_name}.json'
    print(f"Writing to {to_file}.")
    with open(to_file, 'a') as json_file:
        json_file.write('[')
    try:
        _speaker = "Orchestrator"
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                print(f".", end="")
                line = line.strip()
                parts = line.split(" - ", maxsplit=2)
                if len(parts) == 3:
                    le = LogEntry(parts[0], _speaker)
                    parts[2] = parts[2].replace('\\"', '"')
                    parts[2] = parts[2].replace('\"', "'")
                    if parts[1] == 'DEBUG':
                        if parts[2].startswith('Next Speaker'):
                            _speaker = parts[2].split(': ')[1]
                    try:
                        le.message = json.loads(parts[2])
                    except json.JSONDecodeError:
                        le.message = parts[2]
                        pass
                    with open(to_file, 'a') as json_file:
                        json.dump(le.__dict__, json_file)
                        json_file.write(',')
                else:
                    print(f"Zeile konnte nicht korrekt aufgeteilt werden: {line}")
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    with open(to_file, 'a') as json_file:
        json_file.truncate(json_file.tell() - 1)
        json_file.write(']')
    print("")
    print("Transformation completed.")

if __name__ == "__main__":
    print("Transforming log file to JSON format.")
    parser = argparse.ArgumentParser(description="Transform a log file into JSON format.")
    parser.add_argument("file_path", help="Path to the log file to be transformed.")
    args = parser.parse_args()
    print(f"Transforming file {args.file_path}...")
    transform_log(args.file_path)