from audioop import reverse
from math import pi
from tkinter import CENTER, Image, font
from turtle import width
from manim import *
import numpy as np

config.max_files_cached = 3000

font_title = 'Lalezar'
font_fa = 'Vazirmatn'

class bt(Scene):
    def construct(self):
        self.camera.background_color = '#14213D'
        font_size_text = 25
        font_size_title = 28
        font_size_math = 32

        def Tex_fa(text, font_size_text=font_size_text):
            return Tex(text, font_size=font_size_text, color='#FFFFFF', tex_template=TexTemplateLibrary.persian)

        # function to select all but one mobject

        def select_mobjs(*mobjs):
            """
            Select all mobjects in the scene except the one mobject given in the input.
            """
            all_objs = VGroup()
            for obj in self.mobjects:
                if ((isinstance(obj, VMobject) == True) and obj not in mobjs):
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

        text_1 = Text('توی این ویدیو می‌خوام در مورد قضیه‌ی بیز صحبت کنم که یکی از مباحث مهم آمار و یادگیری ماشینه.', 
                      font=font_title,
                      font_size=font_size_title
                      ).to_edge(RIGHT, buff=1).shift(UP*2)
        self.play(Write(text_1), reverse=True, run_time = 4)


        text_bayes_l = MathTex(r'P(H | E) = \frac{P(H) \cdot P(E | H)}{P(H) \cdot P(E | H) + P(H^c) \cdot P(E | H^c)}',
                               font_size=font_size_math).next_to(text_1, DOWN*3).to_edge(LEFT, buff=1)
        self.play(Write(text_bayes_l))

        self.wait()

        text_3 = Text('قضیه‌ی بیز به طور خلاصه به ما میگه که هر اطلاعات جدیدی بدست آوردیم، نباید به تنهایی برای', font=font_title,
                      font_size=font_size_title).next_to(text_bayes_l, DOWN*3).align_to(text_1, RIGHT)
        text_4 = Text(
            'استنتاج استفاده بشه. بلکه باید برای بروزرسانی باورهای قبلی به کار گرفته بشه.',
            font = font_title, 
            font_size=font_size_title
        ).next_to(text_3, DOWN).align_to(text_1, RIGHT)


        self.play(Write(text_3), reverse=True, run_time = 4)
        self.play(Write(text_4), reverse=True, run_time = 3)
        self.wait(5)

        self.play(FadeOut(select_mobjs()))

        smiley = SVGMobject('E:/Social Media/smiley-1635449.svg').scale(0.5)
        steve = Text('Steve', font='Lato', font_size=font_size_text).next_to(smiley, UP)
        self.play(FadeIn(smiley, steve))
        self.wait()


        saddy = SVGMobject('E:/Social Media/smiley-1635454.svg').scale(0.5)
        self.play(ReplacementTransform(smiley, saddy))

        steve_vg = VGroup(saddy, steve)

        doctor = SVGMobject('E:/Social Media/doctor-2027615.svg').shift(UP*2).to_edge(RIGHT, buff=4)
        self.play(steve_vg.animate.shift(UP*2).to_edge(RIGHT, buff=2), FadeIn(doctor))

        lab_exp = ImageMobject('E:/Social Media/lab-3498584.jpg').scale(0.15).shift(RIGHT*9).shift(UP*1.5)
        self.play(lab_exp.animate.shift(LEFT*12))

        positive = Text('positive', font='Caveat', font_size=font_size_text, color='#9d0208').next_to(lab_exp, RIGHT).shift(UP).shift(LEFT*1.2)
        positive_rect = SurroundingRectangle(positive, color='#9d0208', buff=SMALL_BUFF)
        positive_vg = VGroup(positive, positive_rect).rotate(angle=-(1/5)*pi).scale(1.5)
        self.play(FadeIn(positive_vg))
        self.wait(1.5)

        accuracy_test = Tex_fa('1. آزمایش 99\% تست‌های منفی و مثبت رو درست تشخیص می‌ده.', font_size_text=font_size_text+8).next_to(lab_exp, DOWN).align_to(text_1, RIGHT)
        self.wait()
        false_positive = Tex_fa('2. 1\% احتمال تشخیص مثبت به اشتباه وجود داره.', font_size_text=font_size_text+8).next_to(accuracy_test, DOWN).align_to(text_1, RIGHT)
        self.wait()
        population = Tex_fa('3. از هر 1000 نفر 1 نفر این بیماری رو داره.', font_size_text=font_size_text+8).next_to(false_positive, DOWN).align_to(text_1, RIGHT)
        self.wait(3)

        self.play(Write(accuracy_test), reverse=True)
        self.play(Write(false_positive), reverse=True)
        self.play(Write(population), reverse=True)
        self.wait()

        self.play(FadeOut(select_mobjs()), FadeOut(lab_exp))

        think = ImageMobject('E:/Social Media/think.jpg').shift(UP*1.5).scale(0.1).to_edge(LEFT, buff=1)
        steve.next_to(think, UP)
        self.play(FadeIn(think, steve))

        self.wait(8)

        hypothesis_1 = Text(':H', font='Caveat', font_size=font_size_text).next_to(text_1, RIGHT).align_to(text_1, RIGHT)
        hypothesis_2 = Text(
            'من (استیو) واقعا مریض باشم.',
            font = font_fa, 
            font_size = font_size_text
        ).next_to(hypothesis_1, LEFT)

        evidence_1 = Text(':E', font='Caveat', font_size=font_size_text).next_to(hypothesis_1, DOWN*2).align_to(text_1, RIGHT)
        evidence_2 = Text(
            'جواب آزمایشم مثبت بشه.',
            font = font_fa,
            font_size = font_size_text
        ).next_to(evidence_1, LEFT).align_to(hypothesis_2, RIGHT)

        self.play(Write(hypothesis_1), reverse=True)
        self.play(Write(hypothesis_2), reverse=True)

        self.wait()

        self.play(Write(evidence_1), reverse=True)
        self.play(Write(evidence_2), reverse=True)
        self.wait()

        text_bayes_l.next_to(think, DOWN).align_to(think, LEFT)
        self.play(Write(text_bayes_l))
        self.wait(24)
        rep_1 = MathTex('0.001 \\cdot', font_size=font_size_math).move_to(text_bayes_l[0][7:11].get_left()).shift(RIGHT)
        rep_2 = MathTex('0.99', font_size=font_size_math).move_to(text_bayes_l[0][11:18].get_left()).shift(RIGHT)
        rep_3 = MathTex('0.001 \\cdot', font_size=font_size_math).move_to(text_bayes_l[0][19:23].get_left()).shift(RIGHT)
        rep_4 = MathTex('0.99', font_size=font_size_math).move_to(text_bayes_l[0][23:30].get_left()).shift(RIGHT)
        rep_5 = MathTex('+ \, 0.999 \cdot', font_size=font_size_math).move_to(text_bayes_l[0][30:36].get_left()).shift(RIGHT)
        rep_6 = MathTex('0.01', font_size=font_size_math).move_to(text_bayes_l[0][36:44].get_left()).shift(RIGHT)
        self.play(
            Transform(text_bayes_l[0][7:11], rep_1),
            Transform(text_bayes_l[0][11:18], rep_2),
            Transform(text_bayes_l[0][19:23], rep_3),
            Transform(text_bayes_l[0][23:30], rep_4),
            Transform(text_bayes_l[0][30:36], rep_5),
            Transform(text_bayes_l[0][36:44], rep_6),
        )
        self.wait(2)

        all_objs = select_mobjs(text_bayes_l[0][0:6], hypothesis_1, hypothesis_2, evidence_1, evidence_2)
        rep_f =  MathTex('0.09', font_size=font_size_math+25).move_to(text_bayes_l[0][6].get_right()).shift(RIGHT)
        text_bayes_s = text_bayes_l[0][0:7].copy()
        self.add(text_bayes_s)

        self.play(
            ReplacementTransform(all_objs, rep_f),
        )
        rep_f2 = MathTex(r'9\%', font_size=font_size_math+25).move_to(text_bayes_l[0][6].get_right()).shift(LEFT).shift(UP*0.01)
        self.play(
            ReplacementTransform(rep_f, rep_f2)
        )
        self.wait(16)
        second_experiment = MathTex(
            r'\frac{0.09 \: \cdot \: 0.99}{0.09 \: \cdot \: 0.99 + 0.91 \: \cdot \: 0.01}',
            font_size = font_size_math+2,
        ).next_to(text_bayes_s, RIGHT)
        
        self.play(
            ReplacementTransform(rep_f2, second_experiment),
        )
        self.wait(10)
        second_experiment_2 = MathTex(r'91\%', font_size=font_size_math+25).move_to(text_bayes_l[0][6].get_right()).shift(LEFT*0.8).shift(UP*0.01)
        self.play(
            ReplacementTransform(second_experiment, second_experiment_2)
        )
        self.wait(7.5)
        self.play(FadeOut(select_mobjs()), FadeOut(think), FadeOut(steve))

        t_bayes = ImageMobject('E:/Social Media/Thomas-Bayes.jpg').scale(0.3).shift(RIGHT*7).shift(UP*2)
        self.play(t_bayes.animate.to_edge(LEFT, buff=1), rate_func=smooth)

        text_7 = Text(
            'اما توماس بیز چطور به این معادله رسید؟',
            font = font_title,
            font_size = font_size_title,
        ).next_to(t_bayes, RIGHT).align_to(text_1, RIGHT)

        self.play(Write(text_7), reverse=True)

        text_8 = Text(
            'سمت چپ معادله طبق تعریف کلموگروف برابره با:',
            font = font_fa,
            font_size = font_size_text,
        ).next_to(text_7, DOWN*2).align_to(text_1, RIGHT)

        kolmogorov = MathTex(
            r'P(A | B) = \frac{P(A \cap B)}{P(B)}',
            font_size = font_size_math,
        ).next_to(text_8, DOWN).to_edge(LEFT, buff=1)

        self.play(Write(text_8), reverse=True)
        self.play(Write(kolmogorov))
        
        self.wait(2)

        text_9 = Tex_fa(
            r'همین عبارت رو میشه برای $P(B | A)$ هم نوشت:',
            font_size_text=font_size_math,
        ).next_to(kolmogorov, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_9), reverse=True)

        kolmogorov_2 = MathTex(
            r'P(B | A) = \frac{P(B \cap A)}{P(A)}',
            font_size = font_size_math,
        ).next_to(text_9, DOWN).align_to(kolmogorov, LEFT)

        self.play(Write(kolmogorov_2))

        intersect = MathTex(
            r'A \cap B',
            font_size = font_size_math,
        ).move_to(kolmogorov_2[0][9:12].get_center())
        self.wait(1)
        self.play(
            ReplacementTransform(kolmogorov_2[0][9:12], intersect)
        )
        self.wait()
        intersect_eq = MathTex(
            r'P(A \cap B) = P(B | A) \cdot P(A)',
            font_size = font_size_math,
        ).move_to(kolmogorov_2.get_center()).align_to(kolmogorov, LEFT)

        self.play(
            ReplacementTransform(kolmogorov_2, intersect_eq),
            FadeOut(intersect)
        )

        self.wait(3)
        text_10 = Text(
            'بنابراین خواهیم داشت:',
            font = font_fa,
            font_size = font_size_text,
        ).next_to(intersect_eq, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_10), reverse=True)

        rect_1 = SurroundingRectangle(kolmogorov, color=BLUE_D, buff=MED_SMALL_BUFF)
        rect_2 = SurroundingRectangle(intersect_eq, color=BLUE_D, buff=MED_LARGE_BUFF)

        self.play(Create(rect_1), Create(rect_2))
        self.wait()
        kolmogorov_3 = MathTex(
            r'P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)}',
            font_size = font_size_math,
        ).next_to(text_10, DOWN).align_to(kolmogorov, LEFT)

        self.play(Write(kolmogorov_3))

        rect_3 = SurroundingRectangle(kolmogorov_3[0][19:23], color=YELLOW, buff=MED_SMALL_BUFF)

        self.play(Create(rect_3))

        self.play(
            FadeOut(select_mobjs(kolmogorov_3)), 
            FadeOut(t_bayes),
            kolmogorov_3.animate.move_to(text_1.get_left()).shift(UP*0.5).align_to(kolmogorov, LEFT),
        )

        text_11 = Text(
            'این دیاگرام ون رو در نظر بگیرید:',
            font = font_fa,
            font_size = font_size_text,
        ).next_to(kolmogorov_3, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_11), reverse=True)

        venn_rect = Rectangle(color=BLACK, height=3, width=5).set_opacity(0.8).to_edge(LEFT, buff=1)
        self.play(FadeIn(venn_rect))

        venn_circ1 = Circle(radius=1, color=RED).move_to(venn_rect.get_center()).shift(LEFT*0.75).set_opacity(0.4)
        venn_circ2 = Circle(radius=1, color=BLUE).move_to(venn_rect.get_center()).shift(RIGHT*0.75).set_opacity(0.4)
        self.play(FadeIn(venn_circ1, venn_circ2))

        venn_a = Text('A', font='Caveat', font_size = font_size_text).move_to(venn_circ1.get_center()).shift(UL*1)
        venn_b = Text('B', font='Caveat', font_size = font_size_text).move_to(venn_circ2.get_center()).shift(UR*1)
        venn_s = Text('S', font='Caveat', font_size = font_size_text).move_to(venn_rect.get_center()).shift(DOWN*1).shift(RIGHT*2)

        self.play(Write(venn_a), Write(venn_b), Write(venn_s))
        self.wait()

        intersect_ab = Intersection(venn_circ1, venn_circ2, color=WHITE, fill_opacity=0.8)  
        intersect_ab.save_state()
        # self.play(intersect_ab.animate.move_to(ORIGIN))

        diff_ba = Difference(venn_circ2, venn_circ1, color=WHITE, fill_opacity=1) 
        # self.play(diff_ba.animate.next_to(intersect_ab))

        prob_b = MathTex(
            r'P(B) = P(B \cap A) + P(B \cap A^c)',
            font_size = font_size_math,
        ).next_to(venn_rect, RIGHT).to_edge(RIGHT, buff=3).shift(UP)

        self.play(Write(prob_b))
        rect_4 = SurroundingRectangle(prob_b[0][7:10], color=BLUE, buff=MED_SMALL_BUFF)
        self.play(
            FadeIn(rect_4),
            FadeIn(intersect_ab),
        )

        rect_5 = SurroundingRectangle(prob_b[0][14:18], color=BLUE, buff=MED_SMALL_BUFF)
        self.play(
            FadeOut(rect_4),
            FadeOut(intersect_ab),
            FadeIn(rect_5),
            FadeIn(diff_ba),
        )

        self.play(
            FadeOut(rect_5, diff_ba),
        )

        text_12 = Text(
            'از طرفی داشتیم:',
            font = font_fa,
            font_size = font_size_text,
        ).next_to(prob_b, DOWN).align_to(text_1, RIGHT)
        self.play(Write(text_12), reverse=True)

        intersect_eq.next_to(text_12, DOWN).align_to(prob_b, LEFT)

        self.play(Write(intersect_eq))

        text_13 = Text(
            'بنابراین خواهیم داشت:',
            font = font_fa,
            font_size = font_size_text,
        ).next_to(intersect_eq, DOWN).align_to(text_1, RIGHT)

        self.play(Write(text_13), reverse=True)

        prob_b_2 = MathTex(
            r'P(B) = P(B | A) \cdot P(A) + P(B | A^c) \cdot P(A^c)',
            font_size=font_size_math
        ).next_to(text_13, DOWN).align_to(prob_b, LEFT)

        self.play(Write(prob_b_2))

        self.wait(3)

        final_eq = MathTex(
            r'\frac{P(B | A) \cdot P(A)}{P(B | A) \cdot P(A) + P(B | A^c) \cdot P(A^c)}',
            font_size = font_size_math,
        ).next_to(kolmogorov_3[0][6], RIGHT)

        self.play(
            FadeOut(select_mobjs(final_eq, kolmogorov_3)),
            FadeOut(venn_circ1, venn_circ2),
            ReplacementTransform(kolmogorov_3[0][7:23], final_eq)
        )

        brand = Text('mlwithsaeid', font='Caveat', font_size = 100)
        final_vg = VGroup(final_eq, kolmogorov_3)

        self.wait()

        final_rect = SurroundingRectangle(brand, color = BLUE, buff = MED_LARGE_BUFF)
        self.play(
            final_vg.animate.move_to(ORIGIN),
            ReplacementTransform(final_vg, brand), 
            Create(final_rect)
        )
        self.wait(3)