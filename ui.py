from colorama import *


class DistroIcons:
    linux = ""
    almalinux = ""
    alpine = ""
    aosc = ""  # TODO Restore symbol
    apple = ""
    archlabs = ""
    arch = ""
    artix = ""
    budgie = ""
    centos = ""
    coreos = ""
    debian = ""
    deepin = ""
    devuan = ""
    docker = ""
    elementary = ""
    endevour = ""
    fedora = ""
    freebsd = ""
    gentoo = ""
    guix = ""
    kali = ""
    mint = ""
    manjaro = ""
    nixos = ""
    openbsd = ""
    opensuse = ""
    parrot = ""
    popos = ""
    raspi = ""
    slackware = ""
    solus = ""
    ubuntu = ""
    void = ""
    zorin = ""
    garuda=""
    windows = ""


vline = "┃"
hline = "━"


#   get spacing between info and menu end
def retrieveL(dlen, end):
    return " " * ((end - dlen) - 1)

# shows menu


def menu(info):
    # get largest info
    lens = []
    for inf in info:
        lens.append(len(inf))

    most = max(lens)

    # get info variables

    distro = info[0]
    cpu = info[1]
    ram = info[2]
    gpu = info[3]
    wm = info[4]
    #pkgs = info[5]
    uptime = info[5]
    kernel = info[6]

    end = len(f"╭━━━━━━━━━━━━━━━━━━{hline * most}╮")
    distrolen = len(f"┃   DISTRO:    {distro}")
    cpulen = len(f"┃      CPU:    {cpu}")
    ramlen = len(f"┃      RAM:    {ram}")
    gpulen = len(f"┃      GPU:    {gpu}")
    wmlen = len(f"┃    WM/DE:    {wm}")
    #pkgslen = len(f"┃     PKGS:    {pkgs}")
    uptimelen = len(f"┃   UPTIME:    {uptime}")
    kernellen = len(f"┃   KERNEL:    {kernel}")

    newdilen = retrieveL(distrolen, end)
    newcplen = retrieveL(cpulen, end)
    newrmlen = retrieveL(ramlen, end)
    newgplen = retrieveL(gpulen, end)
    newwmlen = retrieveL(wmlen, end)
    #newpklen = retrieveL(pkgslen, end)
    newuplen = retrieveL(uptimelen, end)
    newkelen = retrieveL(kernellen, end)

    spacing = " " * 4

    #               To Update:      Replace DISTRO:                               Replace distro      Replace new*len
    fields = [
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3mDISTRO:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{distro}{newdilen}{Style.RESET_ALL}{Fore.RESET}",
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3m   CPU:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{cpu}{newcplen}{Style.RESET_ALL}{Fore.RESET}",
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3m   RAM:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{ram}{newrmlen}{Style.RESET_ALL}{Fore.RESET}",
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3m   GPU:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{gpu}{newgplen}{Style.RESET_ALL}{Fore.RESET}",
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3m WM/DE:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{wm}{newwmlen}{Style.RESET_ALL}{Fore.RESET}",
        #f"{Fore.YELLOW}{Style.BRIGHT}\033[3m  PKGS:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{pkgs}{newpklen}{Style.RESET_ALL}{Fore.RESET}",
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3mUPTIME:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{uptime}{newuplen}{Style.RESET_ALL}{Fore.RESET}",
        f"{Fore.YELLOW}{Style.BRIGHT}\033[3mKERNEL:{Style.RESET_ALL}\033[0m{Fore.BLUE}{spacing}{kernel}{newkelen}{Style.RESET_ALL}{Fore.RESET}",


    ]

    menu = f"""
╭━━━━━━━━━━━━━━━━━━{hline * most}╮\n"""
    for field in fields:
        menu += f"┃   {field}┃\n"

    menu += f"╰━━━━━━━━━━━━━━━━━━{hline * most}╯\n"

    print(menu)


info = ["Gentoo", "Threadripper 5000WX 5.2GHz", "128GB", "Nvidia RTX 4090",
        "DWM", "5 Hours, 28 mins", "5.19.7-zen2-1-zen"]
menu(info)
