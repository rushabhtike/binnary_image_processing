import cv2
import numpy as np


class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        regions = dict()
        final_regions = dict()
        region_count = 1
        region = np.zeros((image.shape[0], image.shape[1]))
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] == 255:
                    if i == 0 and j == 0:
                        region[i][j] = region_count
                        regions[region_count] = [(i, j)]
                        region_count += 1
                    elif i == 0:
                        if image[i][j - 1] == 255:
                            region[i][j] = region[i][j - 1]
                            regions[region[i][j]].append((i, j))
                        else:
                            region[i][j] = region_count
                            regions[region_count] = [(i, j)]
                            region_count += 1
                    elif j == 0:
                        if image[i - 1][j] == 255:
                            region[i][j] = region[i - 1][j]
                            regions[region[i][j]].append((i, j))
                        else:
                            region[i][j] = region_count
                            regions[region_count] = [(i, j)]
                            region_count += 1
                    elif i != 0 and j != 0:
                        if image[i][j - 1] == 0 and image[i - 1][j] == 0:
                            region[i][j] = region_count
                            regions[region_count] = [(i, j)]
                            region_count += 1
                        elif image[i][j - 1] == 0 and image[i - 1][j] == 255:
                            region[i][j] = region[i - 1][j]
                            regions[region[i][j]].append((i, j))
                        elif image[i][j - 1] == 255 and image[i - 1][j] == 0:
                            region[i][j] = region[i][j - 1]
                            regions[region[i][j]].append((i, j))
                        elif image[i][j - 1] == 255 and image[i - 1][j] == 255:
                            region[i][j] = region[i - 1][j]
                            regions[region[i][j]].append((i, j))
                            if region[i][j - 1] != region[i - 1][j]:
                                to_delete = region[i][j - 1]
                                regions[region[i - 1][j]] = regions[region[i - 1][j]] + regions[region[i][j - 1]]
                                for point in regions[region[i][j - 1]]:
                                    region[point[0]][point[1]] = region[i - 1][j]
                                regions.pop(to_delete)

        k = 1
        for key, value in regions.items():
            final_regions[k] = value
            k += 1

        #print(regions)
        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        stats = dict()
        for key, value in region.items():
            array = np.asarray(value)
            length = array.shape[0]
            if length >= 15:
                x_sum = np.sum(array[:, 0])
                y_sum = np.sum(array[:, 1])
                x_center = int(np.round(x_sum / length))
                y_center = int(np.round(y_sum / length))
                print(key, ": (", x_center, ",", y_center, ")", length)
                stats[key] = [(y_center, x_center), length]
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        new_image = image.copy()
        for key, value in stats.items():
            #print("value", value)
            label = '{key}, {area}'.format(key=key, area=value[1])
            cv2.putText(new_image, "*" + label, (value[0]), cv2.FONT_HERSHEY_COMPLEX, 0.25, 1)

        return new_image
