import textdetectionmodel
import IAGeneration
import hashlib
import datetime

def generate_certificate(texte, result, hash_texte):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    certificat = f"""
    Certificat d'Authenticité
    -------------------------
    Texte: {texte}
    Classification: {result}
    Hash: {hash_texte}
    Timestamp: {timestamp}
    """
    print(certificat)

def main():
    # ---------- FIRST SOLUTION WITH A TRAINDED MODEL ----------
    # texte = "Un exemple de texte généré par une IA"
    texte =  "In this article, we propose an innovative system aimed at certifying the authenticity and origin of online content, particularly regarding the distinction between content generated by artificial intelligence (AI) and human-created content. Our approach relies on the use of two distinct AI models developed by a trusted third party, which enable the placement of marks on content and their reliable recognition. One of these models is designed to integrate invisible or visible markings, such as steganography for sound and watermarks for images, into AI-generated content. When a user publishes content online, digital platforms such as social networks are prompted to request certification from a trusted authority, tasked with verifying the authenticity of the content and assigning a label indicating whether it was generated by AI or not. This trusted authority operates based on principles similar to those of certification authorities in the HTTPS protocol, thus ensuring the reliability and integrity of the certification process. However, our proposal poses significant challenges, including the mandatory adoption of the system by online platforms and companies marketing AI technologies. Additionally, we must address potential risks associated with errors in judgment by the certification authority and attempts at manipulation aimed at erasing markings. We address these challenges and discuss possible strategies for overcoming these obstacles in the context of an ever-evolving digital ecosystem."
    result = textdetectionmodel.test_model(texte)
    hash_texte = hashlib.sha256(texte.encode()).hexdigest()
    
    if result == "humain":
        print("Certified humain: ", texte, hash_texte)
    else:
        print("Certified IA: ", texte, hash_texte)
    
    generate_certificate(texte, result, hash_texte)

    # ---------- SECOND SOLUTION WITH OLLAMA API ----------
    # texte = IAGeneration.Creator()
    # texte =  "In this article, we propose an innovative system aimed at certifying the authenticity and origin of online content, particularly regarding the distinction between content generated by artificial intelligence (AI) and human-created content. Our approach relies on the use of two distinct AI models developed by a trusted third party, which enable the placement of marks on content and their reliable recognition. One of these models is designed to integrate invisible or visible markings, such as steganography for sound and watermarks for images, into AI-generated content. When a user publishes content online, digital platforms such as social networks are prompted to request certification from a trusted authority, tasked with verifying the authenticity of the content and assigning a label indicating whether it was generated by AI or not. This trusted authority operates based on principles similar to those of certification authorities in the HTTPS protocol, thus ensuring the reliability and integrity of the certification process. However, our proposal poses significant challenges, including the mandatory adoption of the system by online platforms and companies marketing AI technologies. Additionally, we must address potential risks associated with errors in judgment by the certification authority and attempts at manipulation aimed at erasing markings. We address these challenges and discuss possible strategies for overcoming these obstacles in the context of an ever-evolving digital ecosystem."

    print("---------")
    result = IAGeneration.Detector(texte)
    print("Result: ", result)

    hash_texte = hashlib.sha256(texte.encode()).hexdigest()

    # if result == "HUMAN":
    #     print("Certified humain: ", texte, hash_texte)
    # else:
    #     print("Certified IA: ", texte, hash_texte)
    
    # generate_certificate(texte, result, hash_texte)

if __name__ == "__main__":
    main()
