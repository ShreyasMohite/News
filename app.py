from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox
import requests
import json



class News:
    def __init__(self,root): 
        self.root=root
        self.root.title("News room")
        self.root.geometry("700x550")
        self.root.resizable(0,0)

        search_items=StringVar()
        country=StringVar()
        categories=StringVar()
        lang=StringVar()



        def search_by_country_name():
            try:
                if country.get()!="Select Country":
                    with open("C:/TEMP/news.json","w",encoding='utf-8') as f:



                        url='https://newsapi.org/v2/top-headlines?country={}&apiKey=yourapikey'.format(country.get())
                        response = requests.get(url)
                        news=response.json()
                        get_news=json.dumps(news,indent=4)
                        f.write(get_news)
                    with open("C:/TEMP/news.json",'r',encoding='utf-8') as f:
                        text.insert('end',f.read())

                else:
                    tkinter.messagebox.showerror("Error","Please Select A Country")
            except Exception as e:
                tkinter.messagebox.showerror('ERROR',"No Internet Conncetion")        




        def search_by_category():
            try:
                if country.get()!="Select Country":

                    if categories.get()!="Select Categories":
                        with open("C:/TEMP/news.json","w",encoding='utf-8') as f:

                            url='https://newsapi.org/v2/top-headlines?country={0}&category={1}&apiKey=yourapikey'.format(country.get(),categories.get())
                            response = requests.get(url)
                            news=response.json()
                            get_news=json.dumps(news,indent=4)
                            f.write(get_news) 
                        with open("C:/TEMP/news.json",'r',encoding='utf-8') as f:
                            text.insert('end',f.read())                   
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Categories")

                else:
                    tkinter.messagebox.showerror("Error","Please Select A Country")
            except Exception as e:
                tkinter.messagebox.showerror('ERROR',"No Internet Conncetion")        


        def search():
            try:
                if search_items.get()!="":
                    with open("C:/TEMP/news.json","w",encoding='utf-8') as f:

                        url='https://newsapi.org/v2/top-headlines?q={}&apiKey=yourapikey'.format(search_items.get())
                        response = requests.get(url)
                        news=response.json()
                        get_news=json.dumps(news,indent=4)
                        f.write(get_news) 
                    with open("C:/TEMP/news.json",'r',encoding='utf-8') as f:
                            text.insert('end',f.read()) 
                else:
                    tkinter.messagebox.showerror("Error","Please Entry Something on search Bar")
                
            except expression as e:
                tkinter.messagebox.showerror('ERROR',"No Internet Conncetion")        


        def sources():
            try:
                with open("C:/TEMP/news.json","w",encoding='utf-8') as f:

            
                    url='https://newsapi.org/v2/sources?apiKey=yourapikey'
                    response = requests.get(url)
                    news=response.json()
                    get_news=json.dumps(news,indent=4)
                    f.write(get_news) 
                with open("C:/TEMP/news.json",'r',encoding='utf-8') as f:
                    text.insert('end',f.read()) 
            
            except expression as e:
                tkinter.messagebox.showerror('ERROR',"No Internet Conncetion")        

        def sources_country():
            try: 
                if lang.get()!="Select Languages":
                    if country.get()!="Select Country":
                        with open("C:/TEMP/news.json","w",encoding='utf-8') as f:

                            url='https://newsapi.org/v2/sources?language={0}&country={1}&apiKey=yourapikey'.format(lang.get(),country.get())
                            response = requests.get(url)
                            news=response.json()
                            get_news=json.dumps(news,indent=4)
                            f.write(get_news) 
                        with open("C:/TEMP/news.json",'r',encoding='utf-8') as f:
                            text.insert('end',f.read()) 
                       
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Country")
                else:
                    tkinter.messagebox.showerror("Error","Please Select Language")
            except Exception as e:
                tkinter.messagebox.showerror('ERROR',"No Internet Conncetion")        
        




        def clear():
            search_items.set("")
            country.set("Select Country")
            categories.set("Select Categories")
            lang.set("Select Languages")
            text.delete('1.0','end')




        def on_enter1(e):
            but_search['background']="black"
            but_search['foreground']="cyan"
  
        def on_leave1(e):
            but_search['background']="SystemButtonFace"
            but_search['foreground']="SystemButtonText"


        def on_enter4(e):
            but_search_coun['background']="black"
            but_search_coun['foreground']="cyan"
  
        def on_leave4(e):
            but_search_coun['background']="SystemButtonFace"
            but_search_coun['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def on_enter3(e):
            but_search_coun_cate['background']="black"
            but_search_coun_cate['foreground']="cyan"
  
        def on_leave3(e):
            but_search_coun_cate['background']="SystemButtonFace"
            but_search_coun_cate['foreground']="SystemButtonText"


        def on_enter5(e):
            but_sources['background']="black"
            but_sources['foreground']="cyan"
  
        def on_leave5(e):
            but_sources['background']="SystemButtonFace"
            but_sources['foreground']="SystemButtonText"

        def on_enter6(e):
            but_sources_country['background']="black"
            but_sources_country['foreground']="cyan"
  
        def on_leave6(e):
            but_sources_country['background']="SystemButtonFace"
            but_sources_country['foreground']="SystemButtonText"
        
        
        


    #=========Frame======================
        Main_Frame=Frame(self.root,relief=RIDGE,width=700,height=550,bd=2,bg="#8080ff")
        Main_Frame.place(x=0,y=0)

        Frame_top=Frame(Main_Frame,width=695,height=300,relief=RIDGE,bd=2)
        Frame_top.place(x=0,y=0)

        Frame_bottom=Frame(Main_Frame,width=695,height=245,relief=RIDGE,bd=2)
        Frame_bottom.place(x=0,y=300)
    #=========================Lab_top==================
     
        lab_top=LabelFrame(Frame_top,width=690,height=294,text="Search News")
        lab_top.place(x=0,y=0)

        lab_search=Label(lab_top,text="Search",font=('times new roman',12))
        lab_search.place(x=10,y=10)
    

        Ent_search=Entry(lab_top,width=28,font=('times new roman',13,'bold'),bd=3,textvariable=search_items)
        Ent_search.place(x=70,y=10)


        country_list=['ae' ,'ar' ,'at' ,'au','be', 'bg', 'br', 'ca', 'ch',\
                      'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr',\
                      'hk', 'hu', 'id', 'ie','il', 'in', 'it', 'jp', 'kr', \
                      'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz',\
                      'ph', 'pl', 'pt', 'ro','rs', 'ru', 'sa', 'se', 'sg',\
                      'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've' ,'za']
        country_combo=Combobox(lab_top,values=country_list,font=('arial',14),width=20,state="readonly",textvariable=country)
        country_combo.set("Select Country")
        country_combo.place(x=400,y=10)


        category_list=['business','entertainment','general','health','science','sports','technology']
        categories_combo=Combobox(lab_top,values=category_list,font=('arial',14),width=20,state="readonly",textvariable=categories)
        categories_combo.set("Select Categories")
        categories_combo.place(x=70,y=60)

        lang_list=['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh']
        lang_combo=Combobox(lab_top,values=lang_list,font=('arial',14),width=20,state="readonly",textvariable=lang)
        lang_combo.set("Select Languages")
        lang_combo.place(x=400,y=60)


        but_search=Button(lab_top,text="Search",width=16,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=search)
        but_search.place(x=20,y=200)
        but_search.bind("<Enter>",on_enter1)
        but_search.bind("<Leave>",on_leave1)

   

        but_search_coun=Button(lab_top,text="Search By Country",width=16,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=search_by_country_name)
        but_search_coun.place(x=510,y=200)#(x=510,y=200
        but_search_coun.bind("<Enter>",on_enter4)
        but_search_coun.bind("<Leave>",on_leave4)


        but_search_coun_cate=Button(lab_top,text="Search By Categories",width=16,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=search_by_category)
        but_search_coun_cate.place(x=270,y=200)#(x=510,y=200
        but_search_coun_cate.bind("<Enter>",on_enter3)
        but_search_coun_cate.bind("<Leave>",on_leave3)


        but_sources=Button(lab_top,text="All Sources",width=16,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=sources)
        but_sources.place(x=270,y=240)#(x=510,y=200
        but_sources.bind("<Enter>",on_enter5)
        but_sources.bind("<Leave>",on_leave5)

        but_sources_country=Button(lab_top,text="Sources Country",width=16,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=sources_country)
        but_sources_country.place(x=20,y=240)#(x=510,y=200
        but_sources_country.bind("<Enter>",on_enter6)
        but_sources_country.bind("<Leave>",on_leave6)





        but_clear=Button(lab_top,text="Clear",width=16,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=clear)
        but_clear.place(x=510,y=240)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


    #===========Frame_bottom==============================

        scol=Scrollbar(Frame_bottom,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(Frame_bottom,height=12,width=83,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=2)
        scol.config(command=text.yview)
        



if __name__ == "__main__":
    root=Tk()
    app=News(root)
    root.mainloop()
