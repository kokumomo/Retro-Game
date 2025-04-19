## 画面を切り替える
Stoneクラスから作られたオブジェクトを落ちてくる一つ一つの石として扱う

<img src="" width=400, height=250>

```python
SCREEN_HEIGHT = 120
STONE_INTERVAL = 30
GAME_OVER_DISPLAY_TIME = 60
START_SCENE = "start"
PLAY_SCENE = "play"

class Stone:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def update(self):
    if self.y < SCREEN_HEIGHT:
      self.y += 1
    
  def draw(self):
    pyxel.blt(self.x,self.y,0,8,0,8,8, pyxel.COLOR_BLACK)

class App:
  def __init__(self):
    pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title='サプーゲーム')
    pyxel.mouse(True)
    pyxel.load("my_resource.pyxres")

表示させるのはスタートかプレイ画面かの情報を持つcurrent_sceneインスタンス変数
    self.current_scene = START_SCENE
    pyxel.run(self.update, self.draw)

初期化する処理を作成、移動
  def reset_play_scene(self):
    self.player_x = SCREEN_WIDTH // 2
    self.player_y = SCREEN_HEIGHT * 4 // 5
    self.stones = []
    self.is_collision = False
    self.game_over_display_timer = GAME_OVER_DISPLAY_TIME

スタート画面のフレーム更新時の処理を書くメソッド作成
画面がクリックされたらプレイ画面に切り替わる
  def update_start_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
      self.reset_play_scene()
      self.current_scene = PLAY_SCENE

プレイ画面用フレームの更新処理を書くメソッドを作ってプレイ画面独自の処理を移動
is_collisionの値からゲームオーバーか判断
ゲームオーバーなら、タイマーの時間を減らして0ならスタート画面へ
  def update_play_scene(self):
    if self.is_collision:
      if self.game_over_display_timer > 0:
        self.game_over_display_timer -= 1
      else:
        self.current_scene = START_SCENE
      return

    if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 12:
      self.player_x += 1
    elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -4:
      self.player_x -= 1

    if pyxel.frame_count % STONE_INTERVAL == 0:
      self.stones.append(Stone(pyxel.rndi(0, SCREEN_WIDTH - 8), 0))

    for stone in self.stones.copy():
      stone.update()

      if (self.player_x <= stone.x <= self.player_x + 8 and self.player_y <= stone.y <= self.player_y + 8):
        self.is_collision = True

      if stone.y >= SCREEN_HEIGHT:
        self.stones.remove(stone)

  def update(self):
    if pyxel.btnp(pyxel.KEY_ESCAPE):
      pyxel.quit()

    if self.current_scene == START_SCENE:
      self.update_start_scene()
    elif self.current_scene == PLAY_SCENE:
      self.update_play_scene()

スタート画面の描画処理
表示させる位置を左上にしたいのでx座標は画面幅の10分の1,y座標は画面の高さの10分の1
  def draw_start_scene(self):
    pyxel.blt(0,0,0,32,0,160,120)
    pyxel.text(SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10, "click to Start", pyxel.COLOR_PINK)

プレイ画面の描画処理を行うためのメソッドを作成してプレイ画面独自の描画処理移動
  def draw_play_scene(self):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    for stone in self.stones:
      stone.draw()
    pyxel.blt(self.player_x, self.player_y, 0,16,0,16,16, pyxel.COLOR_BLACK)

    if self.is_collision:
      pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "Game Over", pyxel.COLOR_YELLOW)

  def draw(self):
    if self.current_scene == START_SCENE:
      self.draw_start_scene()
    elif self.current_scene == PLAY_SCENE:
      self.draw_play_scene()
    

App()
```






ReadMe.md ファイルを開いているときに、「Command + Shift + P」を押して、上のコマンドパレットに 「Markdown: Open Preview to the Side」と入力し選択すると、右側にマークダウンのプレビューを表示することができます。

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p>

<p align="center">
<a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

You may also try the [Laravel Bootcamp](https://bootcamp.laravel.com), where you will be guided through building a modern Laravel application from scratch.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains over 2000 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel [Patreon page](https://patreon.com/taylorotwell).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Cubet Techno Labs](https://cubettech.com)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[Many](https://www.many.co.uk)**
- **[Webdock, Fast VPS Hosting](https://www.webdock.io/en)**
- **[DevSquad](https://devsquad.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[OP.GG](https://op.gg)**
- **[WebReinvent](https://webreinvent.com/?utm_source=laravel&utm_medium=github&utm_campaign=patreon-sponsors)**
- **[Lendio](https://lendio.com)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
