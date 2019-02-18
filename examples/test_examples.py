import unittest
import numpy as np

from dom import DOM


class TEST_DOM(unittest.TestCase):
	def setUp(self):
		self.dom = DOM()

	def test_img_source(self):
		imgPath = "./examples/images/text-img.png"
		score = self.dom.get_sharpness(imgPath)
		# print("img source score:", score)
		self.assertGreater(score, 0)

	def test_three_channel_image(self):
		img = np.random.randint(255,size=(10,10,3), dtype=np.uint8)
		score = self.dom.get_sharpness(img)
		# print("3 channel source score:", score)
		self.assertGreaterEqual(score, 0)

	def test_two_channel_image(self):
		img = np.random.randint(255, size=(10, 10), dtype=np.uint8)
		score = self.dom.get_sharpness(img)
		# print("2 channel source score:", score)
		self.assertGreaterEqual(score, 0)

	def test_value_error(self):
		img = np.random.randint(255, size=(10,), dtype=np.uint8)
		with self.assertRaises(ValueError):
			self.dom.get_sharpness(img)

if __name__ == '__main__':
	unittest.main()