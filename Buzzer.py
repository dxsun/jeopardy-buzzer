from pynput.keyboard import Key, Listener
import os
import sys
import time

louder_buzzer = "jeopardy-incorrect-answer.mp3"
softer_buzzer = "the-family-feud-buzzer-sound-effect.mp3"
locked_buzzer_message = "Buzzer is locked, press space to unlock"

class Buzzer:
    def __init__(self, team1, team2):
        print("Team {} presses the left shift button to buzz in. Team {} presses the right shift button to buzz in".format(team1, team2))
        self.team1 = team1
        self.team2 = team2
        self.buzzer_locked = False
        self.listener = None

        # Collect events until listener is released
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

    def on_press(self, key):
        if key == Key.shift:
            if not self.buzzer_locked:
                print("Team {} pressed".format(self.team1))
                self.buzzer_locked = True
                os.system('say "Team ' + self.team1 + '"')
            else:
                print(locked_buzzer_message)
        elif key == Key.shift_r:
            if not self.buzzer_locked:
                print("Team {} pressed".format(self.team2))
                self.buzzer_locked = True
                os.system('say "Team ' + self.team2 + '"')
            else:
                print(locked_buzzer_message)


        elif key == Key.space:
            self.buzzer_locked = False
            print("Reset buzzer")
        elif key == Key.up:
            print("CORRECT")
            os.system('afplay "/Users/dansun/Downloads/rightanswer.mp3"')
        elif key == Key.down:
            print("INCORRECT")
            # os.system('afplay "/Users/dansun/Downloads/{}"'.format(softer_buzzer))
            os.system('afplay "/Users/dansun/Downloads/{}"'.format(louder_buzzer))
            

    def on_release(self, key):
        if key == Key.esc and self.listener:
            self.listener.stop()


team1 = "1"
team2 = "2"
if len(sys.argv) == 3:
    team1 = sys.argv[1]
    team2 = sys.argv[2]
    print("Teams are {} and {}".format(team1, team2))
else:
    print("No team names specified, defaulting to Team 1 and Team 2")

a = Buzzer(team1, team2)
