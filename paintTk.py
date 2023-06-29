
import pyscreenshot
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tktooltip import ToolTip



class Paint:
    def __init__(self) -> None:        
        self.window = Tk()
        self.window.title('Paint')
        self.window.minsize(width=1100, height=620)
        self.window.resizable(0,0)
       
        self.oval_brush = True
        self.line_brush = False
        self.ereaser_brush = False
       
       #------------ Icons Usados aos botoes -------------------# 
        self.img_line = PhotoImage(file='icons/line.png')
        self.img_oval = PhotoImage(file='icons/oval.png')
        self.img_eraser = PhotoImage(file='icons/eraser.png')
        self.img_save = PhotoImage(file='icons/save.png')
        self.img_square = PhotoImage(file='icons/square.png')
        self.img_new = PhotoImage(file='icons/new.png') 
              
        self.colors = ('black', 'red','orange','white','purple','blue','green',
                        '#3b3b3b','yellow','pink', 'magenta','DeepPink2','cyan',
                        'coral','gray19','azure','LightBlue1','medium spring green')
        
        self.bar_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar_menu.pack(fill = 'x')
        
        self.pick_colors ='black'
                
        self.text_color = Label(self.bar_menu, text = '  Colors:  ', fg='white', bg='#3b3b3b')
        self.text_color.pack(side = 'left')

        #------------ Laço para a seleção de Cores--------------------------------#       
        for i in self.colors: 
            self.button_color = Button(self.bar_menu, bg=i, width=3, height=2,command=lambda col=i: self.select_colors(col))
            self.button_color.pack(side = 'left')
        #---------------------------------------------------------------------------# 
        
        self.label_colors_choose = Label(self.bar_menu, text = '  Color Choose:  ', fg='white', bg='#3b3b3b')
        self.label_colors_choose.pack(side = 'left')

        self.color_choose = Button(self.bar_menu, image=self.img_square, bd=0,bg='#3b3b3b',
                            command=self.selected_color)
        self.color_choose.pack(side = 'left')                 

        self.text_pen_size = Label(self.bar_menu, text='  Size: ', fg='white', bg='#3b3b3b')
        self.text_pen_size.pack(side= 'left') 
        
        self.pen_size = Spinbox(self.bar_menu, from_ =1, to=50)
        self.pen_size.pack(side= 'left')        
        
        self.text_brush = Label(self.bar_menu, text = '  Brushs:  ', fg='white', bg='#3b3b3b')
        self.text_brush.pack(side= 'left')

        self.button_line = Button(self.bar_menu, image=self.img_line, bg='#3b3b3b' ,bd=0,command=self.brush_line)
        self.button_line.pack(side= 'left')
        self.button_oval = Button(self.bar_menu, image=self.img_oval, bg='#3b3b3b',bd=0,command=self.brush_oval)
        self.button_oval.pack(side= 'left')
        self.button_eraser = Button(self.bar_menu, image=self.img_eraser, bg='#3b3b3b',bd=0, command=self.brush_eraser)
        self.button_eraser.pack(side= 'left')
               
        self.text_options = Label(self.bar_menu, text = '  Options:  ', fg='white', bg='#3b3b3b')
        self.text_options.pack(side= 'left')
        
        self.button_save = Button(self.bar_menu, image=self.img_save, bg='#3b3b3b',bd=0, command=self.save)
        self.button_save.pack(side= 'left')

        self.button_new = Button(self.bar_menu, image=self.img_new, bg='#3b3b3b',bd=0, command = self.clean)
        self.button_new.pack(side= 'left')

        self.area_draw= Canvas(self.window, height=620, bg='gainsboro')
        self.area_draw.pack(fill = 'both')
        self.area_draw.bind('<B1-Motion>', self.draw)
        
        # self.window.bind('<F1>', self.clean) --- Ao apertar a tecla f1 Limpa o Desenho - Adcionar (event) na Função como parametos
        # self.window.bind('<F2>', self.save) --- Ao apertar a tecla f2 Salva o Desenho - Adcionar (event) na Função como parametos
        
        self.window.bind('<Escape>',self.exit_esc) # tecla Esc Fecha a Janela. obs: Salvar ants.

        #------------ Baloes de mensagens --------------------------------#
        self.tooltips = ToolTip(self.button_save, msg='Save (F2)', delay=0.2)
        self.tooltips = ToolTip(self.button_new, msg='New Draw (F1)', delay=0.2)
        self.tooltips = ToolTip(self.button_line, msg='Line', delay=0.2)
        self.tooltips = ToolTip(self.button_oval, msg='Circle', delay=0.2)
        self.tooltips = ToolTip(self.button_eraser, msg='Eraser', delay=0.2)
        self.tooltips = ToolTip(self.color_choose, msg='Selector The Colors', delay=0.2)
        
        self.window.mainloop()

    
    def draw(self, event): # Desenha apartir dos eixos x e y
        x1,y1 = event.x, event.y
        x2, y2 = event.x, event.y

        if self.oval_brush:
            self.area_draw.create_oval(x1,y1,x2,y2, fill =self.pick_colors,
                                      outline=self.pick_colors,width=self.pen_size.get())
        elif self.line_brush:
            self.area_draw.create_line(x1-10,y1-10,x2,y2, fill =self.pick_colors,width=self.pen_size.get())
        else:
            self.area_draw.create_oval(x1,y1,x2,y2, fill ='gainsboro',
                                        outline='gainsboro',width=self.pen_size.get())

    
    def select_colors(self,col):
        self.pick_colors = col

    def brush_oval(self):  # Circular
        self.oval_brush = True
        self.line_brush = False
        self.ereaser_brush = False

    def brush_line(self): # Linha
        self.oval_brush = False
        self.line_brush = True
        self.ereaser_brush = False

    def brush_eraser(self): # Borracha
        self.oval_brush = False
        self.line_brush = False
        self.ereaser_brush = False

    def clean(self): # Apaga todo Desenho - 'New'
        self.area_draw.delete('all')
        
    
#------------Salva o Desenho na mesma Pasta do Projeto------------#   
    def save(self):
        try:
            x = self.window.winfo_rootx() + self.area_draw.winfo_x()
            y = self.window.winfo_rooty() + self.area_draw.winfo_y()
            x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
            y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()
            
            img = pyscreenshot.grab(bbox=(x,y,x1,y1))
            img.save('image.png', 'png')  # pode alterar para '.jpeg'           
        
        except Exception as error:
            messagebox.showerror('Erro', error)

        else:
            messagebox.showinfo('Save', '''Imagem Salva com Sucesso !
Recomendaçao: Renomear o nome do arquivo.''')
        
    
#------------Caso o Save anterior apresente Erro ao salvar o desenho....-------#
    def new_save_canvas(self):
        self.area_draw.postscript(file= 'circles.eps')
        from PIL import Image
        img = Image.open('circles.eps')
        img.save('circles.png', 'png')
        messagebox.showinfo('Save', 'Imagem Salva com Sucesso !')
#------------ Chamar esta nova Save , esta função salva em 2 tipos de Extensão----#
#------------------------Extensão '.eps' e a outra Extensão '.png'-------------------------#

    
    def selected_color(self): # Seletor de Cores
        color = askcolor(title='Seletor de Cores')
        self.select_colors(color[1])

    def exit_esc(self,event):
        self.window.quit()
        return event
        





if __name__ =='__main__':
    app = Paint()



