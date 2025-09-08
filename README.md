Det här projektet är en liten automatiserad maskininlärningsservice i python.
Den skapar en databas och tränar en maskininlärningsalgoritm på den. Databasen uppdateras och växer sedan automatiskt, varvid nya modeller tränas allt eftersom databasen växer.

**database_utils.py** skapar en databas innehållande heltal och en beteckning för om talet är udda eller jämnt. Databasen sparas med namnet data.db.

**model_utils.py** skapar en klassificeringsmodell som genom att tränas på databasen lär sig att klassificerar heltal som udda eller jämna.

**main.py** kör de ovanstående scripten med ett tidsintervall, så att ny data läggs till i databasen och en ny klassificeringsmodell tränas med 60 sekunders mellanrum. Modellerna sparas i en mapp med namnet model_registry.
