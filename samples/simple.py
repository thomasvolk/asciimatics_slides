import sys
from asciimatics.effects import Print
from asciimatics.screen import Screen
from asciimatics.renderers import FigletText
from asciimatics.exceptions import ResizeScreenError
from asciimatics_slides.scene import SlideScene, SlideSceneContext

def demo(screen):
    context = SlideSceneContext()
    scenes = [
        SlideScene(context, [
            Print(screen, 
                    FigletText("Slide 1", font='big'),
                    int(screen.height / 2 - 15))]),
        SlideScene(context, [
            Print(screen, 
                    FigletText("Slide 2", font='big'),
                    int(screen.height / 2 - 12))]),
        SlideScene(context, [
            Print(screen, 
                    FigletText("Slide 3", font='big'),
                    int(screen.height / 2 - 9))]),
        SlideScene(context, [
            Print(screen, 
                    FigletText("Slide 4", font='big'),
                    int(screen.height / 2 - 6))]),
        SlideScene(context, [
            Print(screen, 
                    FigletText("Slide 5", font='big'),
                    int(screen.height / 2 - 3))]),
        SlideScene(context, [
            Print(screen, 
                    FigletText("Slide 6", font='big'),
                    int(screen.height / 2 - 0))]),
    ]
    screen.play(scenes)

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass
