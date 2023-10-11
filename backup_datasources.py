import subprocess
import json

token = "<your-grafana-token>"
host = "<ip-address>:<port>"

# Execute the initial curl command to retrieve the list of datasources
list_command = [
    "curl",
    "-s",
    "-H", f"Authorization: Bearer {token}",
    "-X", "GET",
    f"http://{host}/api/datasources"
]

try:
    list_result = subprocess.run(
        list_command, capture_output=True, text=True, check=True)
    datasources = json.loads(list_result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Initial request failed with error: {e}")
    print("Error output:")
    print(e.stderr)
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
    exit(1)

# Iterate over each datasource ID and execute the detailed curl command
for datasource in datasources:
    datasource_id = datasource.get("id")
    if datasource_id:
        detail_command = [
            "curl",
            "-s",
            "-H", f"Authorization: Bearer {token}",
            "-X", "GET",
            f"http://{host}/api/datasources/{datasource_id}"
        ]
        try:
            detail_result = subprocess.run(
                detail_command, capture_output=True, text=True, check=True)
            detail_json = json.loads(detail_result.stdout)
            filename = f"{datasource_id}.json"

            with open(filename, "w") as f:
                json.dump(detail_json, f, indent=4)

            print(
                f"Details for datasource with ID {datasource_id} saved as {filename}")
        except subprocess.CalledProcessError as e:
            print(
                f"Detail request failed for datasource with ID {datasource_id} with error: {e}")
            print("Error output:")
            print(e.stderr)
