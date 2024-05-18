import numpy as np
from PIL import Image
import time
import math
import warnings
warnings.filterwarnings("ignore")

def divide_image(image: np.ndarray) -> list[np.ndarray]:
    mx, my = image.shape[0] // 2, image.shape[1] // 2
    return [image[:mx, :my],
            image[:mx, my:],
            image[mx:, :my],
            image[mx:, my:]]

def construct_image(divided: list[np.ndarray]) -> np.ndarray:
    return np.vstack([np.hstack(divided[:2]),
                      np.hstack(divided[2:])])


def avg_color(image: np.ndarray):
    return np.mean(image, axis=(0, 1)).astype(np.uint8)

def loss_image(image: np.ndarray, avg):
    return (np.abs(image.astype(np.int16) - avg).astype(np.uint8))

def max_color(image: np.ndarray):
    return np.max(image, axis=(0, 1)).astype(np.uint8)

def perc_color(image: np.ndarray, perc: float):
    return np.mean(np.percentile(image, perc, axis=(0, 1))).astype(np.uint8)


def QuadTree(image: np.ndarray, threshold: int):
    if min(image.shape) < 2:
        return image
    avg = avg_color(image)
    if np.mean(avg_color(loss_image(image, avg))) < threshold:
        return np.full_like(image, avg)
    return construct_image([QuadTree(divided, threshold) for divided in divide_image(image)])

def QuadTree_max(image: np.ndarray, threshold: float):
    if min(image.shape) < 2:
        return image
    avg = avg_color(image)
    if np.mean(max_color(loss_image(image, avg))) < threshold:
        return np.full_like(image, avg)
    return construct_image([QuadTree_max(divided, threshold) for divided in divide_image(image)])

def QuadTree_perc(image: np.ndarray, threshold: float, perc: float):
    if min(image.shape) < 2:
        return image
    avg = avg_color(image)
    if np.mean(perc_color(loss_image(image, avg), perc)) < threshold:
        return np.full_like(image, avg)
    return construct_image([QuadTree_perc(divided, threshold, perc) for divided in divide_image(image)])


def main():
    
    image_path = input("Image path: ")
    try:
        try:
            image = np.array(Image.open(image_path))
        except FileNotFoundError:
            try:
                image = np.array(Image.open(image_path + ".png"))
            except FileNotFoundError:
                image = np.array(Image.open(image_path + ".jpg"))
    except FileNotFoundError:
        print("File not found.")
        return
    
    
    threshold = float(input("Threshold: "))
    
    method = input("Method (mean, max, perc): ")
    
    if method == "mean" or method not in ["mean", "max", "perc"]:
        start = time.time()
        Image.fromarray(QuadTree(image, threshold).astype(np.uint8)).save(image_path.split(".")[0] + "_" + str(threshold) + ".png")
        print(f"Saved as {image_path.split('.')[0]}_{threshold}.png in {time.time() - start:.2f} seconds.")

    elif method == "max":
        start = time.time()
        Image.fromarray(QuadTree_max(image, threshold).astype(np.uint8)).save(image_path.split(".")[0] + "_" + str(threshold) + ".png")
        print(f"Saved as {image_path.split('.')[0]}_{threshold}.png in {time.time() - start:.2f} seconds.")

    elif method == "perc":
        perc = float(input("Percentile: "))
        start = time.time()
        Image.fromarray(QuadTree_perc(image, threshold, perc).astype(np.uint8)).save(image_path.split(".")[0] + "_" + str(threshold) + "_" + str(perc) + ".png")
        print(f"Saved as {image_path.split('.')[0]}_{threshold}_{perc}.png in {time.time() - start:.2f} seconds.")


if __name__ == "__main__":
    main()