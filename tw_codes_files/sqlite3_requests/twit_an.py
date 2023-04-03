import sys
import argparse

def CreateParser():
    parser = argparse.ArgumentParser
    parser.add_argument('-f', choices=Lf, required=True)
    parser.add_argument('-R', choices=LR, required=True)
    parser.add_argument('-D', choices=LD, required=True)
    parser.add_argument('-H', choices=LH, required=True)

if __name__ == '__main__':
