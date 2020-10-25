import boto3
import json
import sys


def get_log_groups():
    total = []
    cw = boto3.client("logs")
    batch = cw.describe_log_groups()
    total.extend(batch["logGroups"])
    next_token = batch.get("nextToken", "")
    while next_token != "":
        batch = cw.describe_log_groups(nextToken=next_token)
        total.extend(batch["logGroups"])
        next_token = batch.get("nextToken", "")
    logs = [l["logGroupName"] for l in total]

    return logs


def main(filter):
    logs = get_log_groups()

    filtered_logs = [l for l in logs if filter in l]
    for index, log in enumerate(filtered_logs):
        print(f"\t{index + 1}. {log}")

    log_num = input("\nSelect log number: ")
    if log_num == "0":
        quit()
    index = int(log_num) - 1
    selection = filtered_logs[index]

    print(f"\nGetting logs for: {selection}")
    with open("/Users/sziegler/temp/temp_shell.sh", "w") as file:
        command = f"awslogs get {selection} --start 10m --timestamp"
        file.write(command)


if __name__ == "__main__":
    filter = ""
    if len(sys.argv) == 2:
        filter = sys.argv[1]

    main(filter)