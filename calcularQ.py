def find_unsuccessful_searches(frequencies):
    unsuccessful_searches = []
    total_frequency = sum(frequencies)
    cumulative_probability = 0.0

    for freq in frequencies:
        # Calcular la probabilidad acumulativa de búsqueda exitosa hasta el elemento actual
        cumulative_probability += freq / total_frequency

        # Calcular la probabilidad de búsqueda infructuosa entre este elemento y el anterior
        unsuccessful_search_probability = cumulative_probability - (freq / (2 * total_frequency))

        unsuccessful_searches.append(unsuccessful_search_probability)

    # Añadir la probabilidad de búsqueda infructuosa entre el último elemento y el "elemento ficticio"
    unsuccessful_searches.append(1.0 - (1.0 / (2 * total_frequency)))

    return unsuccessful_searches

# Ejemplo de uso
frequencies = [0.1, 0.2, 0.3, 0.25, 0.15]
unsuccessful_searches = find_unsuccessful_searches(frequencies)
print("Probabilidades de búsqueda infructuosa entre elementos consecutivos:")
for i, prob in enumerate(unsuccessful_searches):
    print(f"Entre elementos {i} y {i+1}: {prob:.4f}")







