import database_utils
import model_utils
import time

# Loop där databasen skapas, data läggs till, modellen tränas...
interval_in_seconds = 60

def main(interval_in_seconds):
    """
    Huvudfunktion som skapar en databas och tränar en modell på den.
    Mer data skapas och läggs till och modellen tränas om i ett enminutsintervall.
    """
    version = 1
    batch = 0
    database_utils.make_database()

    while True:
        new_data = database_utils.generate_data(batch*10, n=10)
        print(new_data.describe)
        database_utils.insert_data(new_data)
        model_utils.train_and_save_model(version)
        print(f"Batch {batch+1} klar, (modell v{version} sparad)")

        version += 1
        batch += 1

        time.sleep(interval_in_seconds)

if __name__ == "__main__":
    main()