from audioop import reverse
from manim import *
import numpy as np
from math import dist


config.max_files_cached = 3000


class LinReg(Scene): 
    def construct(self):
        self.camera.background_color = '#14213D'
        font_size_text = 50
        font_size_math = 55
        font_size_matrices=45

        # first scene: intro of video
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

        self.wait(3)
        text2 = Tex("تئوری و فلسفه‌ی پشت رگرسیون خطی چیه؟", tex_template = TexTemplateLibrary.persian, font_size=font_size_text, color='#FCA311').shift(UP*2.2).shift(RIGHT)
        text1 = Tex("رگرسیون خطی چطور کار می‌کنه؟", tex_template = TexTemplateLibrary.persian, font_size=font_size_text, color='#FCA311').next_to(text2,UP).align_to(text2, direction=RIGHT)
        self.add(text2)
        self.play(Write(text1), reverse=True)
        self.wait(1)
        self.play(Write(text2), reverse=True)

        self.wait(1)
        # Fading Out the entire scene except dots
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(axes), FadeOut(func))

        self.wait(2)
        # Spread the dots
        for dot in dots_group:
            self.play(dot.animate.shift(RIGHT*np.random.uniform(low=2, high=-2,size=1)).shift(UP*np.random.uniform(low=-1.5, high=1.5, size=1)), run_time=0.1)
        
        # Adding explanations for observations
        text3 = Tex(r"\begin{flushright}در آمار و یادگیری ماشین ما مدل رو\\ بر اساس مشاهدات داده‌هامون می‌سازیم.\end{flushright}",
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(dots_group).shift(UP*3)
        self.play(FadeIn(text3), run_time=3)

        # Fading out all dots except one
        random_index = np.random.randint(low=0, high=len(dots_group) - 1)
        random_dot = dots_group[random_index]
        self.play(FadeOut(dots_group.remove(random_dot)), random_dot.animate.next_to(text3, LEFT*15))
        self.wait(1)

        # Adding context for that dot (an observation)
        text4 = Tex(r'$(y, X_1, X_2, \cdots, X_m)$', color='#FFFFFF').next_to(random_dot, DOWN)
        self.play(FadeIn(text4), run_time=1)
        self.wait(3)

        # Adding context for model y = f(X)
        text5 = Tex(r'$y = f(X_1, X_2, \cdots, X_m)$').next_to(text4, DOWN*1.2).align_to(text4,LEFT)
        self.play(Write(text5), run_time=2.5)
        
        self.wait(2)
        # animating f
        self.play(text5[0][2].animate.scale(2).shift(UP*0.2))
        self.play(text5[0][2].animate.scale(0.5).shift(DOWN*0.2))

        self.wait(3)
        # disappearing f
        self.play(FadeOut(text5[0][2]))
        
        self.wait(2)

        # Bringing the dots back
        for dot in dots_group:
            dot.shift(RIGHT*6)
            self.play(FadeIn(dot, shift=RIGHT*2), run_time=0.25)

        self.wait(3.2)

        sample_numbers = np.random.choice(range(len(dots_group)), replace=False, size=10)
        for i in sample_numbers:
            self.play(FadeOut(dots_group[i]), run_time=0.25)
        
        # text for model estimation 
        self.wait(7)
        text_estim = Tex(r"\begin{flushright}بهترین راه اینه که با توجه به نمونه\\یک برآورد مناسب از مدل واقعی داشته باشیم.\end{flushright}",
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text5, DOWN*2).shift(RIGHT)
        self.play(FadeIn(text_estim))

        self.wait(6)
        # text for ols

        text_ols = Tex(r"\begin{flushright}یک راه مناسب، پیدا کردن مدلیه که\\کمترین توان دوم خطای ممکن رو داره.\end{flushright}",
            font_size=font_size_matrices, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_estim, DOWN*1.5).align_to(text_estim, RIGHT)
        self.play(FadeIn(text_ols))

        self.wait(17)
        self.clear()
        self.wait(3)

        # text for different types of models
        text_mod_list = Tex(r"\item رگرسیون خطی\\\item رگرسیون چندجمله‌ای\\\vdots", 
            font_size=font_size_matrices, color='#FFFFFF', tex_template = TexTemplateLibrary.persian, tex_environment='itemize').shift(RIGHT*4).shift(UP*2)
        self.play(Write(text_mod_list), run_time=5)
        self.wait(10)
        elipse1 = Ellipse(width=3, height=1, color=YELLOW_D).shift(RIGHT*4.2).shift(UP*2.9)
        self.play(Create(elipse1), run_time=2)

        # add the axes again
        axes = Axes(x_range=[-1,10], y_range=[-1,10], x_length=5, y_length=5).shift(LEFT*3)
        # Adding the data points
        self.wait(7)
        self.play(Create(axes), run_time=2)
        self.wait(1)

        # add the dots again for linear vs non-linear
        # Adding dots to the data
        np.random.seed(1)
        points_x = np.random.uniform(1, 8, 20)
        f = lambda x: 0.75*x + 1
        np.random.seed(2)
        points_y = f(points_x) + np.random.normal(0, 0.5, 20)

        a = np.column_stack((points_x, points_y))
        dots_group2 = VGroup()
        dots_group2.add(*[Dot(axes.c2p(x,y)) for x, y in a])

        self.add(dots_group2.set_fill('#FCA311', opacity=0.75))
        self.play(Create(dots_group2), lag_ratio = 1)
        # Creating the regression linear line again
        func = axes.plot(lambda x: 0.75*x + 1, x_range=[0.5, 9])
        self.add(func.set_color('#AE2012'))
        self.play(Create(func))

        self.wait(2)
        # Transforming into non-linear data points
        f2 = lambda x: 1.5*(np.sin(x)) + 1
        np.random.seed(2)
        points_y = f2(points_x) + np.random.normal(0, 0.5, size=20)
        b = np.column_stack((points_x, points_y))
        dots_group3 = VGroup()
        dots_group3.add(*[Dot(axes.c2p(x,y)) for x, y in b]).set_color('#FCA311').set_opacity(0.75)

        self.play(ReplacementTransform(dots_group2, target_mobject=dots_group3), run_time=1.5)
        self.wait(5)
        self.play(FadeOut(dots_group3), FadeOut(dots_group2), FadeOut(func), FadeOut(axes), FadeOut(elipse1), FadeOut(text_mod_list))
        self.clear()
        #To be continued
        text_continue = Tex("ادامه دارد...",font_size=52, color='#FFFFFF', tex_template = TexTemplateLibrary.persian)
        self.play(Write(text_continue),reverse=True)
        self.wait(2)
        self.play(Unwrite(text_continue))
        self.wait(2)
    
        # last video (Previously)
        self.clear()
        
        #---------------------------------------------------------------
        #----------------- Video Two -----------------------------------
        #---------------------------------------------------------------
        text_pre_1 = Tex(r'در قسمت قبل به اینجا رسیدیم که چطور می‌تونیم',
            font_size=50, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).shift(RIGHT*2).shift(UP*5).to_edge(RIGHT, buff=1.5)
        text_pre_2 = Tex(r'خودمون رو محدود به فضای مدلهای خطی کنیم.',
            font_size=50, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_pre_1, DOWN).align_to(text_pre_1, RIGHT)

        self.play(Write(text_pre_1), reverse = True)
        self.play(Write(text_pre_2), reverse = True)
        self.wait(3)

        # This video
        text_this_vid_1 = Tex(r'در این قسمت وارد جزئیات رگرسیون خطی',
            font_size=50, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_pre_2, DOWN*2).align_to(text_pre_2, RIGHT)
        text_this_vid_2 = Tex(r'و کمترین توان دوم خطا میشیم.',
            font_size=50, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_this_vid_1, DOWN).align_to(text_this_vid_1, RIGHT)

        self.play(Write(text_this_vid_1), reverse=True)
        self.play(Write(text_this_vid_2), reverse=True)
        self.wait(3.5)

        # transforming sinus to linear data points
        np.random.seed(2)
        points_y = f(points_x) + np.random.normal(0, 1, size=20)
        b = np.column_stack((points_x, points_y))
        dots_group4 = VGroup()
        dots_group4.add(*[Dot(axes.c2p(x,y)) for x, y in b]).set_color('#FCA311').set_opacity(0.75)

        axes.scale(1.3).shift(DOWN*1.5)
        dots_group4.scale(1.3).shift(DOWN*1.5)
        self.play(FadeIn(axes, dots_group4))
        self.wait(4)

        # linear model general case
        model_1d = MathTex(r'y = \beta_0 + \beta_1 \times X', font_size=font_size_math).next_to(axes,DOWN).align_to(axes, LEFT).shift(RIGHT*1.5)
        self.play(Write(model_1d))
        self.wait(2)

        func_set = lambda y,z: axes.plot(lambda x: x*z + y, x_range=[0.5, 7])
        func_group = VGroup()

        np.random.seed(3)
        y_samples = np.random.uniform(-1.5, 1.5, 5)
        np.random.seed(4)
        z_samples = np.random.uniform(0.5, 1.5, 5)
        for i in range(len(y_samples)):
            func_group.add(func_set(y_samples[i], z_samples[i]))
        
        func.shift(DOWN*1.5)
        func_group.set_color_by_gradient(RED, BLUE)
        self.play(Create(func_group), run_time=1.25)
        self.play(Create(func))
        self.wait(6)

        self.play(FadeOut(func_group))
        self.wait(8)

        # distance between a point and a plot function and a perpendicular dashed line between the point and the function
        def min_distance_dot(dot, func, x_min=0.5, x_max=9):
            point = dot.get_center()
            start = axes.c2p(x_min, func(x_min))
            end = axes.c2p(x_max, func(x_max))

            line = Line(start=start, end=end)

            point_project = line.get_projection(point)
            p2p_dist = dist(point[0:2], point_project[0:2])
            dot_project = Dot(point_project)

            return p2p_dist, dot_project

        perpend_dots_group = VGroup()
        perpend_lines_group = VGroup()
        for dot in dots_group4:
            _, dot_perpend = min_distance_dot(dot, f)
            self.play(Create(dot_perpend), run_time = 0.1)
            dline = DashedLine(dot, dot_perpend)
            perpend_dots_group.add(dot_perpend)
            perpend_lines_group.add(dline)
            self.play(Create(dline), run_time=0.1)

        self.wait(1)

        # Moving aside one dot
        np.random.seed(5)
        random_index = np.random.randint(low=0, high=len(dots_group4) - 1)
        random_dot = dots_group4[random_index]
        self.play(random_dot.animate.shift(RIGHT*7).shift(UP*2))
        self.wait(1)

        # observation i: y_i = beta0 + beta1*x_i
        text_obs_i = MathTex(r'y_i, \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i', font_size=font_size_math).next_to(random_dot, DOWN)
        self.play(Write(text_obs_i), run_time=2)
        self.wait(5)

        # observation i: error
        text_distance_i = MathTex(r'e_i = y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i)', font_size=font_size_math).next_to(text_obs_i,DOWN)
        self.play(Write(text_distance_i), run_time = 2)
        self.wait(10)

        # all observations: errors
        text_errors_all = MathTex(r'\sum_{i=1}^{n} e_i = \sum_{i=1}^{n} y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i)',
            font_size=font_size_math).next_to(text_distance_i, DOWN).align_to(text_distance_i, RIGHT)
        self.play(Write(text_errors_all), run_time=2)
        self.wait(3)

        # Non-negativity
        # brace between points
        p1 = [1.8,-2.2,0]
        # p1 = text_errors_all[0][13].get_left()
        p2 = [6, -2.2, 0]
        # p2 = text_errors_all[0][26].get_left()
        brace_sum = BraceBetweenPoints(p1,p2)
        self.play(FadeIn(brace_sum), run_time = 2)
        self.wait(10)
        text_positive = MathTex(r'> 0', font_size = 40).move_to(brace_sum.get_center()).shift(DOWN*0.5)
        self.play(Write(text_positive))
        self.wait(2)
        brace_pos = VGroup()
        brace_pos.add(brace_sum, text_positive)

        # absolute value
        absolute_lines = MathTex(r'\left| \hspace{62 pt} \right|', font_size=font_size_math+5).set_color(YELLOW).move_to(text_errors_all.get_center()).shift(RIGHT*1.5)
        self.play(Write(absolute_lines))
        self.wait(1)

        # Squared Value
        Squared = MathTex(r'(\hspace{62 pt})^2', font_size=font_size_math+5).set_color(YELLOW).move_to(text_errors_all.get_center()).shift(RIGHT*1.7).shift(UP*0.05)
        self.play(Transform(absolute_lines, Squared))
        self.wait(8)

        # minimize sum
        # Rectangle over sum
        rect_sum = SurroundingRectangle(text_errors_all[0][8:27], color=BLUE_D, buff=MED_SMALL_BUFF*1.15).shift(RIGHT*0.2)
        text_minimize = Text('minimize', font_size=35, color='#FFFFFF', font='Lato').next_to(rect_sum, DOWN)
        self.play(Create(rect_sum), Transform(brace_pos, text_minimize))
        self.wait(2)

        # minimization
        mini_group = Group()
        mini_group.add(rect_sum, text_minimize, brace_pos)
        mini_group.add(Squared, absolute_lines)
        mini_group.add(text_errors_all[0][8:28])

        all_objs = Group()
        all_objs.add(text_errors_all[0][0:8], text_distance_i, text_obs_i, model_1d, 
            axes, func, perpend_dots_group, perpend_lines_group, random_dot, dots_group4,
            text_pre_1, text_pre_2, text_this_vid_1, text_this_vid_2)
        

        self.play(FadeOut(all_objs))
        self.play(mini_group.animate.shift(LEFT*7).shift(UP*6))
    

        # beta_0 derivative
        text_derivative_1 = Tex(r'اکنون باید پارامترهایی که این',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(mini_group, RIGHT*4).shift(UP*0.7)
        text_derivative_2 = Tex(r'عبارت را کمینه می‌کنند، بیابیم.',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_derivative_1, DOWN).align_to(text_derivative_1, RIGHT)
        text_dbeta0 = MathTex(r'\frac{\partial}{\partial\beta_0} \vspace{2 pt}', font_size=font_size_math).next_to(mini_group,DOWN*2).align_to(mini_group, LEFT).shift(RIGHT*0.5)
        text_dbeta1 = MathTex(r'\frac{\partial}{\partial\beta_1} \vspace{2 pt}', font_size=font_size_math).next_to(text_dbeta0,DOWN)
        rect_small_0 = Rectangle(height=0.5, width=0.75).next_to(text_dbeta0, RIGHT) 
        rect_small_1 = Rectangle(height=0.5, width=0.75).next_to(text_dbeta1, RIGHT) 
        rect_big0 = rect_sum.copy()
        rect_big1 = rect_sum.copy()

        derivative_group = VGroup()
        derivative_group.add(text_dbeta0, text_dbeta1)
        self.play(Write(text_derivative_1), reverse=True, run_time=0.5)
        self.play(Write(text_derivative_2), reverse=True, run_time=0.5)
        self.wait(1)      
        self.play(Write(derivative_group), Transform(rect_big0, rect_small_0), Transform(rect_big1, rect_small_1), lag_ratio = 0)
        # self.wait(2.5)

        # derivative equals 0
        text_zero_0 = MathTex(' = 0', font_size=40).next_to(rect_big0, RIGHT)
        text_zero_1 = MathTex(' = 0', font_size=40).next_to(rect_big1, RIGHT)
        text_zero = Tex('برای هر پارامتر مشتق باید برابر',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_zero_0, RIGHT*2).align_to(text_derivative_2, RIGHT)
        
        text_zero_2 = Tex('با صفر باشد.',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_zero, DOWN).align_to(text_derivative_2, RIGHT)
        

        self.play(Write(text_zero), reverse=True)
        self.play(Write(text_zero_2), reverse=True)
        self.play(Write(text_zero_0), Write(text_zero_1))
        self.wait(2.5)

        # multiple variables
        text_multiple_vars = Tex('اگر بیشتر از یک متغیر مستقل داشته باشیم',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_zero_2, DOWN*4).align_to(text_zero, RIGHT)
        text_multiple_vars_2 = Tex('چه اتفاقی می‌افتد؟ مثلا 2، 10، 100، یا 1000.', 
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_multiple_vars, DOWN).align_to(text_zero, RIGHT)
        self.play(Write(text_multiple_vars), reverse=True)
        self.play(Write(text_multiple_vars_2), reverse=True)

        self.wait(11)

        text_linalg = Tex('در اینجا باید از خواص جبر خطی و ماتریس‌ها',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_multiple_vars_2, DOWN*4).align_to(text_multiple_vars_2, RIGHT)
        text_linalg_2 = Tex('استفاده کنیم.',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(text_linalg, DOWN).align_to(text_linalg, RIGHT)

        self.play(Write(text_linalg), reverse = True)
        self.play(Write(text_linalg_2), reverse = True)
        self.wait(2)

        self.clear()

        # multi-observation equations
        text_obs_all = MathTex(r'''y_1 &= \beta_0 + \beta_1 x_{11} + \cdots + \beta_m x_{1m}\\
            y_2 &= \beta_0 + \beta_1 x_{21} + \cdots + \beta_m x_{2m}\\
            \vdots & \\
            y_n &= \beta_0 + \beta_1 x_{n1} + \cdots + \beta_m x_{nm}''', font_size=font_size_matrices).shift(LEFT*3).shift(UP*4)

        self.play(Write(text_obs_all))
        self.wait(2)

        #matrices
        def add_brackets(mobj):
            bracket_pair = Tex("\\big[", "\\big]")
            bracket_pair.scale(2)
            bracket_pair.stretch_to_fit_height(
                mobj.height + 2 * 0.1
            )
            l_bracket, r_bracket = bracket_pair.split()
            l_bracket.next_to(mobj, LEFT, .2)
            r_bracket.next_to(mobj, RIGHT, .2)
            return VGroup(l_bracket, mobj, r_bracket)

        # y, X, and beta as matrices
        y_mat = MathTex(r'''
            & y_{1}\\
            & y_{2}\\
            & \vdots\\
            & y_{n}
        ''', font_size=font_size_matrices)
        y_mat = add_brackets(y_mat).next_to(text_obs_all, DOWN*2).align_to(text_obs_all, LEFT)
       
        equals = MathTex(r' = ', font_size=32).next_to(y_mat, RIGHT).shift(LEFT*0.1)

        self.play(Write(y_mat))
        self.play(Write(equals))

        final_mat = MathTex(r'''
            & \beta_{0} + \beta_{1} x_{11} + \cdots + \beta_{m} x_{1m}\\
            & \beta_{0} + \beta_{1} x_{21} + \cdots + \beta_{m} x_{2m}\\
            & \vdots\\
            & \beta_{0} + \beta_{1} x_{n1} + \cdots + \beta_{m} x_{nm}\\
        ''', font_size=font_size_matrices)

        final_mat_bracket = add_brackets(final_mat).next_to(equals, RIGHT)
        self.play(Write(final_mat_bracket))

        equals_2 = MathTex(r' = ', font_size=32).next_to(final_mat_bracket, DOWN*7).align_to(equals, LEFT)


        x_mat = MathTex(r'''
            & 1 \hspace{10 pt} x_{11} \hspace{10 pt} x_{12} \hspace{10 pt} \cdots \hspace{10 pt}  x_{1m}\\
            & 1 \hspace{10 pt} x_{21} \hspace{10 pt} x_{22} \hspace{10 pt} \cdots \hspace{10 pt} x_{2m}\\
            & \vdots \hspace{20 pt} \vdots \hspace{20 pt} \vdots \hspace{15 pt} \cdots \hspace{20 pt}  \vdots\\
            & 1 \hspace{10 pt} x_{n1} \hspace{9 pt} x_{n2} \hspace{9 pt} \cdots \hspace{10 pt} x_{nm}
        ''', font_size=font_size_matrices)
        x_mat = add_brackets(x_mat).next_to(equals_2, RIGHT)

        beta_mat = MathTex(r'''
            & \beta_{0}\\
            & \beta_{1}\\
            & \vdots\\
            & \beta_{m}
        ''', font_size=font_size_matrices)
        beta_mat = add_brackets(beta_mat).next_to(x_mat, RIGHT).shift(LEFT*0.1)

        self.wait(2)
        self.play(Write(equals_2), Write(x_mat))
        self.play(Write(beta_mat))
        self.wait(2)

        
        self.wait(5)

        # Notation instead of a matrix
        yxbeta = VGroup()
        y = MathTex(r'y =').next_to(y_mat, DOWN*16).align_to(y_mat[1], LEFT)
        text_then = MathTex(r'\Rightarrow').next_to(y, LEFT)
        X = MathTex(r'X').next_to(y, RIGHT).shift(UP*0.05)
        beta = MathTex(r'\beta').next_to(X, RIGHT*0.5).shift(DOWN*0.05)
        yxbeta.add(y, X, beta)
        yxbeta_surrect = SurroundingRectangle(yxbeta, BLUE, buff=MED_SMALL_BUFF)
        yxbeta.add(yxbeta_surrect)
        self.play(Write(text_then))
        self.play(Write(yxbeta))
        self.wait(2)
        
        # Clear all objs except for the yxbeta and shift yxbeta to up right
        all_objs_2 = VGroup()
        all_objs_2.add(equals_2, final_mat_bracket, beta_mat, x_mat, equals, y_mat, text_obs_all, text_then)

        self.play(FadeOut(all_objs_2),yxbeta.animate.shift(UP*9).shift(RIGHT*10))
        self.wait(1)

        self.play(FadeIn(mini_group))
        self.wait(8)

        # matrix form sum of squared errors
        sse_mat = MathTex(r'(y - X\beta)^{\prime}(y - X\beta)', font_size=font_size_text).next_to(mini_group, DOWN*2).align_to(mini_group[5], LEFT)
        self.play(Write(sse_mat))
        self.wait(3.5)

        # open up the matrix form
        sse_mat_open = MathTex(r' = y^{\prime}y - y^{\prime}X\beta - \beta^{\prime}X^{\prime}y + \beta^{\prime}X^{\prime}X\beta', font_size=font_size_text).next_to(sse_mat, RIGHT)
        self.play(Write(sse_mat_open))
        self.wait(5)

        # beta derivation
        beta_derivative_text_1 = Tex('در اینجا باید مشتق نسبت به بردار پارامترها را',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(sse_mat, DOWN*2).align_to(yxbeta, RIGHT)
        beta_derivative_text_2 = Tex('به جای هر یک از پارامترها بیابیم.',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(beta_derivative_text_1, DOWN).align_to(beta_derivative_text_1, RIGHT)

        self.play(Write(beta_derivative_text_1), reverse=True)
        self.play(Write(beta_derivative_text_2), reverse=True)
        self.wait(2)

        # derivative of vectors
        dbeta_note_1 = Tex('برای انجام این کار باید دو مورد از خواص', 
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(beta_derivative_text_2, DOWN*3).align_to(beta_derivative_text_2, RIGHT)
        dbeta_note_2 = Tex('مشتق بردارها را به خاطر داشته باشیم:',
            font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian).next_to(dbeta_note_1, DOWN).align_to(beta_derivative_text_2, RIGHT)
        self.play(Write(dbeta_note_1), reverse=True)
        self.play(Write(dbeta_note_2), reverse=True)
        self.wait(1)
        # properties vgroup
        prop1 = MathTex(r'\frac{\partial}{\partial a} a^{\prime}b = \frac{\partial}{\partial a} b^{\prime}a = b',
            font_size=font_size_math).next_to(dbeta_note_2, LEFT*2).align_to(mini_group[5], LEFT).shift(DOWN*1.5)
        prop2 = MathTex(r'\frac{\partial}{\partial a} a^{\prime}Ba = 2Ba', font_size=font_size_math).next_to(prop1, DOWN).align_to(prop1, LEFT)
        propg = VGroup(prop1, prop2)
        self.play(Write(propg))
        self.wait()

        surrect = SurroundingRectangle(propg, color=BLUE, buff=MED_SMALL_BUFF)
        self.play(Create(surrect))
        self.wait()

        # FadeOut Scene except surrect, propg, and sse_mat_open after the equal sign
        dbeta_group = VGroup(sse_mat_open[0][1:22])
        all_objs_3 = VGroup(dbeta_note_1, dbeta_note_2, beta_derivative_text_1, beta_derivative_text_2, sse_mat_open[0][0:1], sse_mat)
        surrect_prop_group = VGroup(surrect, propg)
        self.play(FadeOut(all_objs_3, mini_group, yxbeta), 
            dbeta_group.animate.shift(UP*3).shift(LEFT*5), 
            surrect_prop_group.animate.shift(UP*8.2).shift(RIGHT*8).scale(0.7))
        self.wait()

        dbeta_group_copy = dbeta_group.copy()
        dbeta_derivative = MathTex(r'\xrightarrow{\frac{\partial}{\partial \beta}} 0 - X^{\prime}y - X^{\prime}y + 2X^{\prime}X\beta',
            font_size=font_size_math-3).next_to(dbeta_group_copy, DOWN*2).align_to(dbeta_group_copy, LEFT)
        dbeta_zero = MathTex(r' = 0', font_size=font_size_math).next_to(dbeta_derivative, RIGHT).shift(DOWN*0.2 )

        self.play(Transform(dbeta_group_copy, dbeta_derivative))
        self.wait(1)
        self.play(Write(dbeta_zero))
        self.wait(2)

        p1_1 = [-4.1,3,0]
        p1_2 = [-1.4, 3, 0]
        brace_prop1 = BraceBetweenPoints(p1_1,p1_2, color=WHITE)

        self.play(FadeIn(brace_prop1), prop1.animate.next_to(brace_prop1, DOWN).set_color(WHITE), run_time = 2)
        self.wait(3)
        self.play(FadeOut(brace_prop1), prop1.animate.next_to(prop2,UP).align_to(prop2, LEFT).set_color(WHITE), run_time = 2)
        self.wait(2)
        
        p2_1 = [-0.9, 3, 0]
        p2_2 = [0.8, 3, 0]
        brace_prop2 = BraceBetweenPoints(p2_1, p2_2, color=WHITE)

        self.play(FadeIn(brace_prop2), prop2.animate.next_to(brace_prop2, DOWN).set_color(WHITE), run_time = 2)
        self.wait(3)
        self.play(FadeOut(brace_prop2), prop2.animate.next_to(prop1,DOWN).align_to(prop1, LEFT).set_color(WHITE), run_time = 2)
        self.wait(6)

        # simplifying the derivation equation
        d_eq_simp = MathTex(r'\Rightarrow 2X^{\prime}X\beta = 2X^{\prime}y', font_size=font_size_math).next_to(dbeta_derivative, DOWN*4).align_to(dbeta_derivative, LEFT)
        self.play(Write(d_eq_simp))
        self.wait(2)

        # By multiplying (x'x)^-1 on the left of both sides we will have the final result
        self.play(FadeOut(d_eq_simp[0][1]), FadeOut(d_eq_simp[0][7]))
        self.wait(10)

        d_eq_simp_left = d_eq_simp[0][2:7]
        d_eq_simp_right = d_eq_simp[0][8:12]

        d_multiple = MathTex(r'(X^{\prime}X)^{-1}', font_size=font_size_math).move_to(d_eq_simp.get_center()).align_to(d_eq_simp_left, LEFT).shift(RIGHT*1.2)
        d_multiple_2 = d_multiple.copy().move_to(d_eq_simp_right.get_center()).align_to(d_eq_simp_right, LEFT).shift(RIGHT*2.85)

        right_arrow = MathTex(r'\xrightarrow{(X^{\prime}X)^{-1}*}', font_size=font_size_math-10).move_to(d_eq_simp.get_center()).align_to(d_eq_simp, LEFT)

        self.play(d_eq_simp_left.animate.shift(RIGHT*3.25), d_eq_simp_right.animate.shift(RIGHT*4.9), FadeIn(d_multiple), FadeIn(d_multiple_2), Transform(d_eq_simp[0][0], right_arrow))
        self.wait(10)

        brace_ind = BraceBetweenPoints(d_multiple.get_left(), d_eq_simp_left[2].get_right(), color=BLUE).shift(DOWN*0.15)
        self.play(FadeIn(brace_ind))
        self.wait(1)

        indicator_mat = MathTex(r'\mathbb{I}', font_size=font_size_math).move_to(brace_ind.get_center()).shift(DOWN*0.5)
        self.play(Write(indicator_mat))
        self.wait(6)

        # final equation
        fin_eq_beta = MathTex(r'\Longrightarrow \hat{\beta} = (X^{\prime}X)^{-1}X^{\prime}y', font_size=font_size_math).next_to(right_arrow, DOWN*8).align_to(right_arrow, LEFT)
        
        self.play(Write(fin_eq_beta))
        self.wait(2)

        surrect_fin = SurroundingRectangle(fin_eq_beta[0][2:15], color=BLUE, buff=MED_SMALL_BUFF)
        self.play(Create(surrect_fin))
        self.wait(2)

        fin_group = VGroup(surrect_fin, fin_eq_beta[0][2:15])
        rem_group = VGroup(indicator_mat, brace_ind, right_arrow, d_multiple, d_multiple_2, 
            d_eq_simp_left, d_eq_simp_right, dbeta_group, dbeta_group_copy, dbeta_derivative, 
            dbeta_zero, fin_eq_beta[0][0:2], propg, surrect, d_eq_simp[0][0])

        self.play(FadeOut(rem_group), fin_group.animate.move_to(ORIGIN).scale(2))
        self.wait(2)
        channel_name = Text('mlwithsaeid', font='Lato', font_size=70)
        self.play(Transform(fin_group[1], channel_name))
        self.wait(15)
        
