#!/usr/bin/env python
import sys
import subprocess
sud = "sudo"
aptget = "apt-get"
installer = [sud, aptget, "check"]
packages = []


subprocess.call(installer)
