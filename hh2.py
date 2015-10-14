import argparse
from itertools import count, islice


def generator():
	for num in count(1):
		for c in str(num):
			yield c

def findIdx(iNum):
	iStr = str(iNum)
	charIdx = 0
	sequence = generator()
	for current in sequence:
		charIdx += 1
		iCharIdx = 0
		for iChar in iStr:
			if current != iChar:
				break
			current = next(sequence)
			iCharIdx += 1
		if iCharIdx == len(iStr):
			return charIdx
		charIdx += iCharIdx

def main():
	parser = argparse.ArgumentParser(description='Search index number in an infinite sequence')
	parser.add_argument("num", metavar = "N", type = int, help = "Number")
	args = parser.parse_args()
	print findIdx(args.num)

def print_sequence(num):
    print ''.join(islice(generate_sequence(), 0, num))


if __name__ == "__main__":
    main()

