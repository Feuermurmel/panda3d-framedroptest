from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import CardMaker, PandaNode, Point3


def main():
    base = ShowBase()

    cm = CardMaker('')
    cm.set_frame(-.5, .5, -.5, .5)

    # Node which contains all the cards equally spaced apart and which is
    # animated to move the cards in front of the camera.
    cards = base.render.attach_new_node(PandaNode(''))
    cards.setPos(-2, 5, 0)
    cards.posInterval(2, Point3(-6, 5, 0)).loop()

    for i in range(5):
        card = cards.attach_new_node(cm.generate())
        card.setPos(i * 2, 0, 0)

    def on_every_frame(task):
        # Time which has elapsed since the last frame measured in units of
        # the time quota available at 60 fps (e.g. 1/60 second).
        time_quota = taskMgr.globalClock.get_dt() * 60

        # Print time use as percent of the 60-fps-quota.
        print(f'{round(time_quota * 100):4}', end='', flush=True)

        return Task.DSCont

    taskMgr.add(on_every_frame)
    taskMgr.run()
