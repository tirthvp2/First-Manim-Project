# from manim import *
#
#
# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen

from manim import *


class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            # \[e^{i \phi} = \text{cos}\phi + i\text{sin}\phi = \frac{(3+i)}{\sqrt{10}}\]
            # r"\frac{d}{dx}f(x)g(x)e^{i\phi}=",
            # r"f(x)\frac{d}{dx}g(x){cos}\pi",
            # r"+",
            # r"g(x)\frac{d}{dx}f(x)i{sin}\pi",
            r"e^{i\pi}=",
            r"{cos}\pi",
            r"+",
            r"i{sin}\pi"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=.1)
        framebox2 = SurroundingRectangle(text[3], buff=.1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()
