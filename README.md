岩の位置は画面の中央に表示 SCREEN_WIDTH // 2
y座標は0
イメージバンクのインデックス番号は0
イメージバンクのX座標は8
イメージバンクのY座標は0
ピクセルアートの幅は8
ピクセルアートの高さは8
透明として扱うカラーはCOLOR_BLACK

プレイヤーの位置は画面中央下部に表示 SCREEN_WIDTH // 2, SCREEN_HEIGHT * 4 // 5(5分の4)
ピクセルアートのx座標、幅、高さは16

def draw(self):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    pyxel.blt(SCREEN_WIDTH // 2,0,0,8,0,8,8, pyxel.COLOR_BLACK)
    pyxel.blt(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 4 // 5, 0,16,0,16,16, pyxel.COLOR_BLACK)


<img src="https://img.shields.io/badge/-{言語、フレームワーク名など}-{シールドのカラーコード}.svg?logo=next.js&style={バッチのスタイル}&logoColor={ロゴのカラーコード}">
