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


def retrieveL(dlen, end):
    return " " * ((end - dlen) - 1)


def menu(info):
    lens = []
    for inf in info:
        lens.append(len(inf))

    most = max(lens)

    distro=info[0]
    cpu=info[1]
    ram=info[2]

    end = len(f"╭━━━━━━━━━━━━━━━━━━{hline * most}╮")
    distrolen = len(f"┃   DISTRO:    {distro}")
    cpulen = len(f"┃      CPU:    {cpu}")
    ramlen = len(f"┃      RAM:    {ram}")

    newdilen = retrieveL(distrolen, end)
    newcplen = retrieveL(cpulen, end)
    newrmlen = retrieveL(ramlen, end)


    spacing = " " * 4
    fields = [
        f"{Fore.YELLOW}{Style.BRIGHT}DISTRO:{Style.RESET_ALL}{Fore.BLUE}{spacing}{distro}{newdilen}{Style.RESET_ALL}{Fore.RESET}",
        f"   CPU:{spacing}{cpu}{newcplen}",
        f"   RAM:{spacing}{ram}{newrmlen}",
    ]

    menu = f"""
╭━━━━━━━━━━━━━━━━━━{hline * most}╮\n"""
    for field in fields:
        menu+=f"┃   {field}┃\n"


    menu+=f"╰━━━━━━━━━━━━━━━━━━{hline * most}╯\n"

    print(menu)


info=["d4", "3s", "5m", "4s"]
menu(info)
