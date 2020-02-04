from jira import JIRA
import pprint
from collections import OrderedDict

# Main object = server
jira = JIRA("https://jira.lnd.bz", basic_auth=("jan.simancik", "Medajlon123"))



def get_users_group(jira_group, show=False):
    data = jira.group_members(jira_group)
    converted_users = dict(OrderedDict(data))
    users = []

    for user in converted_users.keys():
        users.append(converted_users[user]['fullname'])

    if show:
        print("\n")
        for user in users:
            print(user)

    return users


# pprint.pprint(get_users("Jira Users"))

def get_groups(filter="", show=False):
    data = jira.groups(filter)

    if show:
        print("\n")
        for groups in range(len(data)):
            print(data[groups])

    return data


def get_all_users(show=False):
    result = list(jira.search_users(searched_user, maxResults=1000, includeInactive=inactive_users))
    print(f"Number of results: {len(result)}\n")

    if show:
        print("\n")
        for i in range(len(result)):
            print(result[i])

        return result


if __name__ == '__main__':
    while True:
        print("\nOptions:\n"
              "1.List all Jira users.\n"
              "2.List all Jira groups.\n"
              "3.Show all users from specific group."
            )
        choice = int(input("Option: "))

        if not choice:
            continue

        elif choice == 1:
            searched_user = input("Enter the pattern for user to search(defaul[all]): ") or "."
            in_users = input("Show inactive users?[y/N]: ") or "No"

            if in_users.lower()[0] == "y":
                inactive_users = True
            else:
                inactive_users = False

            get_all_users(True)

        elif choice == 2:
            search_pattern = input("Pattern for search or blank for all groups: ") or ""
            get_groups(filter=search_pattern, show=True)

        elif choice == 3:
            group = input("Which group?: ")
            get_users_group(group, show=True)





