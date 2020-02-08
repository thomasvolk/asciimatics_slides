from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import NextScene
from asciimatics.event import KeyboardEvent, MouseEvent
import uuid

def slide_scenes(*scenes):
    if len(scenes) == 0:
        return []
    current = scenes[0]
    for s in scenes[1:]:
        current.add_next(s)
        current = s
    return scenes

class SlideSceneContext(object):
    def __init__(self):
        self._scenes = []
    def add_scene(self, scene):
        if len(self._scenes) > 0:
            last = self._scenes[-1]
            last.add_next(scene)
        self._scenes.append(scene)

class SlideScene(Scene):
    def __init__(self, context, effects, duration=0, clear=True, name=None):
        if not name:
            name = str(uuid.uuid4())
        self._predecessor = None
        self._successor = None
        context.add_scene(self)
        super(SlideScene, self).__init__(effects, duration=duration, clear=clear, name=name)
    
    def add_next(self, successor):
        if not isinstance(successor, SlideScene):
            raise TypeError("scene has to be from type: " + str(SlideScene))
        self._successor = successor
        self._successor._predecessor = self
        return successor

    def _forward(self):
        if self._successor:
            raise NextScene(self._successor.name)

    def _backward(self):
        if self._predecessor:
            raise NextScene(self._predecessor.name)

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code in [Screen.KEY_LEFT, Screen.KEY_UP]:
                self._backward()
            if event.key_code in [Screen.KEY_RIGHT, Screen.KEY_DOWN]:
                self._forward()  
        if isinstance(event, MouseEvent):
            if event.buttons == MouseEvent.LEFT_CLICK:
                self._forward()
            if event.buttons == MouseEvent.RIGHT_CLICK:
                self._backward()         
        return super().process_event(event)
    
    @property
    def predecessor(self):
        return self._predecessor
    
    @property
    def successor(self):
        return self._successor