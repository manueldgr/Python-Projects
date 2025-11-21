# Sistema Multi-Agente para Investigación FEM (Finite Element Method)

## Introducción

Este proyecto simula un sistema multi-agente para la investigación y aplicación del Método de Elementos Finitos (FEM). Cada componente del sistema representa un "agente" especializado que contribuye a diferentes aspectos de la investigación:

- **Agente de Desarrollo**: Implementa el código para resolver problemas FEM
- **Agente de Marco Teórico**: Proporciona la fundamentación teórica
- **Agente de Discusión**: Analiza y discute los resultados obtenidos
- **Agente de Conclusión**: Sintetiza hallazgos y propone trabajos futuros

## Estructura del Proyecto

```
fem_research_agent/
├── src/
│   └── fem_solver_1d.py      # Implementación del solver FEM 1D
├── docs/
│   ├── marco_teorico.md      # Fundamentación teórica
│   ├── discusion_resultados.md  # Análisis de resultados
│   └── conclusion.md         # Conclusiones y trabajo futuro
└── README.md                 # Este archivo
```

## Módulos del Sistema

### 1. Módulo de Teoría (`docs/marco_teorico.md`)
Contiene la fundamentación matemática y física del Método de Elementos Finitos aplicado a barras elásticas unidimensionales.

### 2. Módulo de Código (`src/fem_solver_1d.py`)
Implementación completa de un solver FEM para analizar el desplazamiento de una barra elástica 1D bajo carga axial.

### 3. Módulo de Discusión (`docs/discusion_resultados.md`)
Análisis detallado de los resultados obtenidos y comparación con soluciones analíticas exactas.

### 4. Módulo de Conclusión (`docs/conclusion.md`)
Resumen de los logros del proyecto y propuestas para extensiones futuras.

## Instrucciones de Uso

### Requisitos Previos
- Python 3.6 o superior
- NumPy
- Matplotlib

### Instalación de Dependencias
```bash
pip install numpy matplotlib
```

### Ejecutar el Solver FEM
```bash
python src/fem_solver_1d.py
```

Este comando ejecutará el análisis FEM de una barra elástica 1D y generará:
1. Salida en consola con los nodos y desplazamientos calculados
2. Un gráfico comparando la solución FEM con la solución exacta (`fem_result_plot.png`)

## Descripción del Problema

El solver resuelve el problema de una barra elástica 1D de longitud L, área de sección transversal A, módulo de Young E, sometida a una carga axial F en su extremo libre, mientras el otro extremo está empotrado (desplazamiento nulo).

### Parámetros por Defecto
- Longitud (L): 1.0 m
- Área de sección transversal (A): 0.01 m²
- Módulo de Young (E): 210 GPa (acero)
- Carga en el extremo (F): 10,000 N
- Número de elementos: 10

## Resultados Esperados

El programa calculará los desplazamientos en cada nodo de la discretización y los comparará con la solución analítica exacta, mostrando la precisión del método FEM para este tipo de problemas lineales.

## Autor

Sistema Multi-Agente de Investigación FEM

## Licencia

Este proyecto es parte del repositorio Python-Projects y está disponible para fines educativos y de investigación.
