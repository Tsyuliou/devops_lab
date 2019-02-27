import requests
import os.path
import configparser

config = configparser.ConfigParser()
config.read("config.txt")
username = config["private"]["username"]
password = config["private"]["password"]
link1 = config["data"]["link1"]
link2 = config["data"]["link2"]
git_r1 = requests.get(link1, auth=(username, password)).json()
git_r2 = requests.get(link2, auth=(username, password)).json()
print("Author of this work: {}".format(git_r1["login"]))


class rep:
    def rep_info(self, usr, passwd):
        git_r2 = requests.get(link2, auth=(usr, passwd)).json()
        '''with open('output.txt', 'a') as file:
            file.write(str(git_r2))'''
        print("ID: %s" % str(git_r2[0]["id"]))
        print("Type: %s" % str(git_r2[0]["type"]))
        print("Actor: %s" % str(git_r2[0]["actor"]))
        print("Login: %s" % str(git_r2[0]["actor"]["login"]))
        print("Display_login: %s" % str(git_r2[0]["actor"]["display_login"]))
        print("Repo: %s" % str(git_r2[0]["repo"]))


if __name__ == '__main__':
   task4 = rep()
   task4.rep_info(username, password)
