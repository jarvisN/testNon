import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm

# โหลดข้อมูล
sugar = pd.read_csv("ความหวาน.csv")
dataSugar = sugar.iloc[130:250, 1:2]
valueSugar = dataSugar['brix(%)'].values

dataSam = pd.read_csv('all_files_t.csv')
dataGraph = dataSam.iloc[:, 1:]
X = dataGraph.transpose()
y = valueSugar

# ปรับขนาดข้อมูล
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# รับค่าจำนวนชั้นและนิวรอนสูงสุดผ่าน input
max_layers = int(input("Enter the maximum number of layers: "))
max_neurons = int(input("Enter the maximum number of neurons: "))

best_size = None
best_score = float('inf')

# วนลูปเพื่อหาค่า hidden_layer_sizes ที่ดีที่สุด โดยใช้ tqdm แสดงความคืบหน้า
for layer in tqdm(range(1, max_layers + 1), desc="Layers Progress"):
    for neuron in tqdm(range(1, max_neurons + 1), desc="Neurons Progress", leave=False):
        size = (neuron,) * layer
        mlp_regressor = MLPRegressor(hidden_layer_sizes=size, activation='relu', solver='adam', max_iter=1000000, random_state=42, early_stopping=True)
        mlp_regressor.fit(X_train, y_train)
        predictions = mlp_regressor.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        
        if mse < best_score:
            best_score = mse
            best_size = size

print(f"Best Hidden Layer Sizes: {best_size} with MSE: {best_score}")