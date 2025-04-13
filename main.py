# ----------------------------
# Importation dyal les libraries
# ----------------------------
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from datetime import datetime
import os

# ----------------------------
# Variables principales
# ----------------------------
nom_fichier = "facture_pro.pdf"  # Ism dyal fichier PDF
nom_societe = "VOTRE ENTREPRISE"
adresse_societe = "123 Rue Principale, Casablanca"
tel_societe = "+212 6 12 34 56 78"
email_societe = "contact@entreprise.com"

nom_client = "Mr Client Important"    # Ism dyal client
adresse_client = "45 Avenue des Fleurs, Rabat"
date_facture = datetime.now().strftime('%d/%m/%Y')
num_facture = "FAC-2023-001"

produits = [                 # Liste dyal produits
    {"nom": "T-shirt Premium", "prix": 250, "quantite": 2, "description": "T-shirt en coton bio"},
    {"nom": "Jeans Designer", "prix": 450, "quantite": 1, "description": "Jeans slim fit"},
    {"nom": "Casquette Logo", "prix": 120, "quantite": 3, "description": "Casquette brodée"},
]
total = sum(item["prix"] * item["quantite"] for item in produits)  # Somme totale

# Chemin dyal logo (modifier bach yt7aqq l chemin dyal logo dyalek)
logo_path = "logo.png" if os.path.exists("logo.png") else None

# ----------------------------
# Function bach nswbo facture profesionnelle
# ----------------------------
def generer_facture_pro(nom_fichier, client, adresse_client, produits, total):
    try:
        # Dimensions
        largeur, hauteur = A4
        marge = 2*cm
        
        # N9ado PDF
        c = canvas.Canvas(nom_fichier, pagesize=A4)
        
        # Ajouter logo
        if logo_path:
            c.drawImage(logo_path, marge, hauteur-2.5*cm, width=4*cm, height=2*cm, preserveAspectRatio=True)
        
        # Info société
        c.setFont("Helvetica-Bold", 12)
        c.drawString(marge, hauteur-3.5*cm, nom_societe)
        c.setFont("Helvetica", 10)
        c.drawString(marge, hauteur-4*cm, adresse_societe)
        c.drawString(marge, hauteur-4.5*cm, tel_societe)
        c.drawString(marge, hauteur-5*cm, email_societe)
        
        # Titre dyal facture
        c.setFont("Helvetica-Bold", 16)
        c.drawRightString(largeur-marge, hauteur-2.5*cm, "FACTURE")
        c.setFont("Helvetica-Bold", 12)
        c.drawRightString(largeur-marge, hauteur-3*cm, f"N°: {num_facture}")
        c.drawRightString(largeur-marge, hauteur-3.5*cm, f"Date: {date_facture}")
        
        # Info client
        c.setFont("Helvetica-Bold", 12)
        c.drawString(marge, hauteur-6*cm, "Client:")
        c.setFont("Helvetica", 10)
        c.drawString(marge, hauteur-6.5*cm, nom_client)
        c.drawString(marge, hauteur-7*cm, adresse_client)
        
        # Ligne separator
        c.line(marge, hauteur-7.5*cm, largeur-marge, hauteur-7.5*cm)
        
        # Tableau dyal produits
        data = [["Produit", "Description", "Quantité", "Prix unitaire", "Total"]]
        
        for item in produits:
            data.append([
                item["nom"],
                item["description"],
                str(item["quantite"]),
                f"{item['prix']} DH",
                f"{item['prix'] * item['quantite']} DH"
            ])
        
        # Ajouter total
        data.append(["", "", "", "TOTAL:", f"{total} DH"])
        
        # Création tableau
        table = Table(data, colWidths=[3*cm, 6*cm, 2*cm, 3*cm, 3*cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2C3E50")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 10),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-2), colors.HexColor("#ECF0F1")),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#BDC3C7")),
            ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
            ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#F39C12")),
        ]))
        
        # Position tableau
        table.wrapOn(c, largeur-2*marge, hauteur)
        table.drawOn(c, marge, hauteur-14*cm)
        
        # Conditions de paiement
        styles = getSampleStyleSheet()
        styleN = styles["Normal"]
        styleN.alignment = 1  # Centré
        
        conditions = Paragraph(
            "<b>Conditions de paiement:</b> Paiement à réception de facture. Tout retard de paiement entraînera des pénalités de 1,5% par mois.",
            styleN
        )
        conditions.wrapOn(c, largeur-2*marge, hauteur)
        conditions.drawOn(c, marge, 3*cm)
        
        # Signature
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(marge, 2*cm, "Le responsable")
        c.line(marge, 1.8*cm, marge+4*cm, 1.8*cm)
        
        # Sauvegarde dyal PDF
        c.save()
        print(f"✅ Facture professionnelle '{nom_fichier}' mnsaba b najah!")
    except Exception as e:
        print(f"❌ Error f génération: {e}")

# ----------------------------
# Appel dyal function
# ----------------------------
generer_facture_pro(nom_fichier, nom_client, adresse_client, produits, total)