import os
import requests

# Get all existing labels in the repository
all_existing_labels = []
debug = []
for retry_count in range(3):
    response = requests.get('https://api.github.com/repos/wso2/api-manager/labels', headers={"Accept": "application/vnd.github.v3+json"})
    if response.status_code == 200:
        for label in response.json():
            all_existing_labels.append(label["name"])
        break
    else:
        continue
else:
    exit(0)

# Get affected component
i = os.environ["ISSUE_BODY"].index("### Affected Component") + 23
j = os.environ["ISSUE_BODY"].index("### Version")
component = os.environ["ISSUE_BODY"][i:j].strip()
component_label = "Component/" + component
debug.append(component_label)
if component_label in all_existing_labels:
    labels.append(component_label)

# Get component version
version = os.environ["ISSUE_BODY"][j+13:j+18].strip()
affected_label = "Affected/" + component + "-" + version
debug.append(affected_label)
if affected_label in all_existing_labels:
    labels.append(affected_label)

print(debug)
# Return verified labels
# if len(labels) > 0:
#     print(",".join(labels))
# else:
#     print("Missing/Component")
