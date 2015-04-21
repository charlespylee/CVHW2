import cv2
import numpy as np
import re


def findInterestPoints(filename):
	keynames = re.split(r'\.', filename)
	
	img = cv2.imread(filename)
	gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	sift = cv2.SIFT()
	kp, des = sift.detectAndCompute(gray, None)
	
	img = cv2.drawKeypoints(gray,kp)
	cv2.imwrite(keynames[0] + "_keypts.jpg", img)

	return kp, des

def findMatches(filename1, filename2):

	kp1, des1 = findInterestPoints(filename1)	
	kp2, des2 = findInterestPoints(filename2)

	kp_matches1 = []
	kp_matches2 = []
	des_matches = []

	for i in range(0, des1.shape[0]):
		for j in range(0, des2.shape[0]): 
			d = sum(abs(des1[i] - des2[j]))/128
			if (d < 5):
				kp_matches1.append(kp1[i].pt)
				kp_matches2.append(kp2[j].pt)
#				des_matches.append([des1[i], des2[j]])

	return kp_matches1, kp_matches2, des_matches

def showMatches(matches1, matches2, image1, image2):

	rows1 = image1.shape[0]        
	rows2 = image2.shape[0]
	print rows1
	print rows2 
	if rows1 < rows2:
		image1 = np.concatenate((image1, np.zeros((rows2 - rows1, image1.shape[1]))), axis = 0)
	else:
		image2 = np.concatenate((image2, np.zeros((rows1 - rows2, image2.shape[1]))), axis = 0)
	        
	return np.concatenate((image1, image2), axis = 1)	

#def affineMatches:
#
#def alignImages:
#
#def affineMatches_homography:
#
#def alignImages_homography:

if __name__ == "__main__":

	img1 = cv2.imread('StopSign1.jpg')
	img2 = cv2.imread('StopSign2.jpg')

	kps1, kps2, des_matches = findMatches('StopSign1.jpg', 'StopSign2.jpg')
	result_img12 = showMatches(kps1, kps2, img1, img2)
	cv2.imwrite('result12.png', result_img12)

#	for kp in kps12:
#		img[kp[0]][kp[1]] = [0 ,255, 0]

	img[kps12] = [0 ,255, 0] 	
	cv2.imwrite('img12.png', img)
	
