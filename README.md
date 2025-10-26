# Boundary-Dominant Probability Optimization Models

This repository contains the Python source code, experimental simulations, and numerical verifications used in the paper titled **“Boundary-Dominant Optimization in Discrete Probabilistic Allocation Models”**.

The article mathematically and experimentally demonstrates why **internal optima remain saddle point in nature** and why **true optimal behavior emerges at the boundary conditions** in discrete probability models (e.g., ball-drawing problems from two bags).

---

## 📄 Article Information

**Article Title:** Boundary-Dominant Optimization: A Closed-Form Framework for Efficient Resource Allocation
**Author:** Kaan Gökalp 
**Status:** Preprint available on *arXiv (coming soon)*  
**Field:** Applied Probability, Optimization Theory, Mathematical Modeling  

---

## 📁 Repository Structure
├── model1_analysis/
│ ├── model1_boundary_plots.py # Model 1: Sınır davranışı analizleri
│ ├── model1_results.png # Model 1’e ait grafiksel çıktı
│
├── model2_asymmetric/
│ ├── model2_limit_simulation.py # Model 2: Asimetrik durumda limit analizi
│ ├── model2_results.png
│
├── model3_waterfilling/
│ ├── model3_lagrange_solver.py # Model 3: Lagrange çözümü ve heatmap analizi
│ ├── model3_heatmap.png
│
├── appendix/
│ ├── appendix_hessian_example.py # Ek: Hessian sınıflandırma örneği
│ ├── appendix_gap_bound_check.py # Ek: Gap bound hesaplamaları
│
├── Makale.pdf # Ana makale dosyası
├── Supplementary_Material.pdf # Ek materyaller ve ispatlar
└── requirements.txt # Gerekli Python kütüphaneleri
