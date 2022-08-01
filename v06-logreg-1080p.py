from audioop import reverse
from tkinter import CENTER, font
from manim import *
import numpy as np
from math import dist


config.max_files_cached = 3000

class LogReg(Scene): 
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

        text_1 = 'فرض کنید ما یک مسئله‌ی رده‌بندی باینری داشته باشیم. یعنی'
        text_1 = Tex_fa(text_1).to_edge(RIGHT, buff=1).shift(UP*5)
        text_2 = 'متغیر هدف ما فقط دو مقدار به خودش می‌گیره. مثلا 0 و 1.'
        text_2 = Tex_fa(text_2).next_to(text_1,DOWN).align_to(text_1,RIGHT)

        self.wait(0.5)
        self.play(Write(text_1), reverse=True)
        self.wait(1)
        self.play(Write(text_2), reverse=True)
        self.wait(1)

        text_3 = 'هدف ما در اینجا مثل رگرسیون خطی اینه که با توجه به مشاهدات'
        text_3 = Tex_fa(text_3).next_to(text_2, DOWN*6).align_to(text_1, RIGHT)
        text_4 = 'مقدار مورد انتظار از متغیر هدف چه قدر خواهد بود. یعنی:'
        text_4 = Tex_fa(text_4).next_to(text_3, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_3), reverse=True)
        self.wait(1)
        self.play(Write(text_4), reverse=True)
        self.wait(1)

        text_eq_expect = MathTex(r'E \Big[Y | X = x\Big]', font_size=font_size_math).next_to(text_4, DOWN*6).to_edge(LEFT, buff=1)

        self.play(Write(text_eq_expect))
        self.wait(1)

        text_eq_expect_bin = MathTex(r'= \sum_y y\,\mathbb{P}(Y = y|X=x)', font_size=font_size_math).next_to(text_eq_expect, RIGHT).shift(DOWN*0.27)

        self.play(Write(text_eq_expect_bin))
        self.wait(1)

        text_eq_expect_bin_2 = MathTex(r'= &1 \times \mathbb{P}(Y = 1|X = x) +\\ &0 \times \mathbb{P}(Y = 0|X = x)', font_size=font_size_math).next_to(text_eq_expect_bin, DOWN*3).align_to(text_eq_expect_bin, LEFT)

        self.play(Write(text_eq_expect_bin_2))
        self.wait(1)

        text_4_1 = 'بنابراین:'
        text_4_1 = Tex_fa(text_4_1).next_to(text_eq_expect_bin_2, DOWN*2).align_to(text_1, RIGHT)
        self.play(Write(text_4_1), reverse=True)
        self.wait(1)

        text_eq_expect_bin_3 = MathTex(r'E \Big[ Y | X = x \Big] = \mathbb{P}(Y = 1|X = x) = p(x; \beta)', font_size=font_size_math).next_to(text_4_1, DOWN).align_to(text_1, LEFT)

        self.play(Write(text_eq_expect_bin_3))
        self.wait(1)

        self.play(FadeOut(select_mobjs(text_eq_expect_bin_3)), text_eq_expect_bin_3.animate.move_to(text_1.get_center()).align_to(text_1, LEFT))


        # text_5 = 'امیدریاضی متغیر هدف در رگرسیون خطی کراندار نیست و هر'
        # text_5 = Tex_fa(text_5).next_to(text_eq_expect_bin_3, DOWN).align_to(text_1, RIGHT)
        # text_6 = 'عدد حقیقی میتونه باشه. اما توی مسئله‌ی باینری ما، این'
        # text_6 = Tex_fa(text_6).next_to(text_5, DOWN).align_to(text_1, RIGHT)
        # text_7 = 'امیدریاضی یک عدد بین صفر و یک بدست اومد. دانشمندهای'
        # text_7 = Tex_fa(text_7).next_to(text_6, DOWN).align_to(text_1, RIGHT)
        # text_8 = 'علم آمار تلاش میکردن به نحوی از رگرسیون خطی برای حل'
        # text_8 = Tex_fa(text_8).next_to(text_7, DOWN).align_to(text_1, RIGHT)
        # text_9 = 'این مسئله و یافتن بهترین مدل استفاده کنن.'
        # text_9 = Tex_fa(text_9).next_to(text_8, DOWN).align_to(text_1, RIGHT)

        
        p1, p2 = brace_points(text_eq_expect_bin_3[0][20].get_left(), text_eq_expect_bin_3[0][25].get_right(), 0.2, 0.15)
        brace_1 = BraceBetweenPoints(p1, p2)
        self.play(FadeIn(brace_1))
        self.wait(1)

        # self.play(Write(text_5), reverse=True)
        # self.wait(1)
        # self.play(Write(text_6), reverse=True)
        # self.wait(1)
        # self.play(Write(text_7), FadeIn(brace_1), reverse=True)
        # self.play()
        # self.wait(1)
        # self.play(Write(text_8), reverse=True)
        # self.wait(1)
        # self.play(Write(text_9), reverse=True)
        # self.wait(1)

        
        text_10 = 'اگر در خاطرتون باشه، توی رگرسیون خطی داشتیم:'
        text_10 = Tex_fa(text_10).next_to(text_eq_expect_bin_3, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_10), reverse=True)
        self.wait(1)

        text_linear_expect = MathTex(r'E \Big[ Y | X = x \Big] = \beta_0 + \sum_{j=1}^m \beta_j x_j', font_size=font_size_math).next_to(text_10, DOWN).align_to(text_1, LEFT)
        
        self.play(Write(text_linear_expect))
        self.wait(1)

        # defines the axes and linear function
        axes = Axes(x_range=[-1,10], y_range=[-1,10], x_length=5, y_length=5).shift(LEFT*3)

        # Adding dots to the data
        np.random.seed(1)
        points_x = np.random.uniform(1, 8, 20)
        f = lambda x: 0.75*x + 1
        np.random.seed(2)
        points_y = f(points_x) + np.random.normal(0, 0.5, 20)

        a = np.column_stack((points_x, points_y))

        dots_group = VGroup()
        dots_group.add(*[Dot(axes.c2p(x,y)) for x, y in a])

        # Adding the coordinate system
        self.add(axes)

        # Adding the data points
        self.play(Create(axes), run_time=1.5)
        self.wait(1.5)
        self.add(dots_group.set_fill('#FCA311', opacity=0.75))
        self.play(Create(dots_group), lag_ratio = 1)
        
        # Adding the regression line
        func = axes.plot(lambda x: 0.75*x + 1, x_range=[0.5, 9])
        self.add(func.set_color('#AE2012'))
        self.play(Create(func))

        text_11 = 'اگر بخوایم توی این مسئله ازش استفاده کنیم خواهیم داشت:'
        text_11 = Tex_fa(text_11).next_to(text_linear_expect, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_11), reverse=True)
        self.wait(1)


        text_linear_prob = MathTex(r'p(x; \beta) = \beta_0 + \sum_{j=1}^m \beta_j x_j', font_size=font_size_math).next_to(text_11, DOWN).align_to(text_1, LEFT)

        self.play(Write(text_linear_prob))
        self.wait(1)

        self.play(FadeOut(select_mobjs(text_linear_prob)), text_linear_prob.animate.move_to(text_1.get_center()).align_to(text_1, LEFT))

        text_12 = 'سمت راست معادله از هر دو طرف بی‌کرانه ولی سمت چپ از هر'
        text_12 = Tex_fa(text_12).next_to(text_linear_prob, DOWN).align_to(text_1, RIGHT)
        text_13 = 'دو طرف کراندار (صفر و یک). بنابراین از این مدل خطی نمیتونیم'
        text_13 = Tex_fa(text_13).next_to(text_12, DOWN).align_to(text_1, RIGHT)
        text_14 = 'استفاده کنیم و باید تبدیلش کنیم. مثلا تبدیل لگاریتم:'
        text_14 = Tex_fa(text_14).next_to(text_13, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_12), reverse=True)
        self.wait(1)
        self.play(Write(text_13), reverse=True)
        self.wait(1)
        self.play(Write(text_14), reverse=True)
        self.wait(1)

        text_log_prob = MathTex(r'log(p(x; \beta)) = \beta_0 + \sum_{j=1}^m \beta_j x_j', font_size=font_size_math).next_to(text_14, DOWN).align_to(text_1, LEFT)

        self.play(Write(text_log_prob))
        self.wait(1)

        text_15 = 'با این تبدیل اوضاع کمی بهتر میشه اما هنوز از یک طرف کرانداری'
        text_15 = Tex_fa(text_15).next_to(text_log_prob, DOWN).align_to(text_1, RIGHT)
        text_16 = 'وجود داره. پس دانشمندها به فکر استفاده از تبدیل دیگه‌ای افتادن'
        text_16 = Tex_fa(text_16).next_to(text_15, DOWN).align_to(text_1, RIGHT)
        text_17 = 'به اسم تبدیل لُجیت، یا لجستیک که به این صورت بود:'
        text_17 = Tex_fa(text_17).next_to(text_16, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_15), reverse=True)
        self.wait(1)
        self.play(Write(text_16), reverse=True)
        self.wait(1)
        self.play(Write(text_17), reverse=True)
        self.wait(1)

        text_logit_prob = MathTex(r'log(\frac{p}{1-p}) = \beta_0 + \sum_{j=1}^m \beta_j x_j', font_size = font_size_math).next_to(text_17, DOWN).align_to(text_1, LEFT)

        self.play(Write(text_logit_prob))
        self.wait(1)

        self.play(FadeOut(select_mobjs(text_logit_prob)), text_logit_prob.animate.move_to(text_1.get_center()).align_to(text_1, LEFT))


        text_19 = 'هر دو طرف این معادله بیکران هستند. بنابراین میتونیم از'
        text_19 = Tex_fa(text_19).next_to(text_logit_prob, DOWN).align_to(text_1, RIGHT)
        text_20 = 'این تبدیل استفاده کنیم. پس:'
        text_20 = Tex_fa(text_20).next_to(text_19, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_19), reverse=True)
        self.play(Write(text_20), reverse=True)
        self.wait(1)

        text_logit_expect = MathTex(r'E \left[ Y | X = x \right] &= p(x; \beta)\\ &= \frac{1}{1 + \exp{-(\beta_0 + \sum_{j=1}^m \beta_j x_j)}',
            font_size=font_size_math).next_to(text_20, DOWN).align_to(text_1, LEFT)
        
        self.play(Write(text_logit_expect))
        self.wait(1)

        text_21 = 'حالا اینجا هم مثل رگرسیون خطی از روش ماکسیمم درستنمایی'
        text_21 = Tex_fa(text_21).next_to(text_logit_expect, DOWN).align_to(text_1, RIGHT)
        text_22 = 'برای برآورد پارامترها و یافتن بهترین مدل استفاده میکنیم.'
        text_22 = Tex_fa(text_22).next_to(text_21, DOWN).align_to(text_1, RIGHT)
        text_23 = 'توجه داریم که توزیع متغیر هدف ما به شرط مشاهدات، برنولیه.'
        text_23 = Tex_fa(text_23).next_to(text_22, DOWN).align_to(text_1, RIGHT)
        text_24 = 'بنابراین:'
        text_24 = Tex_fa(text_24).next_to(text_23, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_21), reverse=True)
        self.wait(1)
        self.play(Write(text_22), reverse=True)
        self.wait(1)
        self.play(Write(text_23), reverse=True)
        self.play(Write(text_24), reverse=True)

        text_likelihood = MathTex(r'\mathcal{L} &= \prod_{i=1}^{n} \mathbb{P} (Y = y_i | X = x_i)\\ &= \prod_{i=1}^{n} p(x_i; \beta)^{y_i} (1 - p(x_i; \beta))^{1 - y_i}',
            font_size=font_size_math).next_to(text_24, DOWN).align_to(text_1, LEFT)
        self.play(Write(text_likelihood))
        self.wait(1)

        self.play(FadeOut(select_mobjs(text_likelihood)), text_likelihood.animate.move_to(text_1.get_center()).align_to(text_1, LEFT))
        self.wait(1)

        text_25 = 'برای راحتی بیشتر از تابع درستنمایی لگاریتم میگیریم:'
        text_25 = Tex_fa(text_25).next_to(text_likelihood, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_25), reverse=True)
        self.wait(1)

        text_log_likelihood = MathTex(r'\sum_{i=1}^n \Big[ y_i log(p(x_i; \beta)) + (1 - y_i) log(1 - p(x_i; \beta)) \Big]',
            font_size=font_size_math).next_to(text_25, DOWN).align_to(text_1, LEFT)

        self.play(Write(text_log_likelihood))
        self.wait(1)

        text_26 = 'حالا کافیه که به ازای هر پارامتر مشتق بگیریم و برابر با صفر قرار'
        text_26 = Tex_fa(text_26).next_to(text_log_likelihood, DOWN).align_to(text_1, RIGHT)
        text_27 = 'بدیم. اما این معادله هیچ جواب فرم بسته‌ای نداره. پس باید'
        text_27 = Tex_fa(text_27).next_to(text_26, DOWN).align_to(text_1, RIGHT)
        text_28 = 'برای حلش از روش‌های عددی استفاده بشه.'
        text_28 = Tex_fa(text_28).next_to(text_27, DOWN).align_to(text_1, RIGHT)
        

        self.play(Write(text_26), reverse=True)
        self.play(Write(text_27), reverse=True)
        self.play(Write(text_28), reverse=True)

        self.wait(1)

        text_29 = 'به عنوان مثال الگوریتم \lr{Reweighted Least Squares}.'
        text_29 = Tex_fa(text_29).next_to(text_28, DOWN*3).align_to(text_1, RIGHT)

        self.play(Write(text_29), reverse=True)
        self.wait(1)

        self.play(FadeOut(select_mobjs()))

        text_30 = Text('mlwithsaeid', font_size=70, font='Lato')
        rect = SurroundingRectangle(text_30, color=BLUE, buff=MED_LARGE_BUFF)

        self.play(Create(rect), Write(text_30))
        self.wait(1)
        self.play(FadeOut(select_mobjs()))