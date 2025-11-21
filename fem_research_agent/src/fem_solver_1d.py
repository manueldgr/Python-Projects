import numpy as np
import matplotlib.pyplot as plt

def fem_1d_elastic_bar(L, A, E, num_elements, force_at_end):
    """
    Resuelve el desplazamiento de una barra elástica 1D usando FEM.
    Parámetros:
    L: Longitud total, A: Área, E: Módulo de Young, num_elements: Divisiones, force_at_end: Carga
    """
    num_nodes = num_elements + 1
    node_coords = np.linspace(0, L, num_nodes)
    element_length = L / num_elements
    
    K = np.zeros((num_nodes, num_nodes))
    F = np.zeros(num_nodes)
    k_e = (A * E / element_length)
    
    for i in range(num_elements):
        n1, n2 = i, i + 1
        K[n1, n1] += k_e
        K[n1, n2] -= k_e
        K[n2, n1] -= k_e
        K[n2, n2] += k_e

    F[-1] = force_at_end
    
    # Condiciones de contorno (u[0] = 0)
    K_reduced = K[1:, 1:]
    F_reduced = F[1:]
    
    u_reduced = np.linalg.solve(K_reduced, F_reduced)
    u = np.zeros(num_nodes)
    u[1:] = u_reduced
    
    return node_coords, u

if __name__ == "__main__":
    Length = 1.0
    Area = 0.01
    YoungMod = 210e9
    Load = 10000
    Elements = 10
    
    nodes, displacements = fem_1d_elastic_bar(Length, Area, YoungMod, Elements, Load)
    
    print("Nodos:", nodes)
    print("Desplazamientos:", displacements)
    
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, displacements, 'o-', label='FEM Aproximación')
    x_exact = np.linspace(0, Length, 100)
    u_exact = (Load * x_exact) / (Area * YoungMod)
    plt.plot(x_exact, u_exact, 'r--', label='Solución Exacta')
    plt.title('Análisis FEM 1D: Barra Elástica')
    plt.xlabel('Posición (m)')
    plt.ylabel('Desplazamiento (m)')
    plt.legend()
    plt.grid(True)
    plt.savefig('fem_result_plot.png')
    print("Gráfica guardada como fem_result_plot.png")
