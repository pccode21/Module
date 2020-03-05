from matplotlib import pyplot as plt
from skimage import io, data
import os

os.chdir(r'.\Module\matplotlib')  # 创建工作路径
image = io.imread('LOGO.ico')
fig, ax = plt.subplots(1, 1, figsize=(1, 1))
ax.imshow(image)
ax.axis('off')
plt.show()
