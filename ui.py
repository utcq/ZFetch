from colorama import *

class DistroIcons:
    linux=""
    almalinux=""
    alpine=""
    aosc="" # TODO Restore symbol
    apple=""
    archlabs=""
    arch=""
    artix=""
    budgie=""
    centos=""
    coreos=""
    debian=""
    deepin=""
    devuan=""
    docker=""
    elementary=""
    endevour=""
    fedora=""
    freebsd=""
    gentoo=""
    guix=""
    kali=""
    mint=""
    manjaro=""
    nixos=""
    openbsd=""
    opensuse=""
    parrot=""
    popos=""
    raspi=""
    slackware=""
    solus=""
    ubuntu=""
    void=""
    zorin=""
    windows=""

vline="┃"
hline="━"

#   ╭  ╮    ╰  ╯
 

info = ["^d", "&dz", "l09dfdessd38uhuhffd", "83d"]
lens = []
for inf in info:
    lens.append(len(inf))

most = max(lens)
# print(most)

distro=info[0]
cpu=info[1]
ram=info[2]

end = len(f"╭━━━━━━━━━━━━━━━━━━{hline * most}╮")
distrolen = len(f"┃   DISTRO:    {distro}")
cpulen = len(f"┃      CPU:    {cpu}")
ramlen = len(f"┃      RAM:    {ram}")

newdilen = " " * ((end - distrolen) - 1)
newcplen = " " * ((end - cpulen) - 1)
newrmlen = " " * ((end - ramlen) - 1)

menu = f"""
╭━━━━━━━━━━━━━━━━━━{hline * most}╮
┃   DISTRO:    {distro}{newdilen}┃
┃      CPU:    {cpu}{newcplen}┃
┃      RAM:    {ram}{newrmlen}┃
╰━━━━━━━━━━━━━━━━━━{hline * most}╯
"""

print(menu)