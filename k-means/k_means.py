# k means
# 输入一串二维序列点 [(x, y)}

import numpy as np


def init_centroids(data, k):
    # 随机选择k个质心
    init_indexes = np.random.choice(range(len(data)), k, replace=False)
    centroids = data[init_indexes]
    return centroids


def assign_cluster(data, centroids):
    """
    获取每个点对应的聚类类别
    :param data:
    :param centroids:
    :return:
    """
    # 计算每个数据点到k个簇心的距离
    data_expand = data[:, np.newaxis]
    distance_matrix = data_expand - centroids
    distances = np.linalg.norm(distance_matrix, axis=2)
    # 返回距离最近的簇心的索引
    cluster_labels = np.argmin(distances, axis=1)
    return cluster_labels


def update_centroids(data, cluster_labels, k):
    """
    根据聚类类别，重新计算每个聚类的质心
    :param data:
    :param cluster_labels:
    :param k:
    :return:
    """
    new_centroids = np.zeros((k, data.shape[1]))
    for i in range(k):
        new_centroids[i] = np.mean(data[cluster_labels == i], axis=0)
    return new_centroids


def check_convergence(centroids, old_centroids, tol=1e-4):
    """
    检查重新计算的质心与上一步质心的距离是否足够接近
    :param centroids:
    :param old_centroids:
    :param tol:
    :return:
    """
    diff = np.linalg.norm(centroids - old_centroids)
    return diff < tol


def k_means(data, k, max_iteration=100):
    centroids = init_centroids(data, k)
    iter = 0
    converged = False
    while not converged and iter < max_iteration:
        # 获取每个点对应的聚类类别
        cluster_labels = assign_cluster(data, centroids)
        old_centroids = centroids
        # 根据聚类类别，重新计算每个聚类的质心
        centroids = update_centroids(data, cluster_labels, k)
        # 检查重新计算的质心与上一步质心的距离是否足够接近
        converged = check_convergence(centroids, old_centroids)
        iter += 1

    return centroids


if __name__ == '__main__':
    data = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [3, 1]])
    centroids = k_means(data, k=3)
    print('centroids:')
    print(centroids)

