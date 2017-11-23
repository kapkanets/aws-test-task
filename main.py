import datetime
import json
import os
import random
import subprocess
from pprint import pprint
now = datetime.datetime.now()
now2 = now.strftime("%Y-%m-%d") #-%H-%M
from datetime import datetime, timedelta
N =7
date_N_days_ago = datetime.now() - timedelta(days=N)

#print date_N_days_ago
typesofenv = ["Production", "Development" ,"Staging" ,"Backup" ,"Testing"]
# for SS in range(5):
#     RR = random.randint(0, 4)
#     ec2_output = typesofenv[RR]
#     print ec2_output
#     DD = subprocess.Popen(['aws', 'ec2', 'run-instances', '--image-id', 'ami-e28d098d', '--count', \
#                         '1', '--instance-type', 't2.nano', '--key-name', 'kapkanets-work', '--security-groups',\
#                         '--tag-specifications', 'ResourceType=instance,Tags=[{Key=Name,Value=Server-' + ec2_output + '},{Key=Environment,Value=' + ec2_output + '}]'],\
#                        stdout=subprocess.PIPE)





desc_ec2 = subprocess.Popen(['aws', 'ec2', 'describe-instances'], stdout=subprocess.PIPE)
desc_ec2output, err = desc_ec2.communicate()
data = json.loads(desc_ec2output)
lenec2  = len(data['Reservations'])
print lenec2
tag_lenght = len(data['Reservations'][0]['Instances'][0]['Tags'])
print tag_lenght
for i in range(lenec2):
    # allhostList = []
    # allhostList.append(data['Reservations'][i]['Instances'][0]['InstanceId'])
    # allhostList.append(data['Reservations'][i]['Instances'][0]['State']['Name'])
    # allhostList.append(data['Reservations'][i]['Instances'][0]['Tags'][0]['Value'])
    # allhostList.append(data['Reservations'][i]['Instances'][0]['LaunchTime'])
    # print(allhostList)
    for z in range(tag_lenght):
        if data['Reservations'][i]['Instances'][0]['Tags'][z]['Value'] == 'Backup':
            hostList = []
            hostList.append(data['Reservations'][i]['Instances'][0]['InstanceId'])
            hostList.append(data['Reservations'][i]['Instances'][0]['State']['Name'])
            hostList.append(data['Reservations'][i]['Instances'][0]['Tags'][z]['Value'])
            hostList.append(data['Reservations'][i]['Instances'][0]['LaunchTime'])
            print(hostList)

# #################################################
#
# DDDDD = subprocess.Popen(['aws', 'ec2', 'create-image','--instance-id', hostList[0], '--name', hostList[0]+'-'+now2,'--no-reboot'],stdout=subprocess.PIPE)
desc_ami = subprocess.Popen(['aws', 'ec2', 'describe-images','--owners','865884215240'], stdout=subprocess.PIPE)
desc_amioutput, err = desc_ami.communicate()
data_ami = json.loads(desc_amioutput)
data_ami_len = len(data_ami['Images'])
#
# ##################################################

for e in range(data_ami_len):
    amiList = []
    amiList.append(data_ami['Images'][e]['ImageId'])
    amiList.append(data_ami['Images'][e]['Name'])
    amiList.append(data_ami['Images'][e]['CreationDate'])
    amiList.append(data_ami['Images'][e]['BlockDeviceMappings'][0]['Ebs']['SnapshotId'])
    print(amiList)
    if data_ami['Images'][e]['CreationDate'] not in now2:
         #print "Hello World"
         del_ami = subprocess.Popen(['aws', 'ec2', 'deregister-image', '--image-id', amiList[0]],stdout=subprocess.PIPE)
         del_amioutput, err = del_ami.communicate()
         del_snap = subprocess.Popen(['aws', 'ec2', 'delete-snapshot', '--snapshot-id', amiList[3]],stdout=subprocess.PIPE)
         del_snapoutput, err = del_snap.communicate()














#' + ec2_output + '

## result = [x[0] for x in LL.values() if x[2] == 'Backup']
#
#print(result)
#
#
# print output_date
# LL = [x['Instances'][0]['InstanceId'] for x in data['Reservations'] if x['Instances'][0]['Tags'][0]['Value'] == 'Backup']\
#       and x['Instances'][0]['State']['Name'] == 'running'


# data = json.load(open('ec2.json'))
# p = subprocess.Popen(['date', '+%Y-%m-%d:%H:%M:%S'])
# output_date, errors = p.communicate()
# DD = subprocess.Popen(['aws', 'ec2', 'run-instances', '--image-id', 'ami-e28d098d', '--count', \
#                        '1', '--instance-type', 't2.nano', '--key-name', 'kapkanets-work', '--security-groups',\
#                        '--tag-specifications', 'ResourceType=instance,Tags=[{Key=Name,Value=Server-Backup},{Key=Environment,Value=Backup}]'],\
#                       stdout=subprocess.PIPE)