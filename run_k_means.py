from image_utils import*
from k_means import*
if __name__ == "__main__":
    file = input("image file> ")
    image = read_ppm(file)
    k = int(input("Cluster> "))
    new_file = input("New file's name with its extension> ")
    save_ppm("unchanged.ppm", image)

    means, assigns = k_means(image, k)
    print(means)
    width, height = get_width_height(image)
    for x in range(width):
        for y in range(height):
            for i in range(k):
                if assigns[x][y] == i:
                    image[x][y] = means[i]
    save_ppm(new_file, image)

