

import os
import pygame


def speak(data):
    voice1 = "en-GB-SoniaNeural"
    voice = "zu-ZA-ThandoNeural"

    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 100
    chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]

    # Convert and play each chunk
    for chunk in chunks:
        text = ' '.join(chunk)
        command1 = f'edge-tts --voice "{voice1}" --text "{text}" --write-media "C:\\Users\\Hites\\Documents' \
                   f'\\Project_sam-6\\database\\data.mp3" '
        os.system(command1)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    return True




if __name__ == '__main__':
    speak("hello")
