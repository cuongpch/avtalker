from argparse import ArgumentParser

def total(name):
    print("Hello: "+name)
def main(args):
    name=args.name
    total(name)
if __name__ == '__main__':
    parser = ArgumentParser()  
    parser.add_argument("--name", default='Boss', help="some messsage")
    args = parser.parse_args()
    main(args)