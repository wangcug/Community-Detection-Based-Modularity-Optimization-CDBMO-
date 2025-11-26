import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import colorsys
import random
#加载图谱数据
file_path=r"Au20240417.gexf"
G=nx.read_gexf(file_path)
#解析度与聚类数与模块度的测试
i=0.5
resolutions=[]
counts=[]
modularities=[]
while i<20:
    communities=nx.community.louvain_communities(G, weight='None', resolution=i, threshold=1e-07)
    count=len(communities)
    modularity=nx.community.modularity(G,communities)
    resolutions.append(i)
    counts.append(count)
    modularities.append(modularity)
    i=i+0.5
result=[resolutions,counts,modularities]
result= list(map(list, zip(*result)))
df=pd.DataFrame(columns=['resolutions', 'counts', 'modularities'],data=result)
df.counts.plot(
    x="resolutions",
)
df.modularities.plot(
    x="resolutions",
    secondary_y=True,
    style='g'
)
plt.show()
#知识图谱网络分析
communities=nx.community.louvain_communities(G, weight='None', resolution=1, threshold=1e-07)
#计算结果模块度指标
modularity=nx.community.modularity(G,communities)
#输出网络分析中的社区数
len(communities)
#输出初始图数据
for node, data in G.nodes(data=True):
    print(f"Node {node}: {data}")
#将网络分析结果添加到节点属性中
for i in range(len(communities)):
    for n in range(len(list(communities[i]))):
        m=list(communities[i])[n]
        G.nodes[m]['Louvain_communityID']=i
#输出图数据结果
for node, data in G.nodes(data=True):
    print(f"Node {node}: {data}")
#输出图文件
nx.write_gexf(G,"test.gexf")


#可视化知识图谱



#定义网络分析结果中的社区数颜色
def get_n_hls_colors(num):
    hls_colors = []
    i = 0
    step = 360.0 / num
    while i < 360:
        h = i
        s = 90 + random.random() * 10
        l = 50 + random.random() * 10
        _hlsc = [h / 360.0, l / 100.0, s / 100.0]
        hls_colors.append(_hlsc)
        i += step

    return hls_colors

#
def ncolors(num):
    rgb_colors = []
    if num < 1:
        return rgb_colors
    hls_colors = get_n_hls_colors(num)
    for hlsc in hls_colors:
        _r, _g, _b = colorsys.hls_to_rgb(hlsc[0], hlsc[1], hlsc[2])
        r, g, b = [int(x * 255.0) for x in (_r, _g, _b)]
        rgb_colors.append([r, g, b])

    return rgb_colors


def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)
#生成颜色
colors=list(map(lambda x: color(tuple(x)), ncolors(len(communities))))
#将不同社区节点赋值颜色
node_colors = []
for node in G:
    current_community_index = 0
    for community in communities:
        if node in community:
            node_colors.append(colors[current_community_index])
            break
        current_community_index += 1
#将节点以spring的布局形式进行可视化
pos = nx.spring_layout(G, k=0.3, iterations=50, seed=2)
nx.draw(
    G,
    pos=pos,
    node_size=100,
    node_color=node_colors,
    with_labels=True,
    font_size=2,
    font_color="black",
    )