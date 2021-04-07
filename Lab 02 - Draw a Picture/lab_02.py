import arcade

arcade.open_window(800,800, "The Game")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.GREEN)
arcade.finish_render()
arcade.run()








'''import arcade

WIDTH = 1200
HEIGHT = 800

def on_draw(change_time):
    arcade.start_render()

    arcade.draw_circle_filled(on_draw.x, on_draw.y, 35, arcade.color.RED)
    on_draw.x += on.draw.vx
    on_draw.y += on.draw.vy


on_draw.x = 100
on_draw.y = 100


arcade.open_window(WIDTH, HEIGHT, "Bounce!")
arcade.set_background_color(arcade.color.YELLOW)
arcade.schedule(on_draw, 1/120)
arcade.start_render()


arcade.run()'''

