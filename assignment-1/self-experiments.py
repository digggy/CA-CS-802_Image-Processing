from PIL import Image 
import numpy as np
import csv
from numpy import genfromtxt
from matplotlib import pyplot as plt

def read_SE_Values(filename):
    SE_txt = []
    with open(filename,'r') as f1_csv:
        csv_reader = csv.reader(f1_csv)
        for line in csv_reader:
            SE_txt.append(list(map(int, line)))
    
    SE = np.array(SE_txt)
    return SE

def self_experiment_1():

    img_name = "cells2"
    img= Image.open(img_name + ".png").convert('L')
    image_np = np.array(img) 
    
    np.savetxt(img_name + '.txt', image_np,
               delimiter=', ', newline='\n', fmt='%d')

    SE = np.ones((5,3), int)
    
    padding_y , padding_x = SE.shape[0]//2, SE.shape[1]//2 

    image_np_with_boundary_erosion = np.pad(image_np, ((padding_y, padding_y),(padding_x, padding_x)), mode='constant', constant_values=255)
    
    image_np_with_boundary_dilation = np.pad(image_np, ((padding_y, padding_y),(padding_x, padding_x)), mode='constant', constant_values=0)
   
    img_erosion = np.zeros((image_np.shape[0], image_np.shape[1]), int)
    img_dilation = np.zeros((image_np.shape[0], image_np.shape[1]), int)
    square_five_ones_SE = np.ones((4,4), int)


    for i in range(image_np_with_boundary_erosion.shape[0]-SE.shape[0]):
        for j in range(image_np_with_boundary_erosion.shape[1]-SE.shape[1]):
            img_subarr = image_np_with_boundary_erosion[i:i+SE.shape[0], j:j+SE.shape[1]]
            
            img_erosion[i,j] = np.min(img_subarr)

    

    for i in range(image_np_with_boundary_dilation.shape[0]-SE.shape[0]):
        for j in range(image_np_with_boundary_dilation.shape[1]-SE.shape[1]):
            img_subarr = image_np_with_boundary_dilation[i:i+SE.shape[0], j:j+SE.shape[1]]
            
            img_dilation[i,j] = np.max(img_subarr)

    np.savetxt(img_name + '_erosion.txt', img_erosion,
               delimiter=', ', newline='\n', fmt='%d')
    np.savetxt(img_name + '_dilation.txt', img_dilation,
               delimiter=', ', newline='\n', fmt='%d')

    plt.imshow(image_np, cmap='gray')
    plt.savefig(img_name + '_gray.png')

    plt.imshow(img_erosion, cmap='gray')
    plt.savefig(img_name + '_erosion.png')

    plt.imshow(img_dilation, cmap='gray')
    plt.savefig(img_name + '_dilation.png')
    
        
    turn_off_axes = True
    plt.subplot(1, 4, 1)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)
    plt.imshow(SE, cmap='gray')
    plt.title('SE')
    # plt.axis('off') if turn_off_axes else None

    # plot main images
    plt.subplot(1, 4, 2)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(img, cmap='gray')
    plt.title('image')
    plt.axis('off') if turn_off_axes else None

    # Plot the bordered image
    plt.subplot(1, 4, 3)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(image_np_with_boundary_dilation, cmap='gray')
    plt.title('img_with_boundary')
    plt.axis('off') if turn_off_axes else None

    # Plot the exepected output
    plt.subplot(1, 4, 4)
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(img_dilation, cmap='gray')
    plt.title('Image after operation')
    plt.axis('off') if turn_off_axes else None
    # plt.show()
    plt.savefig(img_name + "_four_grids.png", bbox_inches='tight')



if __name__ == "__main__":
    self_experiment_1()