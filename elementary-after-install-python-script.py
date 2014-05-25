#!/usr/bin/env python
#ver 0.1 
#non-classes
#simple variables and funtions.
import sys
import subprocess
sud = "sudo"
aptget = "apt-get"
aptadd = "apt-add-repository"
aptkey = ["apt-key", "adv", "--keyserver", "keyserver.ubuntu.com", "--recv-keys"]
installer = [sud, aptget,"-y"]
needed_repositories = ["ppa:webupd8team/java","ppa:pipelight/stable", "deb http://repository.spotify.com, stable non-free"]

needed_repositories_keys = ["94558F59"]

system_packages = ["linux-image-generic-lts-sausy", "xserver-xorg-lts-saucy", "libgl1-mesa-glx-lts-saucy"]
regular_packages = ["git", "gedit", "ssh", "gufw", "oracle-java7-installer", "libreoffice", "libxss1", "dconf-tools", "hardinfo", "pavucontrol", "spotify-client", "palimpsest"]

checker = True

def repository(repo):
	return subprocess.call(aptadd, "-y", repo)

def apt_get(package):
	return subprocess.call(installer, "-y", package)

for i in needed_repositories:
		repository(i)

#subprocess.call()
