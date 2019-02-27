import numpy as np


class rle:

    def encode_image(self, binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        # rle_code = []
        # maxvalues = []
        # for i in range(binary_image.shape[0]):
        #     for j in range(binary_image.shape[1]):
        #         maxvalues.append(binary_image[i, j])
        # i = 0
        # while True:
        #     length = 0
        #     while i < len(maxvalues) - 1 and maxvalues[i] == maxvalues[i + 1]:
        #         length = length + 1
        #         i = i + 1
        #     code = (maxvalues[i], length)
        #     rle_code.append(code)
        #     i = i + 1
        #     if i >= len(maxvalues):
        #         break

        rle_code = []
        count = 0
        start_pixel = 0
        for i in range(binary_image.shape[0]):
            for j in range(binary_image.shape[1]):
                if start_pixel == binary_image[i][j]:
                    count += 1
                else:
                    rle_code.append(count)
                    count = 1
                    start_pixel = 255 if start_pixel == 0 else 0

        return rle_code  # replace zeros with rle_code

    def decode_image(self, rle_code, height, width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        image = np.zeros((height * width), np.uint8)
        current_pixel = 0
        current_position = 0
        for i in rle_code:
            image[current_position:current_position + i] = current_pixel
            current_position = current_position + i
            current_pixel = 255 if current_pixel == 0 else 0
        return np.reshape(image, (height, width))  # replace zeros with image reconstructed from rle_Code
