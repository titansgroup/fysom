import unittest
from cPickle import dumps, loads

from fysom import Fysom


class PicklingTestCase(unittest.TestCase):
    def test_pickling(self):

        fsm = Fysom({
            'initial': 'green',
            'events': [
                {'name': 'warn', 'src': 'green', 'dst': 'yellow'},
                {'name': 'panic', 'src': 'yellow', 'dst': 'red'},
                {'name': 'calm', 'src': 'red', 'dst': 'yellow'},
                {'name': 'clear', 'src': 'yellow', 'dst': 'green'}
            ]
        })

        pickled = dumps(fsm)
        assert pickled
        fsm = loads(pickled)

        self.assertTrue(isinstance(fsm, Fysom))
        self.assertEquals('green', fsm.current)

        fsm.warn()
        pickled = dumps(fsm)
        assert pickled
        fsm = loads(pickled)

        self.assertEquals('yellow', fsm.current)
