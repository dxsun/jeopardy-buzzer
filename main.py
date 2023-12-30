from Buzzer import Buzzer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buzzer_timeout", help="Time to answer question after buzzing in")
parser.add_argument('-t','--teams', nargs='+', help='Team names')

args = parser.parse_args()
print("Arguments:", vars(args))

if __name__ == "__main__":
	buzzer = Buzzer(args.teams, int(args.buzzer_timeout))
	buzzer.start()