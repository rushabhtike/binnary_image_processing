import numpy as np
import matplotlib.pyplot as plt


class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0] * 256
        x, y = image.shape[:2]
        #print(image.shape)
        for i in range(x):
            for j in range(y):
                hist[image[i, j]] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        k = 256
        threshold = int(k / 2)
        lastexpected1 = lastexpected2 = 0

        while True:
            expected1 = expected2 = 0
            t_exp1 = sum(hist[:threshold])
            t_exp2 = sum(hist[threshold:])
            for i in range(threshold):
                expected1 += (hist[i] / t_exp1) * i

            for i in range(threshold, k):
                expected2 += (hist[i] / t_exp2) * i

            threshold = (expected1 + expected2) / 2
            if abs(expected1 - lastexpected1) != 0 and abs(expected2 - lastexpected2) != 0:
                break
            lastexpected1 = expected1
            lastexpected2 = expected2
            # print(expected2, expected1)
        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        bin_img = image.copy()
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i, j] >= threshold:
                    bin_img[i, j] = 0
                else:
                    bin_img[i, j] = 255
        return bin_img
