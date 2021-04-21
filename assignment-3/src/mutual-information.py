import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import skimage
from skimage import io


### entropy calculation
def calculateEntropy(X):
    uniq = set(X)
    P = [np.mean(X == x) for x in uniq]
    return sum(p * np.log2(p) for p in P)


### main calculation step of mutual information
def mutualInfoCalc(img, num_bins):
    top, bottoms = reshapeImage(img)
    mis = []
    for i in range(len(bottoms)):
        hist = np.histogram2d(np.asarray(top).flatten(), np.asarray(bottoms[i]).flatten(), bins=num_bins)
        hist_img = Image.fromarray(hist[0], 'RGB')
        top_hist = np.histogram(np.asarray(top).flatten(), bins=num_bins)
        bot_hist = np.histogram(np.asarray(bottoms[i]).flatten(), bins=num_bins)
        mis.append(calculateEntropy(top_hist[0]) + calculateEntropy(bot_hist[0]) - calculateEntropy(np.asarray(hist_img).flatten()))
    return mis


### split the image into RGB channels, and crop red and green channels
### of the original image according to the assignment's description
def reshapeImage(img):
    red = img[:,:,0]
    green = img[:,:,1]
    width, height = img.shape[0], img.shape[1]
    top = red[20:width-20, 0:height]
    bottoms = [green[40-x:width-x, 0:height] for x in range(40, -1, -1) ]
    return top, bottoms
    # return top, [green.crop((40-x, 0, width-x, height)) for x in range(40, -1, -1)]



### initialize various bin sizes
def binSizeChangeAlt(img):
    top, bottoms = reshapeImage(img)
    mis = {}
    binses = set([int(256/x) for x in range(1,256)])
    for binss in binses:
        hist = np.histogram2d(np.asarray(top).flatten(), np.asarray(bottoms[20]).flatten(), bins=binss)
        hist_img = Image.fromarray(hist[0], 'RGB')
        top_hist = np.histogram(np.asarray(top).flatten(), bins=binss)
        bot_hist = np.histogram(np.asarray(bottoms[20]).flatten(), bins=binss)
        mi = calculateEntropy(top_hist[0]) + calculateEntropy(bot_hist[0]) - calculateEntropy(np.asarray(hist_img).flatten())
        mis[binss] = mi
    return mis


### calculate mutual information and save plot results
def mutuallInformation(img, img_name, bin_size):
    fig = plt.figure()
    plt.ylabel('Mutual Information')
    plt.xlabel('Image Translations')
    sns.lineplot(x=[x for x in range(41)], y=mutualInfoCalc(img, bin_size))
    translations_outputImgPath = "../output/" + img_name + "_binSize_" + str(bin_size) 
    plt.savefig(translations_outputImgPath)

    fig = plt.figure()
    plt.ylabel('Mutual Information')
    plt.xlabel('Number of Bins')
    mis = binSizeChangeAlt(img)
    x, y = zip(*(sorted(mis.items())))
    sns.lineplot(x=x, y=y)
    binSize_outputImgPath = "../output/" + img_name + "binNumCurve"
    plt.savefig(binSize_outputImgPath)


# add noise to the original image
def addNoise(img, mode):
    gimg = skimage.util.random_noise(img, mode=mode)
    return gimg
    

def main():
    penguin_path = "../input/penguins.jpg"
    penguin_img = skimage.io.imread(penguin_path)/255.0
    penguin_name = penguin_path[len("../input/"): -len(".jpg")]

    noisy_penguin_img = addNoise(penguin_img, "salt");
    noisy_penguin_img = addNoise(noisy_penguin_img, "gaussian");

    mutuallInformation(noisy_penguin_img, penguin_name, 15)
    mutuallInformation(noisy_penguin_img, penguin_name, 50)
    mutuallInformation(noisy_penguin_img, penguin_name, 256)

    nature_path = "../input/nature2.jpg"
    nature_img = skimage.io.imread(nature_path)/255.0
    nature_name = nature_path[len("../input/"): -len(".jpg")]

    # noisy_nature_img = addNoise(nature_img, "salt");
    # noisy_nature_img = addNoise(noisy_nature_img, "gaussian");

    mutuallInformation(nature_img, nature_name, 15)
    mutuallInformation(nature_img, nature_name, 50)
    mutuallInformation(nature_img, nature_name, 256)

    flower_path = "../input/flower.jpg"
    flower_img = skimage.io.imread(flower_path)/255.0
    flower_name = flower_path[len("../input/"): -len(".jpg")]

    # noisy_flower_img = addNoise(flower_img, "salt");
    # noisy_flower_img = addNoise(noisy_flower_img, "gaussian");

    mutuallInformation(flower_img, flower_name, 15)
    mutuallInformation(flower_img, flower_name, 50)
    mutuallInformation(flower_img, flower_name, 256)

if __name__ == '__main__':
    main()