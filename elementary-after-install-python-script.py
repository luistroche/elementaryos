#!/usr/bin/env python
import sys
import subprocess
sud = "sudo"
aptget = "apt-get"
installer = [sud, aptget, "check"]
needed_repositories = ["ppa:webupd8team/java", "ppa:pipelight/stable", "deb http://repository.spotify.com stable non-free"]
needed_repositories_keys = ["94558F59"]
packages = ["git", "gedit", "ssh", "linux-image-generic-lts-sausy", "xserver-xorg-lts-saucy", "libgl1-mesa-glx-lts-saucy", "gufw", "oracle-java7-installer", "libreoffice", "libxss1", "dconf-tools", "hardinfo", "pavucontrol", "spotify-client", "palimpsest"]


subprocess.call(installer)
