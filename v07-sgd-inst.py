from audioop import reverse
from re import S
from select import select
from tkinter import CENTER, font
from manim import *
from matplotlib.pyplot import text
import numpy as np
from math import dist, exp
from statistics import mean, stdev


config.max_files_cached = 3000

class SGD_still(Scene):
    def construct(self):
        self.camera.background_color = '#14213D'
        
        axes_1 = Axes(x_range=[-4,4], y_range=[-1,10], x_length=7, y_length=7).shift(DOWN)
        self.add(axes_1)

        func = axes_1.plot(lambda x: (x)**2, x_range=[-3,3])
        self.add(func.set_color('#AE2012'))
        self.add(func)


        x_points = [2.5, -2, 1.3, -0.5, 0.2, 0]
        f = lambda x: x**2
        y_points = list(map(f, x_points))

        
        dot_0 = Dot(axes_1.c2p(x_points[0], y_points[0]))
        slopes_0 = axes_1.get_secant_slope_group(
                x = x_points[0],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )


        dot_1 = Dot(axes_1.c2p(x_points[1], y_points[1]))
        slopes_1 = axes_1.get_secant_slope_group(
                x = x_points[1],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_1 = DashedLine(dot_0, dot_1)

        dot_2 = Dot(axes_1.c2p(x_points[2], y_points[2]))
        slopes_2 = axes_1.get_secant_slope_group(
                x = x_points[2],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_2 = DashedLine(dot_1, dot_2)

        dot_3 = Dot(axes_1.c2p(x_points[3], y_points[3]))
        slopes_3 = axes_1.get_secant_slope_group(
                x = x_points[3],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_3 = DashedLine(dot_2, dot_3)

        dot_4 = Dot(axes_1.c2p(x_points[4], y_points[4]))
        slopes_4 = axes_1.get_secant_slope_group(
                x = x_points[4],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_4 = DashedLine(dot_3, dot_4)

        dot_5 = Dot(axes_1.c2p(x_points[5], y_points[5]))
        slopes_5 = axes_1.get_secant_slope_group(
                x = x_points[5],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_5 = DashedLine(dot_4, dot_5)

        self.add(dot_0, dot_1, dot_2, dot_3, dot_4, dot_5, 
                          dashed_1, dashed_2, dashed_3, dashed_4, dashed_5, 
                          slopes_0, slopes_1, slopes_2, slopes_3, slopes_4, slopes_5)

class SGD(Scene): 
    def construct(self):
        self.camera.background_color = '#14213D'
        font_size_text = 48
        font_size_math = 55
        # font_size_matrices=45

        def Tex_fa(text, font_size_text=font_size_text):
            return Tex(text, font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian)

        
        # function to select all but one mobject
        def select_mobjs(*mobjs):
            """
            Select all mobjects in the scene except the one mobject given in the input.
            """
            all_objs = VGroup()
            for obj in self.mobjects:
                if((isinstance(obj, VMobject) == True) and obj not in mobjs):
                    all_objs.add(obj)
            return all_objs


        # a function to get the points of an mobject/vmobject and return the points of the apropriate braces
        def brace_points(point_1, point_2, expand_size_h, expand_size_v):
            """
            This function provides two points for braces based on the
            two given points which can be far left and far right of an
            mobject/vmobject. 
            """
            if (expand_size_h < 0 or expand_size_v < 0):
                raise Exception('expand sizes must be positive')
            p1 = point_1
            p2 = point_2
            
            p1[0] -= expand_size_h
            p1[1] -= expand_size_v

            p2[0] += expand_size_h
            p2[1] -= expand_size_v

            if (p1[1] != p2[1]):
                p1[1] = max(p1[1], p2[1])
                p2[1] = max(p1[1], p2[1])

            return p1, p2

        axes_1 = Axes(x_range=[-4,4], y_range=[-1,10], x_length=7, y_length=7)
        self.play(Create(axes_1))

        func = axes_1.plot(lambda x: (x)**2, x_range=[-3,3])
        self.add(func.set_color('#AE2012'))
        self.play(Create(func))


        x_points = [2.5, -2, 1.3, -0.5, 0.2, 0]
        f = lambda x: x**2
        y_points = list(map(f, x_points))

        
        dot_0 = Dot(axes_1.c2p(x_points[0], y_points[0]))
        slopes_0 = axes_1.get_secant_slope_group(
                x = x_points[0],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )


        dot_1 = Dot(axes_1.c2p(x_points[1], y_points[1]))
        slopes_1 = axes_1.get_secant_slope_group(
                x = x_points[1],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_1 = DashedLine(dot_0, dot_1)

        dot_2 = Dot(axes_1.c2p(x_points[2], y_points[2]))
        slopes_2 = axes_1.get_secant_slope_group(
                x = x_points[2],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_2 = DashedLine(dot_1, dot_2)

        dot_3 = Dot(axes_1.c2p(x_points[3], y_points[3]))
        slopes_3 = axes_1.get_secant_slope_group(
                x = x_points[3],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_3 = DashedLine(dot_2, dot_3)

        dot_4 = Dot(axes_1.c2p(x_points[4], y_points[4]))
        slopes_4 = axes_1.get_secant_slope_group(
                x = x_points[4],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_4 = DashedLine(dot_3, dot_4)

        dot_5 = Dot(axes_1.c2p(x_points[5], y_points[5]))
        slopes_5 = axes_1.get_secant_slope_group(
                x = x_points[5],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_5 = DashedLine(dot_4, dot_5)

        self.play(Create(dot_0), Create(dot_1), Create(dot_2), Create(dot_3), Create(dot_4), Create(dot_5), 
                          Create(dashed_1), Create(dashed_2), Create(dashed_3), Create(dashed_4), Create(dashed_5), 
                          Create(slopes_0), Create(slopes_1), Create(slopes_2), Create(slopes_3), Create(slopes_4), Create(slopes_5))

        self.play(FadeOut(select_mobjs()))

        text_1 = 'توی این ویدیو می‌خوام خیلی کوتاه در مورد رگرسیون خطی'
        text_1 = Tex_fa(text_1).to_edge(RIGHT, buff=1).shift(UP*9)

        text_2 = 'با استفاده از الگوریتم گرادیان کاهشی تصادفی صحبت کنم.'
        text_2 = Tex_fa(text_2).next_to(text_1, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_1), reverse=True)
        self.play(Write(text_2), reverse=True)
        self.wait(2)

        text_3 = 'اول اینکه مراحلش به این صورته:'
        text_3 = Tex_fa(text_3).next_to(text_2, DOWN*1.5).align_to(text_1, RIGHT)

        self.play(Write(text_3), reverse=True)


        text_4 = Tex(r"""\item $\beta := \beta_0$ (initial value assignment)\\ \vspace{-5mm} \item $\mathrm{D}_\beta := \frac{\partial \textrm{MSE}}{\partial \beta}$ \\ 
            \vspace{-5mm} \item update $\beta$: $\beta = \beta - L\times \mathrm{D}_\beta$ \\ \vspace{-5mm}\item Update MSE based on new $\beta$\\ \vspace{-5mm}
            \item repeat steps 2 to 4""", 
            font_size=font_size_math, tex_environment='enumerate').next_to(text_3, DOWN*2).to_edge(LEFT, buff=1)
        self.play(Write(text_4))

        self.wait(13)
        
        text_5 = 'قسمت تصادفی ماجرا برای اینه که در هر تکرار فقط از یک'
        text_5 = Tex_fa(text_5).next_to(text_4, DOWN*2).align_to(text_1, RIGHT)

        self.play(Write(text_5), reverse=True)

        text_6 = 'مشاهده برای انجام مراحل استفاده بشه.'
        text_6 = Tex_fa(text_6).next_to(text_5, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_6), reverse=True)
        
        axes_1 = Axes(x_range=[-4,4], y_range=[-1,10], x_length=7, y_length=7).shift(DOWN*4)
        self.play(Create(axes_1))

        func = axes_1.plot(lambda x: (x)**2, x_range=[-3,3])
        self.add(func.set_color('#AE2012'))
        self.play(Create(func))
        self.wait(2)

        x_points = [2.5, -2, 1.3, -0.5, 0.2, 0]
        f = lambda x: x**2
        y_points = list(map(f, x_points))

        
        dot_0 = Dot(axes_1.c2p(x_points[0], y_points[0]))
        slopes_0 = axes_1.get_secant_slope_group(
                x = x_points[0],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        
        self.play(Create(dot_0))
        self.play(Create(slopes_0))
        self.wait(2)

        dot_1 = Dot(axes_1.c2p(x_points[1], y_points[1]))
        slopes_1 = axes_1.get_secant_slope_group(
                x = x_points[1],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_1 = DashedLine(dot_0, dot_1)
        self.play(Create(dashed_1), run_time=0.25)
        self.play(Create(dot_1))
        self.play(Create(slopes_1))

        dot_2 = Dot(axes_1.c2p(x_points[2], y_points[2]))
        slopes_2 = axes_1.get_secant_slope_group(
                x = x_points[2],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_2 = DashedLine(dot_1, dot_2)
        self.play(Create(dashed_2), run_time=0.25)
        self.play(Create(dot_2))
        self.play(Create(slopes_2))
        self.wait(3)

        dot_3 = Dot(axes_1.c2p(x_points[3], y_points[3]))
        slopes_3 = axes_1.get_secant_slope_group(
                x = x_points[3],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_3 = DashedLine(dot_2, dot_3)
        # self.play(Create(dashed_3), run_time=0.25)
        # self.play(Create(dot_3))
        # self.play(Create(slopes_3))

        dot_4 = Dot(axes_1.c2p(x_points[4], y_points[4]))
        slopes_4 = axes_1.get_secant_slope_group(
                x = x_points[4],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_4 = DashedLine(dot_3, dot_4)
        # self.play(Create(dashed_4), run_time=0.25)
        # self.play(Create(dot_4))
        # self.play(Create(slopes_4))

        dot_5 = Dot(axes_1.c2p(x_points[5], y_points[5]))
        slopes_5 = axes_1.get_secant_slope_group(
                x = x_points[5],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_5 = DashedLine(dot_4, dot_5)
        # self.play(Create(dashed_5), run_time=0.25)
        # self.play(Create(dot_5))
        # self.play(Create(slopes_5))

        self.play(Create(dot_3), Create(dot_4), Create(dot_5), 
                          Create(dashed_3), Create(dashed_4), Create(dashed_5), 
                          Create(slopes_3), Create(slopes_4), Create(slopes_5))

        self.wait(2)

        self.play(FadeOut(dot_1, dot_2, dot_3, dot_4, dot_5, 
                          dashed_1, dashed_2, dashed_3, dashed_4, dashed_5, 
                          slopes_1, slopes_2, slopes_3, slopes_4, slopes_5))

        # Small learning rate
        x_points = [2.5, 1.75, 1, 0.35, -0.25, 0]
        y_points = list(map(f, x_points))
        
        dot_1 = Dot(axes_1.c2p(x_points[1], y_points[1]))
        slopes_1 = axes_1.get_secant_slope_group(
                x = x_points[1],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_1 = DashedLine(dot_0, dot_1)
        # self.play(Create(dashed_1), run_time=0.25)
        # self.play(Create(dot_1))
        # self.play(Create(slopes_1))

        dot_2 = Dot(axes_1.c2p(x_points[2], y_points[2]))
        slopes_2 = axes_1.get_secant_slope_group(
                x = x_points[2],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_2 = DashedLine(dot_1, dot_2)
        # self.play(Create(dashed_2), run_time=0.25)
        # self.play(Create(dot_2))
        # self.play(Create(slopes_2))

        dot_3 = Dot(axes_1.c2p(x_points[3], y_points[3]))
        slopes_3 = axes_1.get_secant_slope_group(
                x = x_points[3],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_3 = DashedLine(dot_2, dot_3)
        # self.play(Create(dashed_3), run_time=0.25)
        # self.play(Create(dot_3))
        # self.play(Create(slopes_3))

        dot_4 = Dot(axes_1.c2p(x_points[4], y_points[4]))
        slopes_4 = axes_1.get_secant_slope_group(
                x = x_points[4],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_4 = DashedLine(dot_3, dot_4)
        # self.play(Create(dashed_4), run_time=0.25)
        # self.play(Create(dot_4))
        # self.play(Create(slopes_4))

        dot_5 = Dot(axes_1.c2p(x_points[5], y_points[5]))
        slopes_5 = axes_1.get_secant_slope_group(
                x = x_points[5],
                graph=func,
                dx=0.005,
                secant_line_length=2,
                secant_line_color=YELLOW,
        )
        dashed_5 = DashedLine(dot_4, dot_5)
        # self.play(Create(dashed_5), run_time=0.25)
        # self.play(Create(dot_5))
        # self.play(Create(slopes_5))

        self.play(Create(dot_0), Create(dot_1), Create(dot_2), Create(dot_3), Create(dot_4), Create(dot_5), 
                          Create(dashed_1), Create(dashed_2), Create(dashed_3), Create(dashed_4), Create(dashed_5), 
                          Create(slopes_0), Create(slopes_1), Create(slopes_2), Create(slopes_3), Create(slopes_4), Create(slopes_5), run_time=4)

        self.wait(5)
