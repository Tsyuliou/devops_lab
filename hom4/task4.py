import requests
import argparse
import getpass


def rep_info(usr, passwd):
    git_r1 = requests.get(link1, auth=(usr, passwd)).json()
    git_r2 = requests.get(link2, auth=(usr, passwd)).json()
    print(git_r2)
    print("-----------------------------------------------")
    print("Author of this work: {}".format(git_r1["login"]))
    print("-----------------------------------------------")
    print("Title: {}".format(git_r2["title"]))
    print("Created_at: {}".format(git_r2["created_at"]))
    print("Updated_at: {}".format(git_r2["updated_at"]))
    print("Login: {}".format(git_r2["user"]["login"]))
    print("Organizations_url: {}".format(git_r2["user"]["organizations_url"]))
    print("Repos_url: {}".format(git_r2["user"]["followers_url"]))


password = getpass.getpass()
parser = argparse.ArgumentParser(prog='rep_info')
parser.add_argument('username', help='Username to login on github')
parser.add_argument('link1', help='Link to your repo')
parser.add_argument('link2', help='Link to pull request')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
username = args.username
link1 = args.link1
link2 = args.link2

rep_info(username, password)
