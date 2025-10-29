# Boundary-Dominant Optimization: A Closed-Form Framework for Efficient Resource Allocation

This repository contains the Python source code, experimental simulations, and numerical verifications used in the paper titled **“Boundary-Dominant Optimization in Discrete Probabilistic Allocation Models”**.

The article mathematically and experimentally demonstrates why **internal optima remain saddle point in nature** and why **true optimal behavior emerges at the boundary conditions** in discrete probability models (e.g., ball-drawing problems from two bags).

---

## 📄 Article Information

**Article Title:** Boundary-Dominant Optimization: A Closed-Form Framework for Efficient Resource Allocation  
**Author:** Kaan Gökalp  
**Status:** Preprint (submitted to *Entropy*, 2025)
**Field:** Applied Probability, Optimization Theory, Mathematical Modeling  

---

## 📁 Repository Structure
```bash
├── model1/
│ ├── model1_boundary_curves.py # Model 1 - Boundary curves for x = b and x = b + 5. The plot shows the variation of probability P along both limits.
│ ├── model1_results.png # Output
│
├── model2/
│ ├── model2_histogram.py # Model 2 - Distribution of all (b, x) configurations for example parameters m = 6, n = 4.
│ ├── model2_results.png # Output
│
├── model3/
│ ├── model3_figures.py # Model 3 - Distribution of P across all feasible configurations for m = 15, T = 30, k = 3, Standard deviation of the ratios {bi/xi}, Interior vs boundary configuration.
│ ├── model3_histogram.png # Output
│ ├── model3_stddev.png # Output
│ ├── model3_configuration.png # Output
│ ├── model3_heatmap.py # Model 3 -  Parametric heatmap of maximal P over k ∈ {2, 3, 4} and m/T ∈ [0.1, 0.8] (with T = 30).
│ ├── model3_heatmap.png # Output
│ ├── model3_water-filling.py # Visualization of the water-filling algorithm
│ ├── model3_water-filling.png # Output
│
├── supplementary/
│ ├── supplementary_s5_numerical_validation.py # S.5 Numerical Validation - Heatmap of success function P
│ ├── supplementary_s5_numerical_validation.png # Output
│ ├── supplementary_s7.7&s8.4.py # S.7.7 Heatmap of discrete feasible configurations for k=3, m=9, T=30 and S.8.4 Comparison between continuous and discrete optima
│ ├── supplementary_s7.7_heatmap.png # Output
│ ├── supplementary_s8.4_table.csv # Output
├── Boundary_Dominant_Optimization_Kaan_Gokalp.pdf # Main article
├── Supplementary_Material.pdf # Additional proofs and derivations
└── requirements.txt # Python dependencies
```
## ⚙️ Running Instructions
Clone the repository:
```bash
git clone https://github.com/Kaan-Gokalp/BagProbability-Optimization-Models.git
cd BagProbability-Optimization-Models
  ```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Run a sample experiment:
```bash
python model2/model2_histogram.py
```
All graphs and outputs will be automatically saved to the /results/ folder.

## 🧪 Experimental Outputs
The code reproduces all figures presented in the paper:  
**Model 1**: Probability change along the boundary (monotonic analysis)  
**Model 2**: Limit histograms in asymmetric cases  
**Model 3**: Realization of the global optimum under AM–GM conditions (heatmap)  
**Supplementary Material**: Hessian signature analysis, gap bound verifications  

## 📘 Citation
If you use this work, please cite it as follows:  
```
Gökalp, K. (2025). *Boundary-Dominant Optimization: A Closed-Form Framework for Efficient Resource Allocation* [Software]. Zenodo. https://doi.org/10.5281/zenodo.17474108
```
## 📜 License
MIT License © 2025 Kaan Gökalp  

## 📧 Contact
For questions, comments, or contributions:  
📩 kaangokalp6@gmail.com
