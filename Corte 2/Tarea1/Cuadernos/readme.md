# Redes Neuronales Artificiales: Neurona Biológica y Perceptrón Lineal

Este repositorio contiene las prácticas de laboratorio sobre los fundamentos de redes neuronales artificiales, abarcando desde el modelo biológico hasta la implementación de neuronas lineales en Python.

---

## 🛠️ Estructura del Repositorio

### Bloque 1: Implementación Básica (Python Nativo)
* **`neuron1.ipynb`**: Neurona con regla de actualización directa ($y = wx$).
* **`neuron1.1.ipynb`**: Optimización mediante Error Cuadrático y Descenso por Gradiente ($y = wx$).
* **`neuron1.2.ipynb`**: Modelo lineal completo con peso y sesgo ($y = wx + b$).

### Bloque 2: Implementación Vectorizada (NumPy & Matplotlib)
* **`practica1_numpy.ipynb`**: Modelo $y = wx$ vectorizado y análisis gráfico de convergencia.
* **`practica2_numpy.ipynb`**: Descenso por gradiente vectorizado con curvas de costo.
* **`practica3_numpy.ipynb`**: Modelo $y = wx + b$ vectorizado con visualización del ajuste lineal.

---

## 📐 Fundamentos Matemáticos

* **Modelo del Perceptrón:** $y = wx + b$
* **Error Cuadrático Medio:** $E = (y - t)^2$
* **Derivada respecto al peso:** $\frac{\partial E}{\partial w} = 2(y - t) \cdot x$
* **Derivada respecto al sesgo:** $\frac{\partial E}{\partial b} = 2(y - t)$
* **Actualización por Descenso por Gradiente:** 
  $$w \leftarrow w - \eta \cdot \nabla_w J$$
  $$b \leftarrow b - \eta \cdot \nabla_b J$$

---

## 🚀 Entorno de Ejecución
Todos los cuadernos fueron estructurados como documentos técnicos y desarrollados en la plataforma **Kaggle Notebooks**.
