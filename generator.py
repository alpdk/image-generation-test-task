import os

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO


class InteriorGenerator:
    def __init__(self, args):
        """
        Constructor

        Parameters:
            args (argparse.Namespace): namespace containing seed, model_name, and gemini api key

        Attributes:
            seed (int): seed for random generator
            model_name (str): name of the gemini model
            api_key (str): api key for the model
        """
        self.seed = args.seed
        self.model_name = args.model_name
        self.client = genai.Client(api_key=args.gemini_api_key)

    def extract_style_from_image(self, image_name):
        """
        Method fot extracting information about furniture from the image

        Parameters:
            image_name (str): name of the image from the 'images' directory

        Returns:
             res (str): string containing the extracted information
        """
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, f"images/furniture/{image_name}")

        image = Image.open(path)

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=["Опиши стиль и дизайн мебели на изображении.", image],
            config=types.GenerateContentConfig(
                response_modalities=['Text'],
                seed=self.seed
            )
        )

        res = response.text.strip()

        return res

    def generate_interior(self, room_description, furniture_style):
        """
        Method fot generating image of the room interior with respect to the furniture style and room description

        Parameters:
            room_description (str): name of the file with the room description from 'room_description' directory
            furniture_style (str): furniture style description

        Returns:
             res (str): string containing the full room description
        """
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, f"room_descriptions/{room_description}")

        file = open(path)
        description = file.read()

        prompt = f"Сгенерируй описание интерьера комнаты на основе описания комнаты: {description}, и на основе стиля мебели: {furniture_style}"

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=['Text'],
                seed=self.seed
            )
        )

        res = response.text.strip()

        return res

    def generate_image_prompt(self, full_description, res_image_name="test.jpg"):
        prompt = f"Создай реалистичное изображение интерьера комнаты. {full_description}"

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image'],
                seed=self.seed
            )
        )

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, f"images/generated/{res_image_name}")

        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO((part.inline_data.data)))
                image.save(path)
