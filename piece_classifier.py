import torch
import torchvision.transforms as T
from PIL import Image

CLASSES = [
    "empty",
    "wp", "wn", "wb", "wr", "wq", "wk",
    "bp", "bn", "bb", "br", "bq", "bk"
]


class PieceClassifier:

    def __init__(self, model_path):
        self.model = torch.load(model_path, map_location="cpu")
        self.model.eval()

        self.transform = T.Compose([
            T.Resize((64, 64)),
            T.ToTensor(),
        ])

    def predict(self, square_img):
        pil = Image.fromarray(square_img)

        tensor = self.transform(pil).unsqueeze(0)

        with torch.no_grad():
            out = self.model(tensor)

        pred = out.argmax(dim=1).item()

        return CLASSES[pred]