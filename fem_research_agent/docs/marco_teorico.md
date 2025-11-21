# Marco Teórico: Método de Elementos Finitos para Barras Elásticas 1D

## Introducción al Método de Elementos Finitos

El Método de Elementos Finitos (FEM, por sus siglas en inglés) es una técnica numérica para encontrar soluciones aproximadas a problemas de valores en la frontera para ecuaciones diferenciales. En el contexto de la mecánica estructural, permite analizar el comportamiento de estructuras complejas dividiéndolas en elementos más simples.

## Teoría Fundamental para Barras Elásticas 1D

### Ley de Hooke

La base de la elasticidad lineal es la **Ley de Hooke**, que relaciona el esfuerzo (σ) con la deformación (ε) a través del módulo de Young (E):

$$\sigma = E \epsilon$$

Donde:
- σ: Esfuerzo normal (Pa o N/m²)
- E: Módulo de Young o módulo elástico (Pa)
- ε: Deformación unitaria (adimensional)

Para una barra unidimensional, la deformación se relaciona con el desplazamiento u(x) mediante:

$$\epsilon = \frac{du}{dx}$$

### Ecuación Diferencial de Gobierno

Para una barra elástica sometida a carga axial, la ecuación de equilibrio es:

$$\frac{d}{dx}\left(EA\frac{du}{dx}\right) = 0$$

Donde:
- E: Módulo de Young
- A: Área de la sección transversal
- u(x): Desplazamiento axial en función de la posición x

En el caso de E y A constantes, esto se simplifica a:

$$EA\frac{d^2u}{dx^2} = 0$$

### Discretización por Elementos Finitos

#### División del Dominio

El dominio continuo [0, L] se divide en elementos discretos. Para n elementos, tenemos (n+1) nodos. Cada elemento conecta dos nodos consecutivos.

#### Funciones de Forma Lineales

Dentro de cada elemento, el desplazamiento se aproxima usando funciones de forma lineales:

$$u(x) = N_1(x)u_1 + N_2(x)u_2$$

Donde u₁ y u₂ son los desplazamientos en los nodos del elemento, y N₁(x) y N₂(x) son las funciones de forma lineales (también llamadas funciones de interpolación).

### Matriz de Rigidez Elemental

La **matriz de rigidez elemental** K_e para un elemento de barra 1D con propiedades uniformes es:

$$K_e = \frac{EA}{L_e}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$$

Donde:
- E: Módulo de Young
- A: Área de la sección transversal
- L_e: Longitud del elemento

Esta matriz relaciona las fuerzas nodales con los desplazamientos nodales del elemento:

$$\begin{bmatrix} F_1 \\ F_2 \end{bmatrix} = \frac{EA}{L_e}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$$

### Ensamblaje Global

Las matrices de rigidez elementales se ensamblan en una **matriz de rigidez global** K mediante el proceso de ensamblaje, que suma las contribuciones de cada elemento a los grados de libertad globales correspondientes.

El sistema global de ecuaciones es:

$$\mathbf{K}\mathbf{u} = \mathbf{F}$$

Donde:
- **K**: Matriz de rigidez global (n_nodos × n_nodos)
- **u**: Vector de desplazamientos nodales desconocidos
- **F**: Vector de fuerzas nodales aplicadas

### Condiciones de Contorno

Para que el sistema tenga solución única, deben aplicarse condiciones de contorno:

1. **Condiciones de contorno esenciales (Dirichlet)**: Especifican desplazamientos conocidos. Por ejemplo, u(0) = 0 para un extremo empotrado.

2. **Condiciones de contorno naturales (Neumann)**: Especifican fuerzas aplicadas en los nodos.

Al aplicar u(0) = 0, se reduce el sistema eliminando la primera fila y columna de K, obteniendo un sistema reducido que puede resolverse para los desplazamientos desconocidos.

### Solución Analítica Exacta

Para una barra con extremo empotrado en x=0 y carga F en x=L, la solución exacta es:

$$u(x) = \frac{Fx}{EA}$$

Esta es una función lineal, lo que significa que con elementos lineales, la solución FEM coincidirá exactamente con la solución analítica en los nodos.

## Ventajas del Método FEM

1. **Versatilidad**: Puede aplicarse a geometrías complejas y condiciones de carga variadas
2. **Precisión**: Con un mallado adecuado, proporciona soluciones muy precisas
3. **Extensibilidad**: Fácil extensión a problemas 2D, 3D y no lineales
4. **Implementación computacional**: Estructura matricial ideal para computación

## Referencias Teóricas

- La formulación FEM se basa en el principio de mínima energía potencial
- El método de Galerkin proporciona el marco matemático para la formulación débil
- La convergencia está garantizada cuando se refinan los elementos (teorema de convergencia FEM)

## Aplicaciones

El método presentado para barras 1D es la base para:
- Análisis de armaduras y estructuras reticuladas
- Problemas de transferencia de calor 1D
- Extensión a vigas (incluyendo flexión)
- Problemas más complejos en 2D y 3D
