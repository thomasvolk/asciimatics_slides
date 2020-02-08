from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics_slides.scene import SlideScene, SlideSceneGenerator
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

def _simple(screen):
    centre = (screen.width // 2, screen.height // 2)

    root_scene = SlideScene([_speak(screen, "Slide 1", centre)]).add_next(
        SlideScene([_speak(screen, "Slide 2", centre)])).add_next(
            SlideScene([_speak(screen, "Slide 3", centre)])).root()

    screen.play([s for s in SlideSceneGenerator(root_scene)], stop_on_resize=True)

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(_simple)
            sys.exit(0)
        except ResizeScreenError:
            pass
