from diffusers import StableDiffusionPipeline
import watermark
import torch

def GeneratePicture(prompt):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("mps")

    image = pipe(prompt).images[0]  
    image.save(prompt+"nowatermark.png")
    image.save(prompt+".png")
    watermark.watermark_image(prompt+".png")
    return prompt+".png"

