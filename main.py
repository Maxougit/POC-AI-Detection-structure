import textdetectionmodel
from IAGeneration import Creator, Detector
import picturegeneration
import hashlib
import datetime
import watermark
import unittest
import time

def generate_certificate(texte, result, hash_texte):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    certificat = f"""
    Certificat d'Authenticité
    -------------------------
    Content: {texte}
    Classification: {result}
    Hash: {hash_texte}
    Timestamp: {timestamp}
    """
    print(certificat)

def TextFinderV1(texte):
    # ---------- FIRST SOLUTION WITH A TRAINDED MODEL ----------
    start_time = time.time()
    result = textdetectionmodel.test_model(texte)
    hash_texte = hashlib.sha256(texte.encode()).hexdigest()
    end_time = time.time()
    execution_time = end_time - start_time
    
    if result == "humain":
        print("Certified humain: ", texte, hash_texte)
    else:
        print("Certified IA: ", texte, hash_texte)
    
    generate_certificate(texte, result, hash_texte)
    print("Execution time: ", execution_time)

def TextFinderV2(texte):
     # ---------- SECOND SOLUTION WITH OLLAMA API ----------
    start_time = time.time()
    result = Detector(texte)
    hash_texte = hashlib.sha256(texte.encode()).hexdigest()
    end_time = time.time()
    execution_time = end_time - start_time
    
    # print("Result: ", result)
    
    if result == "HUMAN":
        print("Certified humain: ", texte, hash_texte)
    else:
        print("Certified IA: ", texte, hash_texte)
    
    generate_certificate(texte, result, hash_texte)
    print("Execution time: ", execution_time)

def PictureGenerator(prompt):
    # ---------- PICTURE GENERATION ----------
    picture = picturegeneration.GeneratePicture(prompt)

def PictureAIorNot(picture):
    # ---------- PICTURE DETECTOR ----------
    result = watermark.watermark_decoder(picture)

    if result == "abcd":
        classification = "IA"
    else:
        classification = "HUMAN"

    hash_picture = hashlib.sha256(picture.encode()).hexdigest()
    generate_certificate(picture, classification, hash_picture)

class TestIAGeneration(unittest.TestCase):
    def test_detector(self):
        false_positives = 0
        erreur = 0
        num_tests = 10

        for _ in range(num_tests):
            # Generate a text with Creator
            text = Creator()

            # Test if Detector correctly identifies the text as AI-generated
            detect = Detector(text)
            if  detect!= "AI":
                false_positives += 1
            elif detect != "unknown":
                erreur += 1

        false_positive_rate = (false_positives / num_tests) * 100
        print(f"False positive rate: {false_positive_rate}%")

    def test_text_detector(self):
        false_positives = 0
        num_tests = 10

        for _ in range(num_tests):
            # Generate an image with Creator
            image = picturegeneration.GeneratePicture("Red bike in the forest")

            detect = watermark.watermark_decoder(image)
            if  detect != "abcd":
                false_positives += 1

        false_positive_rate = (false_positives / num_tests) * 100
        print(f"False positive rate: {false_positive_rate}%")


def main():
    print("------------------------------------------------------------ Example 1 ------------------------------------------------------------")
    # Une personne veut publier le texte sur un réseau social
    texte =  "In this article, we propose an innovative system aimed at certifying the authenticity and origin of online content, particularly regarding the distinction between content generated by artificial intelligence (AI) and human-created content. Our approach relies on the use of two distinct AI models developed by a trusted third party, which enable the placement of marks on content and their reliable recognition. One of these models is designed to integrate invisible or visible markings, such as steganography for sound and watermarks for images, into AI-generated content. When a user publishes content online, digital platforms such as social networks are prompted to request certification from a trusted authority, tasked with verifying the authenticity of the content and assigning a label indicating whether it was generated by AI or not. This trusted authority operates based on principles similar to those of certification authorities in the HTTPS protocol, thus ensuring the reliability and integrity of the certification process. However, our proposal poses significant challenges, including the mandatory adoption of the system by online platforms and companies marketing AI technologies. Additionally, we must address potential risks associated with errors in judgment by the certification authority and attempts at manipulation aimed at erasing markings. We address these challenges and discuss possible strategies for overcoming these obstacles in the context of an ever-evolving digital ecosystem."
    # Analyse du texte par le certifier
    TextFinderV1(texte) 
    TextFinderV2(texte)
    # Un certificat est généré et le texte est publié

    print("------------------------------------------------------------ Example 2 ------------------------------------------------------------")
    # Une personne veut publier le texte sur un réseau social
    texte =  Creator()
    print("Texte généré: ", texte)
    # Analyse du texte par le certifier
    TextFinderV2(texte)
    # Un certificat est généré et le texte est publié

    print("------------------------------------------------------------ Example 3 ------------------------------------------------------------")
    # Une personne veut publier une image qu'il a générer via une IA
    picturegeneration.GeneratePicture("Selfie on the moon")
    # Analyse de l'image par le certifier
    PictureAIorNot("Selfie on the moon.png") 
    # Un certificat est généré et l'image est publiée


    

if __name__ == "__main__":
    # main()
    # unittest.main()
    PictureAIorNot("difference_highlighted.png") 

