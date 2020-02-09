asciimatics_slides
==================

asciimatics_slides is an extension that makes it possible to navigate back and 
forward trough the scenes of the
`asciimatics library <https://github.com/peterbrittain/asciimatics>`_.

Usage
-----

Use SlideScene and SlideSceneContext to create your scenes:

.. code-block:: python

    from asciimatics.effects import Print
    from asciimatics.screen import Screen
    from asciimatics.renderers import FigletText
    from asciimatics_slides.scene import SlideScene, SlideSceneContext


    def demo(screen):
        context = SlideSceneContext()
        scenes = [
            SlideScene(context, [
                Print(screen, 
                        FigletText("Slide 1", font='big'),
                        int(screen.height / 2 - 16))]),
            SlideScene(context, [
                Print(screen, 
                        FigletText("Slide 2", font='big'),
                        int(screen.height / 2 - 8))]),
            SlideScene(context, [
                Print(screen, 
                        FigletText("Slide 3", font='big'),
                        int(screen.height / 2 - 0))]),
        ]
        screen.play(scenes)

    Screen.wrapper(demo)

see: https://github.com/thomasvolk/asciimatics_slides/tree/master/samples