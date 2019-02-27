Name: Rushabh Tike \
PSID: 1800104

Assignment 2 Report

1. Region Counting

    a. Histogram and binary image 
    - Computed the histogram of given image. 
    - Found the optimal threshold from the histogram by using expected values. Threshold is equal to the mean of thr two expected values. 
    - Generated a binary image by using the threshold calculated in the previous step. The pixel intensities can be divided into 2 color groups, black and white by comparing them with the threshold. 
    -  if image[i, j] >= threshold \
       bin_img[i, j] = 0 \
       else \
       bin_img[i, j] = 255 
    - The grayscale image was successfully converted to binary image using thresholding. 
        
    b. Blob coloring, stats and region marking
    
    - Used a dictionary to store the regions(R).
    - Stored as key, value pair.
    - Algorithm used : \
      if I(i, j) = 1 and I(i, j-1) = 0 and I(i-1, j) = 0 then \
      set R(i, j) = k and k = k + 1; \
      if I(i, j) = 1 and I(i, j-1) = 0 and I(i-1, j) = 1 then \
      set R(i, j) = R(i-1, j); \
      if I(i, j) = 1 and I(i, j-1) = 1 and I(i-1, j) = 0 then \
      set R(i, j) = R(i, j-1); \
      if I(i, j) = 1 and I(i, j-1) = 1 and I(i-1, j) = 1 then \
      set R(i, j) = R(i-1, j); \
      if R(i, j-1) != R(i-1, j) then \
      set R(i, j-1) and R(i-1, j) as same color.
    - Found the x center and y center of the regions by dividing the sum of arrays by their length. 
    - Used the function cv2.putText to mark the regions.
    - Created a label with key , area to mark the regions on a new image.
    - Regions with area and center were successfully marked.
             
2. Image Compression 

    a. Encoding 
     - Created an empty array.
     - Set the start pixel as 0.
     - If the start pixel is equal to current pixel image increase the count else set the strat pixel as 255 and repeat.
     - Image was successfully encoded. 
           
    b. Decoding 
     - Created a zeros array using the given height and width.
     - Set the current pixel as the starting pixel.
     - Toggled between 255 and 0 when the count changed.
     - Used np.reshape to create the decoded image.
     - Image was successfully decoded.
        