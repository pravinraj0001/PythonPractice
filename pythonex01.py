from queue import Queue as q
import inspect

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
        self.put(item)

qu = Queue()
qu +9
print(qu)
