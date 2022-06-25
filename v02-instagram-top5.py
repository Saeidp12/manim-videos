from audioop import reverse
from manim import *
import numpy as np

config.max_files_cached = 3000

class Story1(MovingCameraScene):
    def construct(self):
        self.camera.background_color = '#14213D'
        self.camera.frame.save_state()
        font_size_text = 15
        font_size_title = 50
        edge_buff = 2

        def tex_fa(text):
            return Tex(text, font_size=font_size_text, color='#FFFFFF', tex_template = TexTemplateLibrary.persian)
        
        text_python = Text('Python', font_size=font_size_title, font='Lato', color='#FFFFFF')
        rect_python = SurroundingRectangle(text_python, buff=MED_LARGE_BUFF)
        python = VGroup(text_python, rect_python).to_edge(RIGHT, buff=edge_buff).shift(UP*6)
        
        text_r = Text('R', font_size=font_size_title, font='Lato', color='#FFFFFF')
        rect_r = SurroundingRectangle(text_r, buff=MED_LARGE_BUFF)
        r = VGroup(text_r, rect_r).to_edge(LEFT, buff=edge_buff).shift(UP*3)

        text_java = Text('Java', font_size=font_size_title, font='Lato', color='#FFFFFF')
        rect_java = SurroundingRectangle(text_java, buff=MED_LARGE_BUFF)
        java = VGroup(text_java, rect_java).to_edge(RIGHT, buff=edge_buff)

        text_julia = Text('Julia', font_size=font_size_title, font='Lato', color='#FFFFFF')
        rect_julia = SurroundingRectangle(text_julia, buff=MED_LARGE_BUFF)
        julia = VGroup(text_julia, rect_julia).to_edge(LEFT, buff=edge_buff).shift(DOWN*3)

        text_lisp = Text('Lisp', font_size=font_size_title, font='Lato', color='#FFFFFF')
        rect_lisp = SurroundingRectangle(text_lisp, buff=MED_LARGE_BUFF)
        lisp = VGroup(text_lisp, rect_lisp).to_edge(RIGHT, buff=edge_buff).shift(DOWN*6)


        self.play(Write(python))
        self.play(Write(r))
        self.play(Write(java))
        self.play(Write(julia))
        self.play(Write(lisp))
        self.wait(2)

        # move to python
        self.play(python.animate.shift(UP*0.5), self.camera.frame.animate.set(width=python.width*1.5).move_to(python).shift(DOWN*0.4))
        self.wait(2)
        why_python_1 = 'پایتون پرکاربردترین زبان برنامه‌نویسی برای هوش مصنوعیه.'
        why_python_1 = tex_fa(why_python_1).next_to(python, DOWN)

        why_python_2 = 'پایتون هم برای تازه واردها و هم برای متخصصین هوش'
        why_python_2 = tex_fa(why_python_2).next_to(why_python_1, DOWN).align_to(why_python_1, RIGHT)
        why_python_2_1 = 'مصنوعی مناسبه.'
        why_python_2_1 = tex_fa(why_python_2_1).next_to(why_python_2, DOWN*0.5).align_to(why_python_1, RIGHT)

        why_python_3 = 'به گزارش \lr{stackoverflow} سال 2022 به طور متوسط، 71165'
        why_python_3 = tex_fa(why_python_3).next_to(why_python_2_1, DOWN).align_to(why_python_1, RIGHT)     
        why_python_3_1 = 'دلار درآمد سالیانه‌ی برنامه نویس‌های \lr{Python} بوده.'
        why_python_3_1 = tex_fa(why_python_3_1).next_to(why_python_3, DOWN*0.5).align_to(why_python_1, RIGHT)     
        
        self.play(Write(why_python_1), reverse=True)
        self.play(Write(why_python_2), reverse=True)
        self.play(Write(why_python_2_1), reverse=True)
        self.play(Write(why_python_3), reverse=True)
        self.play(Write(why_python_3_1), reverse=True)
        self.wait(3)
        # move to R 
        self.play(r.animate.shift(UP*0.5), self.camera.frame.animate.set(width=python.width*1.5).move_to(r).shift(DOWN*0.4), FadeOut(why_python_1, why_python_2, why_python_2_1, why_python_3, why_python_3_1))
        self.wait(2)

        why_r_1 = '\lr{R} دومین زبان برنامه نویسی پرکاربرد برای هوش مصنوعی و آماره.'
        why_r_1 = tex_fa(why_r_1).next_to(r, DOWN)

        why_r_2 = '\lr{R} برای کسایی مناسبه که علاقه‌ی زیادی به یادگیری برنامه نویسی'
        why_r_2 = tex_fa(why_r_2).next_to(why_r_1, DOWN).align_to(why_r_1, RIGHT)
        why_r_2_1 = 'ندارن.'
        why_r_2_1 = tex_fa(why_r_2_1).next_to(why_r_2, DOWN*0.5).align_to(why_r_1, RIGHT)
       
        why_r_3 = 'به گزارش  سال 2022 \lr{stackoverflow} به طور متوسط، 67734'
        why_r_3 = tex_fa(why_r_3).next_to(why_r_2_1, DOWN).align_to(why_r_1, RIGHT)     
        why_r_3_1 = 'دلار درآمد سالیانه‌ی برنامه نویسهای \lr{R} بوده.'
        why_r_3_1 = tex_fa(why_r_3_1).next_to(why_r_3, DOWN*0.5).align_to(why_r_1, RIGHT)    

        why_r_4 = '\lr{RStudio} معروف ترین فریم‌ورک این زبان برنامه نویسیه.'
        why_r_4 = tex_fa(why_r_4).next_to(why_r_3_1, DOWN).align_to(why_r_1, RIGHT)     
        
        self.play(Write(why_r_1), reverse=True)
        self.play(Write(why_r_2), reverse=True)
        self.play(Write(why_r_2_1), reverse=True)
        self.play(Write(why_r_3), reverse=True)
        self.play(Write(why_r_3_1), reverse=True)
        self.play(Write(why_r_4), reverse=True)

        self.wait(3)
        
        # move to java
        self.play(java.animate.shift(UP*0.4),self.camera.frame.animate.set(width=python.width*1.5).move_to(java).shift(DOWN*0.5), FadeOut(why_r_1, why_r_2, why_r_2_1, why_r_3, why_r_3_1, why_r_4))
        self.wait(2)

        why_java_1 = 'جاوا یک زبان برنامه نویسی معروفه که بیشتر برای کارهایی'
        why_java_1 = tex_fa(why_java_1).next_to(java, DOWN)
        why_java_1_2 = 'غیر از یادگیری ماشین استفاده میشه.'
        why_java_1_2 = tex_fa(why_java_1_2).next_to(why_java_1, DOWN*0.5).align_to(why_java_1,RIGHT)

        why_java_2 = 'اما دوتا از فریم‌ورک‌های معروف حوزه‌ی آمار و هوش مصنوعی'
        why_java_2 = tex_fa(why_java_2).next_to(why_java_1_2, DOWN).align_to(why_java_1, RIGHT)
        why_java_2_1 = 'یعنی وِکا و رپید ماینر، با استفاده از جاوا توسعه یافتن.'
        why_java_2_1 = tex_fa(why_java_2_1).next_to(why_java_2, DOWN*0.5).align_to(why_java_1, RIGHT)
       
        why_java_3 = 'به گزارش  سال 2022 \lr{stackoverflow} به طور متوسط، 64572'
        why_java_3 = tex_fa(why_java_3).next_to(why_java_2_1, DOWN).align_to(why_java_1, RIGHT)     
        why_java_3_1 = 'دلار درآمد سالیانه‌ی برنامه نویسهای \lr{Java} بوده.'
        why_java_3_1 = tex_fa(why_java_3_1).next_to(why_java_3, DOWN*0.5).align_to(why_java_1, RIGHT)     
        
        self.play(Write(why_java_1), reverse=True)
        self.play(Write(why_java_1_2), reverse=True)
        self.play(Write(why_java_2), reverse=True)
        self.play(Write(why_java_2_1), reverse=True)
        self.play(Write(why_java_3), reverse=True)
        self.play(Write(why_java_3_1), reverse=True)   

        self.wait(3)     
        
        # move to julia
        self.play(julia.animate.shift(UP*0.4), self.camera.frame.animate.set(width=python.width*1.5).move_to(julia).shift(DOWN*0.5), FadeOut(why_java_1, why_java_1_2,why_java_2,  why_java_2_1, why_java_3, why_java_3_1))
        self.wait(2)
        
        why_julia_1 = 'جولیا یک زبان برنامه نویسی پرکاربرد دیگه‌ست که ازش برای'
        why_julia_1 = tex_fa(why_julia_1).next_to(julia, DOWN)
        why_julia_1_2 = 'هوش مصنوعی هم استفاده میشه.'
        why_julia_1_2 = tex_fa(why_julia_1_2).next_to(why_julia_1, DOWN*0.5).align_to(why_julia_1,RIGHT)

        why_julia_2 = 'جولیا برای انجام محاسبات ریاضی سنگین توسعه داده شده.'
        why_julia_2 = tex_fa(why_julia_2).next_to(why_julia_1_2, DOWN).align_to(why_julia_1, RIGHT)
        why_julia_2_1 = 'بنابراین میتونه برای یادگیری ماشین هم ازش استفاده بشه.'
        why_julia_2_1 = tex_fa(why_julia_2_1).next_to(why_julia_2, DOWN*0.5).align_to(why_julia_1, RIGHT)
       
        why_julia_3 = 'به گزارش  سال 2022 \lr{stackoverflow} به طور متوسط، 77966'
        why_julia_3 = tex_fa(why_julia_3).next_to(why_julia_2_1, DOWN).align_to(why_julia_1, RIGHT)     
        why_julia_3_1 = ' دلار درآمد سالیانه‌ی برنامه نویسهای \lr{Julia} بوده.'
        why_julia_3_1 = tex_fa(why_julia_3_1).next_to(why_julia_3, DOWN*0.5).align_to(why_julia_1, RIGHT)     
        
        self.play(Write(why_julia_1), reverse=True)
        self.play(Write(why_julia_1_2), reverse=True)
        self.play(Write(why_julia_2), reverse=True)
        self.play(Write(why_julia_2_1), reverse=True)
        self.play(Write(why_julia_3), reverse=True)
        self.play(Write(why_julia_3_1), reverse=True)   

        self.wait(3)     

        # move to lisp
        self.play(lisp.animate.shift(UP*0.4), self.camera.frame.animate.set(width=python.width*1.5).move_to(lisp).shift(DOWN*0.5), FadeOut(why_julia_1, why_julia_1_2, why_julia_2, why_julia_2_1, why_julia_3, why_julia_3_1))
        self.wait(2)

        why_lisp_1 = '\lr{Lisp} قدیمی‌ترین زبان برنامه نویسی در این لیسته که توسط جان'
        why_lisp_1 = tex_fa(why_lisp_1).next_to(lisp, DOWN)
        why_lisp_1_2 = 'مک‌کارتی یکی از پیشگامان هوش مصنوعی توسعه یافته.'
        why_lisp_1_2 = tex_fa(why_lisp_1_2).next_to(why_lisp_1, DOWN*0.5).align_to(why_lisp_1,RIGHT)

        why_lisp_2 = 'یکی از معروف‌ترین فریم‌ورکهای \lr{Lisp}، \lr{Clojure} هست'
        why_lisp_2 = tex_fa(why_lisp_2).next_to(why_lisp_1_2, DOWN).align_to(why_lisp_1, RIGHT)
        why_lisp_2_1 = 'که پر درآمدترین زبان برنامه نویسی موجوده.'
        why_lisp_2_1 = tex_fa(why_lisp_2_1).next_to(why_lisp_2, DOWN*0.5).align_to(why_lisp_1, RIGHT)
       
        why_lisp_3 = 'به گزارش  سال 2022 \lr{stackoverflow} به طور متوسط، 106644'
        why_lisp_3 = tex_fa(why_lisp_3).next_to(why_lisp_2_1, DOWN).align_to(why_lisp_1, RIGHT)     
        why_lisp_3_1 = ' دلار درآمد سالیانه‌ی برنامه نویسهای \lr{Clojure} بوده.'
        why_lisp_3_1 = tex_fa(why_lisp_3_1).next_to(why_lisp_3, DOWN*0.5).align_to(why_lisp_1, RIGHT)     
        
        self.play(Write(why_lisp_1), reverse=True)
        self.play(Write(why_lisp_1_2), reverse=True)
        self.play(Write(why_lisp_2), reverse=True)
        self.play(Write(why_lisp_2_1), reverse=True)
        self.play(Write(why_lisp_3), reverse=True)
        self.play(Write(why_lisp_3_1), reverse=True)   

        self.wait(3)     

        # restoring back the frame to its original state
        self.play(Restore(self.camera.frame), 
            FadeOut(why_lisp_1, why_lisp_1_2, why_lisp_2, why_lisp_2_1, why_lisp_3, why_lisp_3_1),
            python.animate.shift(DOWN*0.4),
            r.animate.shift(DOWN*0.4),
            java.animate.shift(DOWN*0.4),
            julia.animate.shift(DOWN*0.4),
            lisp.animate.shift(DOWN*0.4))
        self.wait(2)


        

        






        



