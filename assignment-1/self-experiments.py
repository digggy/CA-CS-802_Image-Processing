from PIL import Image 
import numpy as np

def read_SE_Values(filename):
    SE_txt = []
    with open(filename,'r') as f1_csv:
        csv_reader = csv.reader(f1_csv)
        for line in csv_reader:
            SE_txt.append(list(map(int, line)))
    
    SE = np.array(SE_txt)
    return SE

def self_experiment_1():

    img= Image.open("cells1.png").convert('L')
    image_np = np.array(img) 
    
    SE_eleven = np.ones((11,11), int)
    
    image_np_with_boundary = np.ones((image_np.shape[0]+2, image_np.shape[1]+2))
    
    for i in range(image_np.shape[0]):
        image_np_with_boundary[i, 0] = 255
        image_np_with_boundary[i, image_np.shape[1]+1] = 255

    image_np_with_boundary[0:image_np.shape[0], 1:image_np.shape[1]+1] = image_np
    img_erosion = np.zeros((image_np.shape[0], image_np.shape[1]), int)
    img_dilation = np.zeros((image_np.shape[0], image_np.shape[1]), int)
    square_five_ones_SE = np.ones((5,5), int)


    for i in range(image_np_with_boundary.shape[0]-SE_eleven.shape[0]):
        for j in range(image_np_with_boundary.shape[1]-SE_eleven.shape[1]):
            img_subarr = image_np_with_boundary[i:i+SE_eleven.shape[0], j:j+SE_eleven.shape[1]]
            
            img_erosion[i,j] = np.min(img_subarr)
            img_dilation[i,j] = np.max(img_subarr)

    np.savetxt('self_experiment_1_erosion.txt', img_erosion,
               delimiter=', ', newline='\n', fmt='%d')
    np.savetxt('self_experiment_1_dilation.txt', img_dilation,
               delimiter=', ', newline='\n', fmt='%d')

if __name__ == "__main__":
    self_experiment_1()