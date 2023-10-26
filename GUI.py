import customtkinter
from wallet_crypto import *

class Data(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        refresh(date, name, symbol, price, percent_change_24h, percent_change_7d)
        for i in range(len(name)):
            self.label = customtkinter.CTkLabel(self, text=name[i], text_color='darkviolet')
            self.label.grid(row=i, column=0)
            
            self.label = customtkinter.CTkLabel(self, text=f'{price[i]} USD', text_color='white')
            self.label.grid(row=i, column=1, padx=20)
            
            if percent_change_7d[i] < 0.00:
                self.label = customtkinter.CTkLabel(self, text=f'{percent_change_7d[i]}% /7J', text_color='red')
                self.label.grid(row=i, column=2, padx=20)
            else:
                self.label = customtkinter.CTkLabel(self, text=f'{percent_change_7d[i]}% /7J', text_color='green')
                self.label.grid(row=i, column=2, padx=20)
            
            if percent_change_24h[i] < 0.00:
                self.label = customtkinter.CTkLabel(self, text=f'{percent_change_24h[i]}% /24H', text_color='red')
                self.label.grid(row=i, column=3)
            else:
                self.label = customtkinter.CTkLabel(self, text=f'{percent_change_24h[i]}% /24H', text_color='green')
                self.label.grid(row=i, column=3)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
                      
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        
        def button_callback():
            app.destroy()
        button = customtkinter.CTkButton(master=self, text="Exit", command=button_callback)
        button.grid(row=0, column=0)

        self.data = Data(master=self, width=500, height=500)
        self.data.grid(row=1, column=0, padx=20, pady=20)
        

        
app = App()
app.title("Wallet Crypto")
app.mainloop()
