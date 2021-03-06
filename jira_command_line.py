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


pprint.pprint(get_users("Jira Users"))