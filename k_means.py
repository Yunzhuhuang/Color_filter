from image_utils import*
from math import sqrt
from math import pow


def k_means(image: list, k: int):

    # get width and height of image
    width, height = get_width_height(image)

    # create a random initial means_list
    means_list = []
    for i in range(k):
        means_list.append(random_color())
    print(means_list)

    # create a assignments_list
    assignments_list = []

    # compute distance
    def distance(color, mean):
        dist = sqrt(pow((color[0]-mean[0]), 2) + pow((color[1]-mean[1]), 2) + pow((color[2]-mean[2]), 2))
        return dist

    #  assigned to clusters
    def assign(images, means, ks):
        assignments = []
        for col in range(width):
            assignments.append([0])
            for row in range(height):
                if row < height - 1:
                    assignments[col].append(0)
                close = 0
                for p in range(1, ks):
                    if distance(images[col][row], means[p]) < distance(images[col][row], means[close]):
                        close = p
                assignments[col][row] = close
        return assignments

    # recomputed means_list
    def re_means(images, means, assignments, ks):
        sums = [[0, 0, 0]] * ks
        num = [0] * ks
        new_means = sums
        for cols in range(width):
            for rows in range(height):
                for j in range(ks):
                    if assignments[cols][rows] == j:
                        num[j] += 1
                        print(j)
                        # sum of everything?
                        for m in range(3):
                            print(m, images[cols][rows][m])
                            sums[j][m] += images[cols][rows][m]
        print(num)
        print(sums)
        for n in range(ks):
            for a in range(3):
                if num[n] != 0:
                    new_means[n][a] = sums[n][a] // num[n]
                else:
                    new_means[n][a] = sums[n][a]
        return new_means

    # start doing k_means
    assignments_list = assign(image, means_list, k)
    # print(assignments_list)
    change = True
    while change:
        means_list = re_means(image, means_list, assignments_list, k)
        print(means_list)
        new_assignments_list = assign(image, means_list, k)
        print(1)
        if new_assignments_list == assignments_list:
            change = False
        else:
            assignments_list = new_assignments_list

    return means_list, assignments_list
