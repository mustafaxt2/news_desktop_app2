from newsApi import news
from customtkinter import * 
import webbrowser
from images import Images
from currencyApi import *

class Window(CTk):
    def __init__(self):
        super().__init__()
        self.title("News")
        self.geometry("1000x450")
        self.resizable(False,False)
        self.iconbitmap("images\\news.ico")
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.default_color=('#979DA2', '#565B5E')
        self.navigationBar=CTkFrame(self,corner_radius=0)
        self.navigationBar.grid(row=0,column=0,sticky="nsew")
        self.navigationBar.grid_columnconfigure(0,weight=1)
        self.navigationBar.grid_rowconfigure(8,weight=1)

        self.navigationBar_label=CTkLabel(self.navigationBar,text=" Home",image=Images().home_image,compound="left",font=CTkFont(size=15, weight="bold"))
        self.navigationBar_label.grid(row=0,column=0,padx=20,pady=20)

        self.navigationBar_button1=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Home",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().home_image,
                                            anchor="w",
                                            command=self.homeButton)
        self.navigationBar_button1.grid(row=1,column=0,sticky="ew")

        self.navigationBar_button2=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Business",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().business_image,
                                            anchor="w",
                                            command=self.businessButton)
        self.navigationBar_button2.grid(row=2,column=0,sticky="ew")

        self.navigationBar_button3=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Entertainment",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().entertainment_image,
                                            anchor="w",
                                            command=self.entertainmentButton)
        self.navigationBar_button3.grid(row=3,column=0,sticky="ew")

        self.navigationBar_button4=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Sports",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().sports_image,
                                            anchor="w",
                                            command=self.sportsButton)
        self.navigationBar_button4.grid(row=4,column=0,sticky="ew")

        self.navigationBar_button5=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Science",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().science_image,
                                            anchor="w",
                                            command=self.scienceButton)
        self.navigationBar_button5.grid(row=5,column=0,sticky="ew")

        self.navigationBar_button6=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Health",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().health_image,
                                            anchor="w",
                                            command=self.healthButton)
        self.navigationBar_button6.grid(row=6,column=0,sticky="ew")

        self.navigationBar_button7=CTkButton(self.navigationBar,
                                            corner_radius=0,
                                            height=40,
                                            border_spacing=10,
                                            text="Technology",
                                            fg_color="transparent",
                                            text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=Images().technology_image,
                                            anchor="w",
                                            command=self.technologyButton)
        self.navigationBar_button7.grid(row=7,column=0,sticky="ew")

        self.appearance_mode_menu = CTkOptionMenu(self.navigationBar,
                                                                values=["Dark", "Light", "System"],
                                                                fg_color=self.default_color,
                                                                text_color=("gray10", "gray90"),
                                                                button_color=self.default_color,
                                                                button_hover_color=("gray70", "gray30"),
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=8, column=0, padx=20, pady=20, sticky="s")

        self.frame=CTkFrame(self,corner_radius=0,fg_color="transparent",border_width=3)
        self.frame.grid(row=0,column=1,sticky="nsew")
        self.frame.grid_rowconfigure(2,weight=1)
        self.frame.grid_columnconfigure(2,weight=1)

        self.homeFrame=CTkFrame(self.frame,corner_radius=0,fg_color="transparent")

        self.businessFrame=CTkFrame(self.frame,corner_radius=3,fg_color="transparent")
        self.businessFrame.grid_rowconfigure(10,weight=1)
        self.entertainmentFrame=CTkFrame(self.frame,corner_radius=3,fg_color="transparent")
        self.entertainmentFrame.grid_rowconfigure(10,weight=1)
        self.sportsFrame=CTkFrame(self.frame,corner_radius=3,fg_color="transparent")
        self.sportsFrame.grid_rowconfigure(10,weight=1)
        self.scienceFrame=CTkFrame(self.frame,corner_radius=3,fg_color="transparent")
        self.scienceFrame.grid_rowconfigure(10,weight=1)
        self.healthFrame=CTkFrame(self.frame,corner_radius=3,fg_color="transparent")
        self.healthFrame.grid_rowconfigure(10,weight=1)
        self.technologyFrame=CTkFrame(self.frame,corner_radius=3,fg_color="transparent")
        self.technologyFrame.grid_rowconfigure(10,weight=1)

        self.homeFrame_label=CTkLabel(self.homeFrame,text="",image=Images().currencies_image,compound="top",font=CTkFont(size=20, weight="bold"))
        self.homeFrame_label.place(relx=0.45,rely=0.4)

        self.homeFrame_label1=CTkLabel(self.homeFrame,text=f"USD/EUR\n{currencies['EUR']}",image=Images().euro_image,compound="top",font=CTkFont(size=15, weight="bold"))
        self.homeFrame_label1.place(relx=0.15,rely=0.1)

        self.homeFrame_label2=CTkLabel(self.homeFrame,text=f"USD/GBP\n{currencies['GBP']}",image=Images().gbp_image,compound="top",font=CTkFont(size=15, weight="bold"))
        self.homeFrame_label2.place(relx=0.475,rely=0.1)

        self.homeFrame_label3=CTkLabel(self.homeFrame,text=f"USD/CHF\n{currencies['CHF']}",image=Images().chf_image,compound="top",font=CTkFont(size=15, weight="bold"))
        self.homeFrame_label3.place(relx=0.8,rely=0.1)

        self.homeFrame_label4=CTkLabel(self.homeFrame,text=f"USD/JPY\n{currencies['JPY']}",image=Images().jpy_image,compound="top",font=CTkFont(size=15, weight="bold"))
        self.homeFrame_label4.place(relx=0.15,rely=0.75)

        self.homeFrame_label5=CTkLabel(self.homeFrame,text=f"USD/RUB\n{currencies['RUB']}",image=Images().rub_image,compound="top",font=CTkFont(size=15, weight="bold"))
        self.homeFrame_label5.place(relx=0.475,rely=0.75)

        self.homeFrame_label6=CTkLabel(self.homeFrame,text=f"USD/TRY\n{currencies['TRY']}",image=Images().try_image,compound="top",font=CTkFont(size=15, weight="bold"))
        self.homeFrame_label6.place(relx=0.8,rely=0.75)

        self.select_frame_by_name("Home")


    def callback(self,url):
        webbrowser.open_new_tab(url)


    def homeButton(self):
        self.select_frame_by_name("Home")
        self.navigationBar_label.configure(text=" Home",image=Images().home_image)

    def businessButton(self):
        self.select_frame_by_name("Business")
        self.navigationBar_label.configure(text=" Business",image=Images().business_image)
        if len(news.businessNews)==0:
            news.get_news("business",news.businessNews)
            buttons=[]
            k=0
            for i in news.businessNews:
                buttons.append(CTkButton(self.businessFrame,
                                  text=i._title,
                                  fg_color="transparent",
                                  text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=None,
                                  height=40,
                                  anchor="w",
                                  font=CTkFont(size=12, weight="bold"),
                                  command=lambda i=i:self.callback(i._url)))
                buttons[k].grid(row=k,column=0,padx=5,pady=5,sticky="ew")
                k+=1
                if k==10:
                    break

    def entertainmentButton(self):
        self.select_frame_by_name("Entertainment")
        self.navigationBar_label.configure(text=" Entertainment",image=Images().entertainment_image)
        if len(news.entertainmentNews)==0:
            news.get_news("entertainment",news.entertainmentNews)
            buttons=[]
            k=0
            for i in news.entertainmentNews:
                buttons.append(CTkButton(self.entertainmentFrame,
                                  text=i._title,
                                  fg_color="transparent",
                                  text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=None,
                                  height=40,
                                  anchor="w",
                                  font=CTkFont(size=12, weight="bold"),
                                  command=lambda i=i:self.callback(i._url)))
                buttons[k].grid(row=k,column=0,padx=5,pady=5,sticky="ew")
                k+=1
                if k==10:
                    break

    def sportsButton(self):
        self.select_frame_by_name("Sports")
        self.navigationBar_label.configure(text=" Sports",image=Images().sports_image)
        if len(news.sportsNews)==0:
            news.get_news("sports",news.sportsNews)
            buttons=[]
            k=0
            for i in news.sportsNews:
                buttons.append(CTkButton(self.sportsFrame,
                                  text=i._title,
                                  fg_color="transparent",
                                  text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=None,
                                  height=40,
                                  anchor="w",
                                  font=CTkFont(size=12, weight="bold"),
                                  command=lambda i=i:self.callback(i._url)))
                buttons[k].grid(row=k,column=0,padx=5,pady=5,sticky="ew")
                k+=1
                if k==10:
                    break

    def scienceButton(self):
        self.select_frame_by_name("Science")
        self.navigationBar_label.configure(text=" Science",image=Images().science_image)
        if len(news.scienceNews)==0:
            news.get_news("science",news.scienceNews)
            buttons=[]
            k=0
            for i in news.scienceNews:
                buttons.append(CTkButton(self.scienceFrame,
                                  text=i._title,
                                  fg_color="transparent",
                                  text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=None,
                                  height=40,
                                  anchor="w",
                                  font=CTkFont(size=12, weight="bold"),
                                  command=lambda i=i:self.callback(i._url)))
                buttons[k].grid(row=k,column=0,padx=5,pady=5,sticky="ew")
                k+=1
                if k==10:
                    break

    def healthButton(self):
        self.select_frame_by_name("Health")
        self.navigationBar_label.configure(text=" Health",image=Images().health_image)
        if len(news.healthNews)==0:
            news.get_news("health",news.healthNews)
            buttons=[]
            k=0
            for i in news.healthNews:
                buttons.append(CTkButton(self.healthFrame,
                                  text=i._title,
                                  fg_color="transparent",
                                  text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=None,
                                  height=40,
                                  anchor="w",
                                  font=CTkFont(size=12, weight="bold"),
                                  command=lambda i=i:self.callback(i._url)))
                buttons[k].grid(row=k,column=0,padx=5,pady=5,sticky="ew")
                k+=1
                if k==10:
                    break

    def technologyButton(self):
        self.select_frame_by_name("Technology")
        self.navigationBar_label.configure(text=" Technology",image=Images().technology_image)
        if len(news.technologyNews)==0:
            news.get_news("technology",news.technologyNews)
            buttons=[]
            k=0
            for i in news.technologyNews:
                buttons.append(CTkButton(self.technologyFrame,
                                  text=i._title,
                                  fg_color="transparent",
                                  text_color=("gray10", "gray90"),
                                  hover_color=("gray70", "gray30"),
                                  image=None,
                                  height=40,
                                  anchor="w",
                                  font=CTkFont(size=12, weight="bold"),
                                  command=lambda i=i:self.callback(i._url)))
                buttons[k].grid(row=k,column=0,padx=5,pady=5,sticky="ew")
                k+=1
                if k==10:
                    break

    def select_frame_by_name(self,name):
        self.navigationBar_button1.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
        self.navigationBar_button2.configure(fg_color=("gray75", "gray25") if name == "Business" else "transparent")
        self.navigationBar_button3.configure(fg_color=("gray75", "gray25") if name == "Entertainment" else "transparent")
        self.navigationBar_button4.configure(fg_color=("gray75", "gray25") if name == "Sports" else "transparent")
        self.navigationBar_button5.configure(fg_color=("gray75", "gray25") if name == "Science" else "transparent")
        self.navigationBar_button6.configure(fg_color=("gray75", "gray25") if name == "Health" else "transparent")
        self.navigationBar_button7.configure(fg_color=("gray75", "gray25") if name == "Technology" else "transparent")
        if name=="Home":
            self.homeFrame.grid(rowspan=5,columnspan=5,padx=5,pady=5,sticky="nsew")
        else:
            self.homeFrame.grid_forget()
        if name=="Business":
            self.businessFrame.grid(row=0,column=0,columnspan=5,padx=5,pady=5,sticky="nsew")
        else:
            self.businessFrame.grid_forget()
        if name=="Entertainment":
            self.entertainmentFrame.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        else:
            self.entertainmentFrame.grid_forget()
        if name=="Sports":
            self.sportsFrame.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        else:
            self.sportsFrame.grid_forget()
        if name=="Science":
            self.scienceFrame.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        else:
            self.scienceFrame.grid_forget()
        if name=="Health":
            self.healthFrame.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        else:
            self.healthFrame.grid_forget()
        if name=="Technology":
            self.technologyFrame.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
        else:
            self.technologyFrame.grid_forget()

    def change_appearance_mode_event(self, new_appearance_mode):
        set_appearance_mode(new_appearance_mode)

a=Window()
a.mainloop()