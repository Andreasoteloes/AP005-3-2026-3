import time

inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]

w = 0.1
epochs = 10
learning_rate = 0.1
pause_time = 0

def predict(i):
    return w * i

for epoch in range(epochs):
    predictions = [predict(i) for i in inputs]
    errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    cost = sum(errors) / len(targets)
    
    errors_d = [2 * (p - t) for p, t in zip(predictions, targets)]
    weight_d = [e * i for e, i in zip(errors_d, inputs)]
    
    print("\n" + "=" * 65)
    print(f"ÉPOCA {epoch + 1}")
    print("=" * 65)
    
    for i, t, p, e, ed, wd in zip(inputs, targets, predictions, errors, errors_d, weight_d):
        print(f"Entrada: {i:>2} | Target: {t:>2} | Pred: {p:>8.4f} | Error^2: {e:>8.4f} | dE/dy: {ed:>8.4f} | dE/dw: {wd:>8.4f}")
    
    print("-" * 65)
    print(f"Peso antes de actualizar: {w:.10f}")
    print(f"Costo promedio: {cost:.6f}")
    
    gradient = sum(weight_d) / len(weight_d)
    print(f"Gradiente promedio: {gradient:.6f}")
    
    w -= learning_rate * gradient
    print(f"Peso después de actualizar: {w:.10f}")
    
    time.sleep(pause_time)

test_inputs = [5, 6]
test_targets = [10, 12]

print("\n" + "=" * 65)
print("PRUEBA FINAL")
print("=" * 65)

test_predictions = [predict(i) for i in test_inputs]

for i, t, p in zip(test_inputs, test_targets, test_predictions):
    print(f"Entrada: {i:>2} | Target: {t:>2} | Predicción: {p:>8.4f}")
