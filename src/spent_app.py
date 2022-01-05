from docopt import docopt
from setup import *
from tabulate import tabulate
from colorama import Fore, Style, Back


usage = '''
Usage:
    spent_app.p --init
    spent_app.p --show [<category>]
    spent_app.p --add <amount> <category> [<message>]
    spent_app.p --remove <category>
    spent_app.py -h | --help
    
Options:
    --init          Initialize the database
    --show          Show all expenses or expenses of a specific category
    --add           Add an expense
    --remove        Remove an expense
    --version       Show version

'''


args = docopt(usage, options_first = True , version='spent_app.py 1.0', help=True)

if args['--init']:
    init()
    print(f'{Back.LIGHTGREEN_EX}{Fore.BLACK}Successfully{Back.RESET}{Fore.RESET}')
    
if args['--show']:
    category = args['<category>']
    amount, results = show(category)
    print('Total amount:', amount)
    print(tabulate(results))
    
if args['--add']:
    try:
        amount = float(args['<amount>'])  
        add(amount , args['<category>'] , args['<message>']) 
        print(f'{Back.LIGHTGREEN_EX}{Fore.BLACK}Item added {Back.RESET}{Fore.RESET}')
    except:
        print(usage, f'{Fore.RESET}')    
        
if args['--remove']:
    try:
        remove(args['<category>'])
        print(f'{Back.LIGHTGREEN_EX}{Fore.BLACK}Item removed {Back.RESET}{Fore.RESET}')
    except:
        print(usage, f'{Fore.RESET}')