from jira import JIRA
import pprint
from collections import OrderedDict


# Main object = server
jira = JIRA("https://jira.lnd.bz", basic_auth=("jan.simancik", "Medajlon123"))


searched_user = input("Enter to pattern for user to search(defaul[all]): ") or "."
inactive_users = input("Show inactive users?[y/N]: ") or "No"


if inactive_users.lower()[0] == "y":
    inactive_users = True
else:
    inactive_users = False


def get_users(group):
    data = jira.group_members(group)
    converted_users = dict(OrderedDict(data))
    users = []

    for user in converted_users.keys():
        users.append(converted_users[user]['fullname'])

    return users


# pprint.pprint(get_users("Jira Users"))

def get_groups(filter="", show=False):
    data = jira.groups(filter)

    if show:
        for group in range(len(data)):
            print(data[group])

    return data


def get_all_users(show=False):
    result = list(jira.search_users(searched_user, maxResults=1000, includeInactive=inactive_users))
    print(f"Number of results: {len(result)}\n")

    if show:
        for i in range(len(result)):
            print(result[i])

        return result


get_all_users(True)
