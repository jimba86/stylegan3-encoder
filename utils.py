import os
import torch
import matplotlib.pyplot as plt

def image2tensor(image):
    image = torch.FloatTensor(image).permute(2,0,1).unsqueeze(0)/255.
    return (image-0.5)/0.5

def tensor2image(tensor):
    tensor = tensor.clamp_(-1., 1.).detach().squeeze().permute(1,2,0).cpu().numpy()
    return tensor*0.5 + 0.5

def imshow(img, size=5, cmap='jet'):
    plt.figure(figsize=(size*3,size))
    plt.imshow(img, cmap=cmap)
    plt.axis('off')
    plt.show()
    
def save_image(img, size=5, out='output.png' , cmap='jet'):
    plt.figure(figsize=(size*3,size))
    plt.imshow(img, cmap=cmap)
    plt.axis('off')
    plt.savefig(out, dpi=300)

# Download pretrained models
google_drive_paths = {
    "encoder-250k.pt" : "https://drive.google.com/uc?id=17mwABMONSQfTj2fpgiFdAPd6giXAGBi3",
    "jugyeong-30k.pt" : "https://drive.google.com/uc?id=1ROTZDv0HaHS-brbkghh7tKD8PurLtDR1",
}

def download_pretrained_model(file=''):

    if not os.path.isdir('checkpoints'):
        os.makedirs('checkpoints')

    from gdown import download as drive_download

    url = google_drive_paths[file]
    networkfile = os.path.join('checkpoints', file)

    drive_download(url, networkfile, quiet=False)