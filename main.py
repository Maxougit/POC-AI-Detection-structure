import textdetectionmodel
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
    texte = "Pas un exemple de texte généré par une IA"
    result = textdetectionmodel.test_model(texte)
    hash_texte = hashlib.sha256(texte.encode()).hexdigest()
    
    if result == "humain":
        print("Certified humain: ", texte, hash_texte)
    else:
        print("Certified IA: ", texte, hash_texte)
    
    generate_certificate(texte, result, hash_texte)

if __name__ == "__main__":
    main()
