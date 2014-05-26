#!/usr/bin/env python
#ver 0.1 
#non-classes
#simple variables and funtions.
import sys
import subprocess

yo = "sudo"
caller = subprocess.call
def update(): 
	return subprocess.call([yo, aptget, "update"])
def upgrade():
	return subprocess.call([yo, aptget, y, "upgrade"])
def autoremove():
	return subprocess.call([yo, aptget, y, "autoremove"])
def autoclean():
	return subprocess.call([yo, aptget, y, "autoclean"])
def autocheck():
	return subprocess.call([yo, aptget, y, "check"])
aptget = "apt-get"
aptadd = "apt-add-repository"
aptkey = ("apt-key", "adv", "--keyserver", "keyserver.ubuntu.com", "--recv-keys")
installer = [yo, aptget]
needed_repositories = ["ppa:webupd8team/java","ppa:pipelight/stable", "ppa:versable/elementary-update", "deb http://repository.spotify.com stable non-free"]

repo_keys = ["94558F59"]

system_packages = ["linux-image-generic-lts-sausy", "xserver-xorg-lts-saucy", "libgl1-mesa-glx-lts-saucy"]
regular_packages = ["git", "gedit", "gedit-plugins", "ssh", "gufw", "oracle-java7-installer", "libreoffice", "libxss1", "dconf-tools", "hardinfo", "pavucontrol", "thunderbird", "firefox", "chromium-browser", "vlc", "flashplugin-installer", "gnome-disk-utility", "gtk2-engines-pixbuf", "spotify-client",]
y = "-y"
checker = True
counter = ""

def add_repo(repo):
	 return subprocess.call([yo, "apt-add-repository", y, repo])
     
def add_key(key):
    return subprocess.call([yo, "apt-key", "adv", "--keyserver", "keyserver.ubuntu.com", "--recv-keys", key])

def apt_get(package):
	return subprocess.call([yo, aptget, "install", y, package])

if checker:
    counter = len(needed_repositories)
    print "counter is:", counter
    
    if counter >= 1:
        for i in needed_repositories:
             add_repo(i)
             counter -= 1
             print "now counter is:", counter
             if counter == 0:
                checker = False
        update()
        upgrade()
        autocheck()        
        print "Repositories added to source list"
if not checker:
        for item in repo_keys:
            add_key(item)
	update()
        print "Repositories Keys added"
        for pack in regular_packages:
            apt_get(pack)
        print "All Packages Installed"

autocheck()
autoremove()
autoclean()
autocheck()

print "The End"


# The End


        
