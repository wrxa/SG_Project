#coding=utf-8
class Publisher:
    def __init__(self):
        pass

    def register(self):
        pass

    def unregister(self):
        pass

    def notifyAll(self):
        pass 

class TechForum(Publisher):
    def __init__(self):
        self._listOfObj = []
        self.val = None

    def register(self, obj):
        if obj not in self._listOfObj:
            self._listOfObj.append(obj)

    def notifyAll(self):
        for objects in self._listOfObj:
            objects.notify(self.val)
    
    def writeNewPost(self , val):
        self.val = val
        self.notifyAll()


class Subscriber:
    def __init__(self):
        pass

    def notify(self):
        pass
