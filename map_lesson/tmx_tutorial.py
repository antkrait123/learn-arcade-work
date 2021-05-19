import arcade

WIDTH = 600
HEIGHT = 600

TITLE = "TMX lesson"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.coin_list = None
        self.wall_list = None
        self.player = None
        self.physics_engine = None
        self.level = 1
    
    def setup(self):
        self.player = arcade.Sprite("./images/dog.jpg")
        self.load_map = (f"./map_lesson/maps/level{self.level}.tmx")
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.wall_list,1)

    def load_map(self, resource):
        platforms_layer_name = "Platforms"
        coins_layer_name = "Coins"
        foreground_layer_name = "Detail"
        dont_touch_layer_name = "Death"

        my_map = arcade.tilemap.read_tmx(resource)

        self.wall_list = arcade.tilemap.process_layer(
            map_object = my_map,
            layer_name=platforms_layer_name,
            use_spatial_hash=True,
            scaling=0.5
        )

        self.coin_list = arcade.tilemap.process_layer(
            map_object = my_map,
            layer_name=coins_layer_name,
            scaling=0.5
        )

        self.foreground_list = arcade.tilemap.process_layer(
            map_object = my_map,
            layer_name=foreground_layer_name,
            scaling=0.5
        )

        self.dont_touch_list = arcade.tilemap.process_layer(
            map_object = my_map,
            layer_name=dont_touch_layer_name,
            scaling=0.5
        )


    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.wall_list.draw()
        self.dont_touch_list.draw()
        self.foreground_list.draw()
        self.player.draw()

game = Game()
game.setup()
arcade.run()












