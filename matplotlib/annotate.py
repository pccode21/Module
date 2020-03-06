import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import matplotlib.path as mpath
import matplotlib.image as mpimg

os.chdir(r'.\Module\matplotlib')  # 创建工作路径

font = {'family': 'Microsoft Yahei', 'size': '8'}  # 设置才可以正常现在中文
matplotlib.rc('font', **font)

x = np.linspace(-3, 3, 50)  # 使用np.linspace定义x：范围是(-3,3);个数是50.
y1 = 2 * x + 1
y2 = x ** 2
left, bottom, width, height = 0.1, 0.2, 0.8, 0.6
"""
确定大图左下角的位置以及宽高
注意，4个值都是占整个figure坐标系的百分比。
在这里，假设figure的大小是10x10，那么大图就被包含在由(1, 1)开始，宽8，高8的坐标系内。
"""
plt.figure(num=1, figsize=(8, 6)).add_axes([left, bottom, width, height])  # 使用plt.figure定义一个图像窗口：编号为1；大小为(8, 5)
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# set new sticks
# new_sticks = np.linspace(-1, 2, 5)
# plt.xticks(new_sticks)
plt.xticks([-1, -0.5, 0, 0.5, 1, 1.5, 2],)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$Negative\ two$', r'$Negative\ one\ point\ eight$', r'$Negative\ one$', r'$one\ point\ two\ two$', r'$three$'])
# set line styles
l1, = plt.plot(x, y1, label='linear line', linestyle='--')
# 用变量 l1存储起来. 而且需要注意的是 l1,要以逗号结尾, 因为plt.plot() 返回的是一个列表
l2, = plt.plot(x, y2, color='red', linewidth=1.0, label='square line')
# 用变量 l2存储起来. 而且需要注意的是 l2,要以逗号结尾, 因为plt.plot() 返回的是一个列表
plt.legend(handles=[l1, l2], labels=['straight line', 'Arc line'], loc='best')
# legend 添加图例
# 其中’loc’参数有多种，’best’表示自动分配最佳位置
ax = plt.gca()  # 使用plt.gca获取当前坐标轴信息
ax.spines['right'].set_color('none')  # 使用.spines设置边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置
ax.spines['bottom'].set_position(('data', 0))  # 使用.set_position设置边框位置：y=0的位置；（位置所有属性：outward，axes，data）
ax.yaxis.set_ticks_position('left')  # 使用.yaxis.set_ticks_position设置y坐标刻度数字或名称的位置
ax.spines['left'].set_position(('data', 0))  # 使用.set_position设置边框位置：x=0的位置
# 标注出点(x0, y0)的位置信息
x0 = 1
y0 = x0 ** 2
plt.plot([x0, x0], [0, y0], 'y--', linewidth=1)  # 画出一条垂直于x轴的虚线， k 是虚线的颜色
# plt.plot([x0, 0], [y0, y0], 'y--', linewidth=2.5)  # 画出一条垂直于y轴的虚线， k 是虚线的颜色
# set dot styles
star = mpath.Path.unit_regular_star(5)
circle = mpath.Path.unit_circle()
verts = np.concatenate([circle.vertices, star.vertices[::-1, ...]])
codes = np.concatenate([circle.codes, star.codes])
circle_star = mpath.Path(verts, codes)
plt.scatter([x0], [y0], s=100, color='r', marker=circle_star)  # 画一个点
# 添加注释 annotate
plt.annotate(r'$x^2=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
            textcoords='offset points', fontsize=12, color='g',
            arrowprops={'arrowstyle': '->', 'connectionstyle': 'arc3, rad=-0.3'})
            # 也可以写成 arrowprops=dict(arrowstyle='-|>',connectionstyle='arc3, rad=-0.3')
"""
其中参数xycoords='data' 是说基于数据的值来选位置,
xytext=(+30, -30) 和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值,
arrowprops是对图中箭头类型的一些设置
"""
# 添加注释 text
plt.text(-1, 2, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
        fontdict={'size': 9, 'color': 'red'})
# 其中-1, 2,是选取text的开始位置, 空格需要用到转字符\ ,fontdict设置文本字体.
plt.title("函数图", fontsize=14, loc='center')  # 设置标题
# 插入小图，注意坐标系位置和大小的改变
left, bottom, width, height = 0.9, 0.1, 0.1, 0.1
ax2 = plt.figure(num=1).add_axes([left, bottom, width, height])  # 这里的 num 值要跟大图一致
# fig, ax = plt.subplots(1, 1, figsize=(1, 1))
image = mpimg.imread('LOGO.ico')
ax2.imshow(image)
ax2.axis('off')
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap('LOGO.ico')
thismanager.canvas.set_window_title('数能工作室制作')
plt.savefig('annotate.png', dpi=400)  # 保存图表
plt.show()
