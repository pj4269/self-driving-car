import os
pics = os.listdir("test_images/")
print (pics)

#1. Color selection
red_threshold = 100
green_threshold = 200
blue_threshold = 1
rgb_threshold = [red_threshold, green_threshold, blue_threshold]
kernel_size = 3
rho = 1 # distance
theta = np.pi/180 # angle
threshold = 1
min_line_len = 1
max_line_gap = 1


for i, pic in enumerate(pics):
    #print (i)
    image_i = mpimg.imread('test_images/'+pic)
    plt.figure()
    plt.imshow(image_i) 
    # step 1. Turning image to gray
    gray = grayscale(image_i)
    plt.figure()
    plt.imshow(gray) 
    # step 2: Gray to blurred gray 

    blur_gray = gaussian_blur(gray, kernel_size)
    plt.figure()
    plt.imshow(blur_gray) 
    # step 3
    low_threshold = 400
    high_threshold = 500
    masked_edges = canny(blur_gray, low_threshold, high_threshold)
    plt.figure()
    plt.imshow(masked_edges) 
    # Step 4
    #line_image = np.copy(image)*0 #creating a blank to draw lines on
    lines =  hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)
    plt.figure()
    plt.imshow(lines) 
    # Step 5
    #image_i = np.dstack((masked_edges, masked_edges, masked_edges)) 
    combo = weighted_img(lines, image_i, α=0.8, β=1., γ=0.)
    plt.figure()
    plt.imshow(combo) 
    '''
    #1. Color selection
    thresholds = (image_i[:,:,0] < rgb_threshold[0]) | (image_i[:,:,1] < rgb_threshold[1]) | (image_i[:,:,2] < rgb_threshold[2])
    # pixels above the threshold [0,0,0] have been selected 
    color_select_i = np.copy(image_i)
    color_select_i[thresholds] = [0,0,0]
    # Display the image          
    plt.figure()
    plt.imshow(color_select_i)
    plt.show()
    '''
