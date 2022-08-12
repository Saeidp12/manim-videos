from manim import *

font_size_text = 48
font_size_math = 55
# font_size_matrices=45

# Caution: These functions should be used inside the scene!

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