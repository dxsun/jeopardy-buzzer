from pynput.keyboard import Key, Listener
import os
from threading import Timer

LOUDER_INCORRECT_ANSWER = "jeopardy-incorrect-answer.mp3"
SOFTER_INCORRECT_ANSWER = "the-family-feud-buzzer-sound-effect.mp3"
CORRECT_ANSWER = "rightanswer.mp3"
LOCKED_BUZZER_MESSAGE = "Buzzer is locked, press space to unlock"
SOUNDS_FOLDER = "/Users/dansun/Downloads/"
DEFAULT_BUZZER_TIMEOUT = 5
BUZZER_BUTTONS = [Key.shift, Key.shift_r, Key.tab, Key.backspace]

class Buzzer:
    def __init__(self, teams, buzzer_timeout=DEFAULT_BUZZER_TIMEOUT):
        self.teams = teams if teams else ["1", "2"]
        if not teams:
            print("No team names specified, defaulting to Team 1 and Team 2")
        else:
            print("Teams are {}".format(self.teams))

        self.team_buzzer_keys = BUZZER_BUTTONS[:len(self.teams)]
        self.buzzer_locked = False
        self.buzzer_timeout = buzzer_timeout
        self.listener = None
        
    def start(self):
        # Collect events until listener is released
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

    def on_press(self, key):
        print("Key:", str(key))
        for i in range(len(self.teams)):
            if key == self.team_buzzer_keys[i]:
                self.team_buzz(self.teams[i])

        if key == Key.space:
            self.buzzer_locked = False
            print("Reset buzzer")
        elif key == Key.up:
            print("CORRECT")
            os.system('afplay "{}{}"'.format(SOUNDS_FOLDER, CORRECT_ANSWER))
        elif key == Key.down:
            print("INCORRECT")
            os.system('afplay "{}{}"'.format(SOUNDS_FOLDER, LOUDER_INCORRECT_ANSWER))
            
    def on_release(self, key):
        if key == Key.esc and self.listener:
            self.listener.stop()

    def team_buzz(self, team):
        if not self.buzzer_locked:
            print("Team {} pressed".format(team))
            self.buzzer_locked = True
            os.system('say "Team ' + team + '"')
            t = Timer(self.buzzer_timeout, self.release_buzzer)
            t.start()
        else:
            print(LOCKED_BUZZER_MESSAGE)

    def release_buzzer(self):
        print("Buzzer released")
        self.buzzer_locked = False