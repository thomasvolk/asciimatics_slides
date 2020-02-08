from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics_slides.scene import SlideScene, slide_scenes
from asciimatics.renderers import SpeechBubble, FigletText, Box
from asciimatics.exceptions import ResizeScreenError
import sys

def _speak(screen, text, pos):
    return Print(
        screen,
        SpeechBubble(text, uni=screen.unicode_aware),
        x=pos[0], y=pos[1],
        colour=Screen.COLOUR_CYAN,
        clear=True)

def _slide(screen, text):
    centre = (screen.width // 2, screen.height // 2)
    return SlideScene([_speak(screen, text, centre)])

def _simple(screen):
    scenes = slide_scenes(
      _slide(screen, "Slide 1"),
      _slide(screen, "Slide 2"),
      _slide(screen, "Slide 3"),
      _slide(screen, "Slide 4"),
      _slide(screen, "Slide 5")
    )

    screen.play(scenes, stop_on_resize=True)

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(_simple)
            sys.exit(0)
        except ResizeScreenError:
            pass
