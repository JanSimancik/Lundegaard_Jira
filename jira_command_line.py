from jira import JIRA
import pprint
from collections import OrderedDict


# Main object = server
jira = JIRA("https://jira.lnd.bz", basic_auth=("jan.simancik", "Medajlon123"))


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


# get_groups(show=True)
def get_all_users():
    data = jira.search_users(".")


print(type(jira.search_users(".")))
# print(jira.client_info())