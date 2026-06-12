import cv2
import numpy as np


class BoardDetector:

    def detect_board(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blurred, 50, 150)

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        largest_quad = None
        largest_area = 0

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area < 50000:
                continue

            peri = cv2.arcLength(cnt, True)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if len(approx) == 4 and area > largest_area:
                largest_quad = approx
                largest_area = area

        if largest_quad is None:
            raise RuntimeError("Chessboard not found")

        return largest_quad.reshape(4, 2)