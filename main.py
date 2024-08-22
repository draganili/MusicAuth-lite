import mido
import time

correct_sequence = [60, 62, 64, 65, 67]  # Example: C, D, E, F, G, change it to whatever you want!


def capture_midi_input():
    # Capture MIDI input
    with mido.open_input() as x:
        played_sequence = []
        print("I'm listening...")

        start_time = time.time()
        for msg in x:
            if msg.type == 'note_on' and msg.velocity > 0:
                played_sequence.append(msg.note)
                print(f"Played: {msg.note}")

            # Break after receiving enough notes or after a certain time
            if len(played_sequence) >= len(correct_sequence) or time.time() - start_time > 10:
                break

        return played_sequence


def diff(played_sequence, correct_sequence):
    return played_sequence == correct_sequence


def main():
    played_sequence = capture_midi_input()
    if diff(played_sequence, correct_sequence):
        print("Unlocking the system.")  # do something to unlock the system
    else:
        print("Incorrect melody, the system stays locked.")  # do something else


if __name__ == "__main__":
    main()
