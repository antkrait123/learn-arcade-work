import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.change_x = 0
        self.change_y = 0        

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        self.position_x += self.change_x
        self.position_y +=  self.change_y


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)


        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
         # create background
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
        arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
        arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_polygon_filled(((500, 400),
                                    (480, 360),
                                    (470, 320),
                                    (530, 320),
                                    (520, 360)
                                    ),
                                arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(500,550,40, arcade.color.YELLOW)
        arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
        arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
        self.ball.draw()

    # def on_mouse_motion(self, x, y, dx, dy):
    #     """ Called to update our objects. Happens approximately 60 times per second."""
    #     self.ball.position_x = x
    #     self.ball.position_y = y

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.ball.change_y += 1

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()

main()