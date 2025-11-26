# Community-Detection-Based-Modularity-Optimization-CDBMO-
# Community Detection in a Geological Knowledge Graph Using Modularity Optimization  

## 📘 Overview
This project applies the **Louvain modularity optimization algorithm** to a geological knowledge graph stored in `.gexf` format. It evaluates the influence of the resolution parameter on community detection results, visualizes the graph with community-based coloring, and provides mapping tables between detected communities and mineral deposit types.

The repository includes:

- The algorithm for running community detection  
- Resolution scan results (community count vs. modularity)  
- Visualization of entity–relationship knowledge graph  
- Mapping between communities and deposit types  

---

## 📁 Data Description

### 1. Knowledge Graph Data (`.gexf`)
- **File**: `Au20240417.gexf`  
- **Content**: Geological entities (deposits, lithologies, tectonic events, structures, etc.) and the semantic relations among them (e.g., “occurs in,” “belongs to,” “controlled by”).  
- **Characteristics**:  
  - Covers all entity types in the ontology  
  - Includes all major relationship types  
  - Serves as input for community detection and visualization  

### 2. Graph Figures
- **Entity–relationship schema graph** illustrating the ontology structure  
- **Community detection visualization** with spring layout and color-coded communities  

### 3. Community–Deposit Type Mapping Table  
A detailed correspondence between:
- Louvain community ID  
- Geological deposit type  
- Representative deposit examples  

(Provided separately as an Excel/CSV file.)

---

## 🧠 Method and Algorithm

### Louvain Community Detection  
The analysis uses the implementation in NetworkX:

```
nx.community.louvain_communities(G, resolution=..., weight=None)
```

Key ideas:
1. Locally optimize modularity by moving nodes  
2. Aggregate nodes within each community  
3. Repeat until modularity stabilizes  

The method is efficient for large networks and suited for exploratory knowledge graph analysis.

### Resolution Parameter Scan  
To understand how resolution impacts community detection, the workflow iterates:

```
resolution from 0.5 to 20, step = 0.5
```

For each resolution value, it computes:
- Number of detected communities  
- Overall modularity value  

The results are plotted with dual axes, showing resolution vs. community count and modularity.

---

## 🧩 Code Overview

### Main Analysis Script

```python
# (Code omitted here for brevity; included in full version above)
```

---

## 📊 Key Results

### 1. Resolution Scan
- Higher resolution values generally produce more communities  
- Modularity peaks in specific resolution ranges  
- Helps determine the optimal scale for structural analysis  

### 2. Community Detection at Resolution = 1
- **Modularity**: *value depends on your dataset*  
- **Number of communities**: *varies by dataset*  
- Each community corresponds to a cluster of semantically related geological entities  

### 3. Knowledge Graph Visualization
- Spring layout  
- Coloring reflects Louvain communities  
- Node attributes include a `Louvain_communityID` field, compatible with Gephi/Cytoscape  

---

## 📦 Output Files

| File | Description |
|------|-------------|
| `test.gexf` | Updated graph with community IDs |
| `resolution_modularity_plot.png` | (Optional) Modularity–resolution figure |
| `entity_relation_graph.png` | Knowledge graph example figure |
| `community_mineraltype_mapping.xlsx` | Mapping between communities and deposit types |

---

## 🚀 Usage

1. Place `Au20240417.gexf` in the working directory  
2. Run the Python script  
3. Inspect printed node attributes or import `test.gexf` into **Gephi**  
4. Adjust layout/coloring for high-quality visualization  

---

## 📚 Reference

> Blondel, V.D., Guillaume, J.L., Lambiotte, R., & Lefebvre, R. (2008).  
> **Fast unfolding of communities in large networks.** *Journal of Statistical Mechanics: Theory and Experiment.*

