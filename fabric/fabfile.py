from fabric.api import *
from fabric.contrib.console import confirm


env.hosts = [
    'ubuntu@123.206.220.149',

]

# env.passwords = {
#     'ubuntu@123.206.220.149': '',
# }

def reboot():
    run("sudo reboot")

def up():
    run("git clone https://github.com/persontianshuang/mafter.git")
    cd("mafter")
    run("nohup gunicorn -w4 -b 0.0.0.0:8768 api:api &")
    cd("../")
    run("supervisord -c /home/ubuntu/nihongo1/supervisord.conf")


def echo():
    run("apt-get update")
    run("export LC_ALL=C")
    run("apt install python3-pip -y")
    run("apt install git")
    run("pip3 install pymongo redis requests lxml gevent")
    run("git clone https://github.com/persontianshuang/crapy500m.git")
    run("ls")
