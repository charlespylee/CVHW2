import cv2
import numpy as np
import sys
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
		best_match = sys.maxint 
		bm_index = -1	
		second_match = sys.maxint
		sm_index = -1
		for j in range(0, des2.shape[0]):
			d = sum((des1[i] - des2[j])**2)
			if (d < best_match):
				second_match = best_match
				sm_index = bm_index
				best_match = d
				bm_index = j 
			elif (d < second_match):
				second_match = d
				sm_index = j
		if (best_match / second_match) < 0.8:
			kp_matches1.append(kp1[i].pt)
			kp_matches2.append(kp2[bm_index].pt)
	return kp_matches1, kp_matches2, des_matches

def showMatches(matches1, matches2, image1, image2):
<<<<<<< HEAD
	
=======
	# print "matches1"
	# print matches1
	# print matches2
>>>>>>> 1203664a8deec9633bfc1c53352872e5d52383dc
	rows1 = image1.shape[0]        
	rows2 = image2.shape[0]
	col1 = image1.shape[1]
	# print rows1
	# print rows2 
	if rows1 < rows2:
		image1 = np.concatenate((image1, np.zeros((rows2 - rows1, image1.shape[1],3))), axis = 0)
	else:
		image2 = np.concatenate((image2, np.zeros((rows1 - rows2, image2.shape[1],3))), axis = 0)

	res = np.concatenate((image1, image2), axis = 1)
	print len(matches1),len(matches2)
<<<<<<< HEAD
=======
	for i in range(len(matches1)):
		cv2.line(res,( int(matches1[i][0]),int(matches1[i][1])),(col1+int(matches2[i][0]),int(matches2[i][1])),(0,255,0),1)
	
	return res
>>>>>>> 1203664a8deec9633bfc1c53352872e5d52383dc

	for i in range(len(matches1)):
		cv2.line(res,( int(matches1[i][0]),int(matches1[i][1])),(col1+int(matches2[i][0]),int(matches2[i][1])),(0,255,0),1)
	
	return res

def affineMatches:

	
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

	
