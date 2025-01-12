# Readme Dokumentation

Stable Diffusion Text-to-Image Verwendung mit Grundlage von Controlnet

Sampling method/Schedulers: Methode Art und Weise wird zur Generierung der Daten

Model: Trainiertes Model zum erstellen der AI Kunst

Parameter:
- [ ] prompt: Eingabe von Text, Beschreibung zum Generieren der gewollten Sachen im Bild
- [ ] negativ prompt: Keywords, die nicht im Bild vorkommen sollen
- [ ] enhance prompt: verstärkt Prompts für bessere Bilder 
- [ ] auto hint: nutzt Hinweise um Bilder zu Generierung
- [ ] height & width: max 1024x1024 
- [ ] seed: Wert der Zufallsgenerator übergeben wird um Bilder zu erstellen, der selbe Seed gibt das selbe Bild immer aus
- [ ] samples: Anzahl der zu generierenden Bildern insgesamt max 4
- [ ] batch count: Anzahl der generierung
- [ ] batch size: Anzahl Bilder die in einen Batch generiert werden
- [ ] prompt strenght: Stärker wie sehr das Prompt Einfluss nimmt
- [ ] controlnet weight/controlnet scale: Je höher der Wert desto mehr hat Controlnet Einfluss auf das Bild und behaltet die Strukturinformationen
- [ ] starting control step: Startpunkt wann Control net anfängt zu wirken
- [ ] ending control step: Endpunkt wann control net aufhört zu wirken
- [ ] num inference steps: Anzahl der Iterationen um Bild zu verbessern/entrauschen
- [ ] clip skip: Überspirngen von Verarbeitungsstufen, 1 keine Ebene wird übersprungen bis 8
- [ ] safety checker: Scannt ob es fsk 18 ist, wenn ja dann wird ein weißes Bild angezeigt

# Anleitungsbeispiel zur Erstellung der QR-Code Kunst:

Checkpoint:
Sampling method: DPM++ 2M Karras

Model: controlnet model auswählen z.B. QR Code Monster

- [ ] Prompt: Nature, Water, Plants, Good Quality
- [ ] Negative Prompt: Blurry, People, ugly
- [ ] auto hint: yes
- [ ] enhance prompt: yes
- [ ] height & width: 512 x 512
- [ ] seed: 0 zufällige Seednummer
- [ ] samples: 4
- [ ] batch count: 2
- [ ] batch size: 2
- [ ] prompt strenght: 0,5
- [ ] controlnet weight/controlnet scale: 1.0 
- [ ] starting control step: 0,3
- [ ] ending control step: 1
- [ ] num inference steps: 30
- [ ] clip skip: 1
- [ ] safety checker: yes
