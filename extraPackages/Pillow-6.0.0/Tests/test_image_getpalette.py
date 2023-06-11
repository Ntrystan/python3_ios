from .helper import PillowTestCase, hopper


class TestImageGetPalette(PillowTestCase):

    def test_palette(self):
        def palette(mode):
            p = hopper(mode).getpalette()
            return p[:10] if p else None

        self.assertIsNone(palette("1"))
        self.assertIsNone(palette("L"))
        self.assertIsNone(palette("I"))
        self.assertIsNone(palette("F"))
        self.assertEqual(palette("P"), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertIsNone(palette("RGB"))
        self.assertIsNone(palette("RGBA"))
        self.assertIsNone(palette("CMYK"))
        self.assertIsNone(palette("YCbCr"))
