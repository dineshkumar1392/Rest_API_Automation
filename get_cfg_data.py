# import data from configration file

import configparser
config = configparser.ConfigParser()
# to read data from config file
# for giving path use forward slash /
# and if we use backward slash \ we use r before the path
config.read('./conf/config.cfg')    # we no need to give path of your system
print(config.get('users','user_name'))
print(config.get('users','password'))
