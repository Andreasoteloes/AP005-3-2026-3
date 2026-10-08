import time

inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]

w = 0.1
learning_rate = 0.1
epochs = 30
pause_time = 0

def predict(i):
    return w * i

for epoch in range(epochs):
    predictions = [predict(i) for i in inputs]
    errors = [t - p for p, t in zip(predictions, targets)]
    cost = sum(errors) / len(targets)
    
    print("\n" + "=" * 60)
    print(f"ÉPOCA {epoch + 1}")
    print("=" * 60)
    for i, t, p, e in zip(inputs, targets, predictions, errors):
        print(f"Entrada: {i:>2} | Target: {t:>2} | Predicción: {p:>8.4f} | Error: {e:>8.4f}")
    
    print("-" * 60)
    print(f"Peso antes de actualizar: {w:.10f}")
    print(f"Error promedio: {cost:.6f}")
    
    w += learning_rate * cost
    
    print(f"Peso después de actualizar: {w:.10f}")
    time.sleep(pause_time)

test_inputs = [5, 6]
test_targets = [10, 12]

print("\n" + "=" * 60)
print("PRUEBA FINAL")
print("=" * 60)

test_predictions = [predict(i) for i in test_inputs]

for i, t, p in zip(test_inputs, test_targets, test_predictions):
    print(f"Entrada: {i:>2} | Target: {t:>2} | Predicción: {p:>8.4f}")
