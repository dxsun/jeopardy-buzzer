# jeopardy-buzzer
Jeopardy buzzer run on local machine (no web hosting), using keys on keyboard


This is a Python-based buzzer system inspired by the game show Jeopardy, designed to support multiple teams. Teams can buzz in using different keys, and the buzzer system enforces a timeout for each team's response. The system also plays sound effects for correct or incorrect answers.

## Requirements

To run this system, you need to install the following dependencies:

1. `pynput` - For capturing keyboard input.
   ```bash
   pip install pynput
   ```

Additionally, you need to have sound files (for correct and incorrect answers) located in the folder specified in `SOUNDS_FOLDER`.

### Sound Files

- Correct Answer Sound: `rightanswer.mp3`
- Incorrect Answer Sound (Louder): `jeopardy-incorrect-answer.mp3`
- Incorrect Answer Sound (Softer): `the-family-feud-buzzer-sound-effect.mp3`

Ensure that these files are present in the specified folder (`SOUNDS_FOLDER`), or update the path accordingly in `Buzzer.py`.

## Usage

### 1. Starting the Buzzer

To start the buzzer system, run the `main.py` script from the command line.

```bash
python main.py -t <team_1> <team_2> ... -b <timeout>
```

Where:
- `-t` or `--teams`: A space-separated list of team names (e.g., `Team A`, `Team B`, etc.). If not provided, the system defaults to `Team 1` and `Team 2`.
- `-b` or `--buzzer_timeout`: The time (in seconds) that a team has to respond after buzzing in. If not provided, it defaults to 5 seconds.

#### Example 1: Two teams with default timeout of 5 seconds
```bash
python main.py -t "Team 1" "Team 2"
```

#### Example 2: Four teams with a buzzer timeout of 7 seconds
```bash
python main.py -t "Team A" "Team B" "Team C" "Team D" -b 7
```

### 2. Buzzer Controls

- Each team has a dedicated key for buzzing in:
  - **Team 1**: `Shift` (Left)
  - **Team 2**: `Shift` (Right)
  - **Team 3**: `Tab`
  - **Team 4**: `Backspace`
  
  If you have fewer teams than the default 4, only the first corresponding keys will work.

- The buzzer system will lock after a team presses their button and cannot be used again until the buzzer is reset.
  
- To reset the buzzer, press the **Spacebar**. This will unlock the buzzer and allow any team to buzz in again.

- To indicate whether a team's answer was correct or incorrect:
  - Press the **Up Arrow** key for a correct answer.
  - Press the **Down Arrow** key for an incorrect answer.
  
  The corresponding sound effect will play for each action.

### 3. Stopping the Buzzer

To exit the system, press the **Esc** key at any time. This will stop the buzzer system and terminate the listener.
