from configparser import ConfigParser
import configparser
import os
import json

def get_accountinfo():
    print("enter email")
    username = input()
    print("enter password")
    password = input()
    accountInfo = [username, password]
    return accountInfo

file = '../../config/config.ini'
config = ConfigParser()

# create folder two directories up (out of repo)
if not os.path.exists('../../config'):
    os.mkdir('../../config')
    open(file , 'w').close
    config.read(file)
    '''
    configUpdate = configparser.RawConfigParser()
    configUpdate.add_section('Account')
    accountInfo = get_accountinfo
    configUpdate.set('Account', 'name', ''.join(accountInfo))
    with open(file, 'w') as file:
        configUpdate.write(file)'''
    config.add_section('Account')
    accountInfo = get_accountinfo()
    for i in accountInfo:
        print(i)
    config.set('Account', 'username', accountInfo[0])
    config.set('Account', 'password', accountInfo[1])
    with open(file, 'w') as file:
        config.write(file)






