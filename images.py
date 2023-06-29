import os,customtkinter
from PIL import Image
class Images:
    def __init__(self):
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "home_dark.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "home_light.png")), size=(20, 20))

        self.business_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "dollar.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "dollar.png")), size=(20, 20))
        self.entertainment_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "popcorn.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "popcorn.png")), size=(20, 20))
        self.sports_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "ball.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "ball.png")), size=(20, 20))
        self.science_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "science.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "science.png")), size=(20, 20))
        self.health_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "health.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "health.png")), size=(20, 20))
        self.technology_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "technology.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "technology.png")), size=(20, 20))
        self.euro_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "euro.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "euro.png")), size=(50, 50))
        self.gbp_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "gbp.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "gbp.png")), size=(50, 50))
        self.chf_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "chf.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "chf.png")), size=(50, 50))
        self.jpy_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "jpy.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "jpy.png")), size=(50, 50))
        self.rub_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "rub.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "rub.png")), size=(50, 50))
        self.try_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "try.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "try.png")), size=(50, 50))
        
        self.currencies_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "currencies.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "currencies.png")), size=(100, 100))