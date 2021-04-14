# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:45:41 2021

@author: Main Floor
"""


from tkinter import *
from Highlight.Highlight import MouseoverHighlight



####################################################################################################
###
###     Canvas for Highlighting: PopupMenu
###
###        This class allows you to bind an arbitrary PopupMenu to a canvas
###     widget object. When the mouse passes over the object, the PopUp Menu
###     can be called by way of a Right Button Click. In theory, the popupmenu
###     should pertain to that particular widget. However, it is unknown how
###     exactly this will play out. Future edits may be necessary
###
###
###     Author:  Chad Unterschultz
###
###     V 1.0.0    Feb 13, 2021
###     V 1.0.1    Feb 27, 2021   Added a counter to ensure multiple popup menues aren't
###                               all created for the same single click.


debugging = True
VERSION     = (1,0,1)
VERSION_s   = "%s.%s.%s" %VERSION



class PopupMenu:
    """ Class PopupMenu
        Usage: MouseoverHighlight(<widget>, <window>, <canvas>, <menu>, <window>)
        <widget>         = required, widget you are trying to enclose or highlight
        <window>         = required, the window within which the widget lives
        <canvas>         = required, the canvas within which the widget lives
        <menu>           = required, the menu you want to popup
        <window>         = optional, is this a window in canvas?
    """

    COLOURS  = ['black', 'snow', 'ghost white', 'white smoke', 'gainsboro',
                'floral white', 'old lace', 'linen', 'antique white',
                'papaya whip', 'blanched almond', 'bisque', 'peach puff',
                'navajo white', 'lemon chiffon', 'mint cream', 'azure',
                'alice blue', 'lavender', 'lavender blush', 'misty rose',
                'dark slate gray', 'dim gray', 'slate gray', 'light slate gray',
                'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
                'dark slate blue', 'slate blue', 'medium slate blue',
                'light slate blue', 'medium blue', 'royal blue',  'blue',
                'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue',
                'steel blue', 'light steel blue', 'light blue', 'powder blue',
                'pale turquoise', 'dark turquoise', 'medium turquoise',
                'turquoise', 'cyan', 'light cyan', 'cadet blue',
                'medium aquamarine', 'aquamarine', 'dark green',
                'dark olive green', 'dark sea green', 'sea green',
                'medium sea green', 'light sea green', 'pale green',
                'spring green', 'lawn green', 'medium spring green',
                'green yellow', 'lime green', 'yellow green', 'forest green',
                'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
                'light goldenrod yellow', 'light yellow', 'yellow', 'gold',
                'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
                'indian red', 'saddle brown', 'sandy brown', 'dark salmon',
                'salmon', 'light salmon', 'orange', 'dark orange', 'coral',
                'light coral', 'tomato', 'orange red', 'red', 'hot pink',
                'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon',
                'medium violet red', 'violet red', 'medium orchid',
                'dark orchid', 'dark violet', 'blue violet', 'purple',
                'medium purple', 'thistle', 'snow2', 'snow3', 'snow4',
                'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1',
                'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2',
                'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4',
                'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2',
                'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
                'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2',
                'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3',
                'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4',
                'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2',
                'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2',
                'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2',
                'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
                'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3',
                'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4',
                'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3',
                'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
                'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2',
                'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1',
                'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2',
                'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
                'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2',
                'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2',
                'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4',
                'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3',
                'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1',
                'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1',
                'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
                'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3',
                'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2',
                'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2',
                'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
                'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2',
                'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2',
                'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2',
                'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
                'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2',
                'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2',
                'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2',
                'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
                'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3',
                'sienna4', 'burlywood1', 'burlywood2', 'burlywood3',
                'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
                'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3',
                'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4',
                'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
                'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3',
                'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1',
                'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2',
                'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4',
                'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3',
                'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1',
                'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3',
                'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4',
                'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3',
                'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4',
                'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
                'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2',
                'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4',
                'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
                'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3',
                'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4',
                'MediumPurple1', 'MediumPurple2', 'MediumPurple3',
                'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
                'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7',
                'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13',
                'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
                'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25',
                'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31',
                'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
                'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44',
                'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50',
                'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
                'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62',
                'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68',
                'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
                'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80',
                'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86',
                'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
                'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

    Canvas_Items = ["arc", "bitmap", "image", "line", "oval", "polygon",
                    "rectangle", "text", "window"]

    def __init__(self, Widget, Root, Canvas_, Menu_, Manager = None, window = False):
        '''  Tie the Popup Menu behavior to the widget that has been inputted  '''

        self.config_check( Widget, Root, Canvas_, Menu_, Manager, window)
        self.canvas_setup()


    def config_check(self, Widget, Root, Canvas_, Menu_, Manager, window ):
        ''' Check that the variables are all valid types '''

        if ( (Root.__class__.__name__ != Tk.__name__) &                        # Is the Root a tkinter Window or Frame?
            ( Root.__class__.__name__ != Frame.__name__) ):
            raise TypeError ("<Root> must be a Window or a Frame")
        else:
            self.Root = Root


        if (Canvas_.__class__.__name__ != Canvas.__name__) :                   # Is the Canvas a tkiner Canvas?
            raise TypeError ("<Canvas_> must be a Canvas Widget")
        else:
            self.Canvas = Canvas_


        if window == False:
            if self.Canvas.type(Widget) not in PopupMenu.Canvas_Items:             # Is the Widget part of the Canvas?
                raise TypeError ("<Widget> must be a Canvas Widget")
            else:
                self.Widget = Widget
        else:
            self.Widget = Widget


        if (( Menu_.__class__.__name__ != Menu.__name__)):                     # Is the Menu a Tkinter Dropdown Menu?
            raise TypeError ("<menu> must be a tkinter menu")
        else:
            self.Menu = Menu_

        self.Manager = Manager
        self.check_time = 500
        self.Window = window

    def canvas_setup(self):

        if self.Window == True:
            print("bound")
            self.Widget.bind("<Enter>", self.allowPopUp, add = '+')   #   If mouse enters widget area
            self.Widget.bind("<Leave>", self.preventPopUp, add = '+')   #   If mouse leaves widget area

        else:
            self.Canvas.tag_bind(self.Widget, '<Enter>', self.allowPopUp, add = '+') #Menu can only be shown upon mousover
            self.Canvas.tag_bind(self.Widget, '<Leave>', self.preventPopUp, add = '+') #Menu hidden


    def allowPopUp(self, event = None):

        if self.Window == True:
            self.Widget.bind("<Button-3>", self.showmenu, add = '+')
        else:
            self.Canvas.bind('<Button-3>', self.showmenu, add = '+')               # Right Click to Show

        self.PopUpPresent = None

    def preventPopUp(self, event = None):

        if self.Window == True:
            self.Widget.unbind("<Button-3>")
        else:
            self.Canvas.unbind('<Button-3>')                                       #A way of unbinding only a single handler?

        self.Menu.unpost()
        self.PopUpPresent = None

        #if "showmenu_check_handler" in self.__dict__.keys():
        #    if self.showmenu_check_handler != None:
        #       self.Root.after_cancel(self.showmenu_check_handler)
        #       del self.showmenu_check_handler
        #    self.showmenu_check_handler = None



    def showmenu(self, event):
        if debugging == True: print("Pop up Menu")
        #if self.Manager != None:
        #    self.Manager.PopupMenu_update(event)
        #    if debugging == True: print("Passed Event position X: ", event.x)
        if self.PopUpPresent == None:                                          # Only Allow one Popup At a Time
            self.Menu.post(event.x_root, event.y_root)                             #Display PopupMenu at button click locations
            self.PopUpPresent = 1

        #self.showmenu_check_handler  = self.Root.after(self.check_time, self.showmenu_check)



    def showmenu_check(self):
        ''' Leaving the Text Widget Region Eliminates the ability to cause a Popup .
        Ended up not being necessary     '''

        buffer_distance = 25 #number of pixels you can be near something and still count as on it

        canvas_X = self.Canvas.winfo_rootx() #Canvas Top Left Absolute Position
        canvas_Y = self.Canvas.winfo_rooty() #Canvas Top Left Absolute Position

        mouse_X = self.Canvas.winfo_pointerx() #Mouse Absolute Position
        mouse_Y = self.Canvas.winfo_pointery()

        if self.Window == True:

            Xpos = self.Widget.winfo_rootx()                               # Widget absolute Position
            Ypos = self.Widget.winfo_rooty()

            width = self.Widget.winfo_width()                              #Widget Width and Height (in pixels)
            height = self.Widget.winfo_height()

            canvas_x = self.Canvas.winfo_rootx()                           # Canvas Top Left Absolute Position
            canvas_y = self.Canvas.winfo_rooty()

            Xmin = Xpos - canvas_x                                         # Relative Position of Anchor
            Ymin = Ypos - canvas_y
            Xmax = Xmin + width
            Ymax = Ymin + height
            position = (Xmin, Ymin, Xmax, Ymax)
        else:
            position = self.Canvas.bbox(self.Widget)

        mouse_X = mouse_X - canvas_X
        mouse_Y = mouse_Y - canvas_Y

        widget_minX = position[0] - buffer_distance
        widget_maxX = position[2] + buffer_distance

        widget_minY = position[1] - buffer_distance
        widget_maxY = position[3] + buffer_distance

        menu_X = self.Menu.winfo_rootx()
        menu_Y = self.Menu.winfo_rooty()

        menu_Width = self.Menu.winfo_width()
        menu_Height = self.Menu.winfo_height()

        menu_minX = menu_X - buffer_distance
        menu_maxX = menu_X + menu_Width + buffer_distance

        menu_minY = menu_Y - buffer_distance
        menu_maxY = menu_Y + menu_Height + buffer_distance

        if ( ( (widget_minX <= mouse_X <= widget_maxX) & (widget_minY <= mouse_Y <= widget_maxY) ) |
            ( (menu_minX <= mouse_X <= menu_maxX) & (menu_minY <= mouse_Y <= menu_maxY) ) ):
            if self.showmenu_check_handler == None: #check not already scheduled for sometime in the future
                self.showmenu_check_handler = self.Root.after(self.check_time, self.showmenu_check)

            else:
                self.deletePopUp()



    def version(self):
        global VERSION_S
        global DATE
        if debugging == True: print(VERSION_S)
        if debugging == True: print( DATE )
        return VERSION_S, DATE



if __name__ == "__main__":
    debugging = True

    if debugging == True: print("Library File Test")

    Root = Tk()
    Root.focus_set()


    canvas = Canvas(Root, width = 400, height = 400)
    canvas.pack()

    menu = Menu(Root, tearoff = 0)
    menu.add_command(label = "1 Insert Line", command = Root.bell)
    menu.add_command(label = "2 Insert Section", command = Root.bell)
    menu.add_command(label = "3 Delete Line", command = Root.bell)
    menu.add_command(label = "4 Delete Section", command = Root.bell)

    submenu = Menu(menu, tearoff = 0)
    submenu.add_command(label = "Edit Mode")
    submenu.add_command(label = "Attach Mode")
    submenu.add_command(label = "Finish Mode")
    menu.add_cascade(label = "edit", menu = submenu)

    if debugging == True: print("Test: ", menu.__class__.__name__)
    if debugging == True: print("Test: ", Menu.__name__)
    if debugging == True: print("Menu Test: ", menu.__class__.__name__ == Menu.__name__)







    canvasText2 = canvas.create_text(10, 10, text = "Box Outline Highlight", anchor = NW)
    canvasText2_highlight = MouseoverHighlight(canvasText2, Root, canvas, highlightOption = 0x02)
    canvasText2_highlight = PopupMenu(canvasText2, Root, canvas, menu)


    Root.mainloop()



