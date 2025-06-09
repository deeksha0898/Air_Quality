from models.air_quality import AirQualityRecord
from datetime import datetime
from sqlalchemy.exc import IntegrityError

class AirQualityLoader:
    def __init__(self, session):
        self.session = session

    def save_data(self, data):
        results = data.get("results", [])
        if not results:
            print("No results returned from API.")
            return

        print("Received {len(results)} measurement(s)")
        inserted_count = 0

        for measurement in results:
            try:
                date_utc = datetime.fromisoformat(measurement["datetime"]["utc"].replace("Z", "+00:00"))
                record = AirQualityRecord(
                    location=str(measurement.get("locationsId")),
                    country="N/A",
                    parameter="pm25",
                    value=measurement.get("value"),
                    unit="\u00b5g/m\u00b3",
                    date_utc=date_utc,
                )
                self.session.add(record)
                inserted_count += 1
            except IntegrityError:
                self.session.rollback()
            except Exception as e:
                print(f"Skipping record due to error: {e}")

        self.session.commit()
        print(f"Committed {inserted_count} new record(s)")