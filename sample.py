import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------p
# パターン1: 座標セット [[x1, y1], [x2, y2], ...] のプロット
# --------------------------------------------------
# 1. データの生成
x = np.linspace(0, 10, 50)
y = 2 * x + 1
# 2次元配列にする (形状: 50行2列)
line_coordinates = np.stack([x, y], axis=1)

# 2. プロット処理
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
# 2次元配列から X座標(0列目) と Y座標(1列目) を抽出して描画
plt.plot(line_coordinates[:, 0], line_coordinates[:, 1], color='blue', linewidth=2)
plt.scatter(line_coordinates[:, 0], line_coordinates[:, 1], color='red', s=15) # 点も表示
plt.title("Pattern 1: Coordinate List\n(shape: [50, 2])")
plt.grid(True)
# --------------------------------------------------
# パターン2: 格子状データ (画像・ヒートマップ) のプロット
# --------------------------------------------------
# 1. 縦横の格子データ生成
x_grid = np.linspace(0, 10, 100)
y_grid = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x_grid, y_grid)

# 2次元空間上に直線の壁（平面）を作る (y = 2x + 1 の変化を2次元配列にする)
z_line_2d = 2 * X + 1

# 2. プロット処理
plt.subplot(1, 2, 2)
# pcolormeshで2次元配列を色（ヒートマップ）として可視化
plt.pcolormesh(X, Y, z_line_2d, shading='auto', cmap='viridis')
plt.colorbar(label='Z value (2X + 1)')
plt.title("Pattern 2: Grid Data\n(shape: [100, 100])")

plt.tight_layout()
plt.show()