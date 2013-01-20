import unittest

from fysom import Fysom, FysomError


class StatesTestCase(unittest.TestCase):
    def setUp(self):
        self.fsm = Fysom({
            'initial': 'green',
            'events': [
                {'name': 'warn', 'src': 'green', 'dst': 'yellow'},
                {'name': 'panic', 'src': 'yellow', 'dst': 'red'},
                {'name': 'calm', 'src': 'red', 'dst': 'yellow'},
                {'name': 'clear', 'src': 'yellow', 'dst': 'green'}
            ]
        })

    def test_invalid_state(self):
        self.assertRaises(AttributeError, getattr, self.fsm, 'wtfbbq')

    def test_state_conditions(self):
        """
        This will check for example, if state is in clear, will be able to emit
        warn and will not be able to emit panic, calm or clear again.
        """
        self.assertTrue(self.fsm.isstate('green'))
        self.assertTrue(self.fsm.can('warn'))
        self.assertFalse(self.fsm.can('panic'))
        self.assertFalse(self.fsm.can('clam'))
        self.assertFalse(self.fsm.can('clear'))

    def test_state_changing(self):
        self.assertTrue(self.fsm.isstate('green'))
        self.fsm.warn()
        self.assertTrue(self.fsm.isstate('yellow'))

    def test_state_cannot_be_called_twice(self):
        self.fsm.warn()
        self.assertTrue(self.fsm.isstate('yellow'))
        self.assertRaises(FysomError, self.fsm.warn)

    def test_auto_next_state(self):
        self.assertEqual('green', self.fsm.current)

        self.assertEqual('yellow', self.fsm.next())
        self.assertEqual('yellow', self.fsm.current)
