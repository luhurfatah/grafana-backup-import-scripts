import subprocess
import json
import os

# Replace these variables with your actual values
token = "<your-grafana-token>"
host = "<ip-address>:<port>"
grafana_dashboards_folder = "backup"

# Command to retrieve the list of UIDs
list_uids_command = f'curl -sSL -k -H "Authorization: Bearer {token}" "{host}/api/search?query=&" | jq -r \'.[] | select(.type == "dash-db") | .uid\''

try:
    # Retrieve the list of UIDs
    result_uids = subprocess.run(
        list_uids_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result_uids.returncode == 0:
        uids = result_uids.stdout.decode('utf-8').strip().split('\n')

        # Iterate through each UID
        for uid in uids:
            dashboard_command = f'curl -sSL -k -H "Authorization: Bearer {token}" "{host}/api/dashboards/uid/{uid}"'
            result_dashboard = subprocess.run(
                dashboard_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result_dashboard.returncode == 0:
                dashboard_info = json.loads(
                    result_dashboard.stdout.decode('utf-8'))

                # Extract slug and folderTitle
                slug = dashboard_info['dashboard']['uid']
                folder = dashboard_info['meta']['folderTitle']

                # Create folder if it doesn't exist
                folder_path = os.path.join(grafana_dashboards_folder, folder)
                os.makedirs(folder_path, exist_ok=True)

                # Save the dashboard info to a file
                file_name = os.path.join(folder_path, f'{slug}.json')
                with open(file_name, 'w') as file:
                    json.dump(dashboard_info, file, indent=2)

                print(f"Dashboard UID: {uid}")
                print(f"Saved to: {file_name}")
                print("-" * 40)
            else:
                print(f"Error retrieving dashboard info for UID: {uid}")
                print(result_dashboard.stderr.decode('utf-8'))
    else:
        print("Error retrieving the list of UIDs.")
except Exception as e:
    print("An error occurred:", str(e))
