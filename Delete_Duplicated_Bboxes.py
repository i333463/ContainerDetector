import numpy as np

# Delete by position of Top Left Coordinate
def Delete_Duplicated_Bboxes(bboxes):

    # return an empty list if there are no boxes
    if len(bboxes) == 0:
        return []

    # initialize the list of remaining Bounding Boxes
    rbboxes = []

    # Ascending sort by y1 & x1
    indexes = np.lexsort((bboxes[:, 0], bboxes[:, 1]))

    while len(indexes) > 0:

        # Indexes of Bounding boxes to be deleted
        overlap_boxes = []

        # delete w/h >= 2.5
        if bboxes[indexes[0], 2] / bboxes[indexes[0], 3] >= 2.5:
            overlap_boxes.append(0)
            indexes = np.delete(indexes, overlap_boxes)
            continue

        # Top Left Coordinate (x1, y1) & Bottom Right Coordinate (x2, y2)
        top_left_x = bboxes[indexes[0], 0]
        top_left_y = bboxes[indexes[0], 1]
        bottom_right_x = bboxes[indexes[0], 0] + bboxes[indexes[0], 2]
        bottom_right_y = bboxes[indexes[0], 1] + bboxes[indexes[0], 3]

        # Initialize Size
        max_size = 0

        # find all overlap boxes and keep the Max one
        for i in range(0, len(indexes)):

            x1 = bboxes[indexes[i], 0]
            x2 = bboxes[indexes[i], 0] + bboxes[indexes[i], 2]
            y1 = bboxes[indexes[i], 1]

            # check overlap with (x1,y1) and (x2,y1)
            if ((top_left_x <= x1 < bottom_right_x) and (top_left_y <= y1 < bottom_right_y))\
               or ((top_left_x < x2 <= bottom_right_x) and (top_left_y < y1 <= bottom_right_y)):

                size = bboxes[indexes[i], 2] * bboxes[indexes[i], 3]

                if size > max_size:
                    max_size = size
                    box = np.array(bboxes[indexes[i], :])

                overlap_boxes.append(i)

        # delete other overlap boxes from loop
        indexes = np.delete(indexes, overlap_boxes)

        rbboxes.append(box)

    # return only the bounding boxes that were picked
    return rbboxes
