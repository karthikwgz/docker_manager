import docker as d
import time
from rich import print,box
from datetime import datetime
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.console import Console
from rich.live import Live

console = Console()

grid = Table.grid(expand=True)
grid.add_column(justify="center", ratio=1)
grid.add_column(justify="right")
grid.add_row(
    "Docker Management Tool",
    datetime.now().ctime().replace(":", "[blink]:[/]"),
)
print(Panel(grid, style="white on blue"))

def fn_menu():
    grid1 = Table(expand=True,border_style="white")
    grid1.add_column("[purple]Choice[purple]",justify="right",style="purple")
    grid1.add_column("[purple]Details[purple]",justify="center",style="purple")
    grid1.add_row(
        "1","Download New Image"
    )
    grid1.add_row(
        "2","Run Container"
    )
    grid1.add_row(
        "3","Status of Containers"
    )
    grid1.add_row(
        "4","Network Details"
    )
    grid1.add_row(
        "5","Modify Network"
    )
    grid1.add_row(
        "6","Exit"
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")

def dwn_rich(img):
    di = d.download_image(img)
    
    table = Table(border_style="bright_red")
    table.add_column("Status",style="bright_cyan")
    
    with Live(table, refresh_per_second=1):
        for res in di.split("\n"):
            table.add_row(str(res))
            time.sleep(1.0)
    choice()

def get_img():
    x = input("Enter Image name :")
    return(x)

def get_cntnr():
    x = input("Enter Container name :")
    return(x)

def get_nt():
    x = input("Enter Network :")
    return(x)

def stat_rich():
    ds = d.docker_status()
    table = Table(border_style="bright_red")
    table.add_column("Status",style="bright_cyan")
    
    with Live(table, refresh_per_second=1):
        for res in ds.split("\n"):
            table.add_row(str(res))
            time.sleep(1.0)
    choice()

def netd_rich():
    netd = d.network_details()
    table = Table(border_style="bright_red")
    table.add_column("response",style="bright_cyan")
    
    with Live(table, refresh_per_second=1):
        for res in netd.items():
            table.add_row(str(res))
            time.sleep(1.0)

    choice()

def netmod():
    table = Table(border_style="bright_red")
    table.add_column("networks",style="bright_cyan")
    
    with Live(table, refresh_per_second=1):
        for res in d.list_netwrok().split("\n"):
            table.add_row(str(res))
            time.sleep(1.0)

    d.disconnect_network(get_cntnr(),get_nt())
    print("disconnected..")
    d.connect_network(get_cntnr(),get_nt())
    print("connected to new network")
    choice()

def choice():
    fn_menu()
    ch = int(input())
    if ch == 1:
        dwn_rich(get_img())
    elif ch == 2:
        d.run_container(get_cntnr(),get_img())
        choice()
    elif ch == 3:
        stat_rich()
    elif ch == 4:
        netd_rich()
    elif ch == 5:
        netmod()
    elif ch == 6:
        exit()
    else:
        print("\n invalid choice")
        choice()

choice()