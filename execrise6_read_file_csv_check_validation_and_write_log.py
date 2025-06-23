import csv
import os
import logging
import re
from datetime import datetime

EVN = os.getenv("ENVIRONMENT","development")

logging.basicConfig(
    filename="process.log",
    level=logging.DEBUG if EVN == "development" else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PHONE_REGEX = re.compile(r'^\+?[0-9]{1,3}?[-.\s]?([0-9]{1,4}[-.\s]?){1,3}[0-9]{1,4}$')
VALID_STATUSES = {"pending", "completed", "failed"}

def validate_row(row:dict, line_number:int) -> bool:
    try:
        if not row["candidate_id"].strip():
            raise ValueError("Candidate ID is required")
        if not row["name"].strip():
            raise ValueError("Name is required")
        if not EMAIL_REGEX.match(row["email"]):
            raise ValueError("Invalid email address")
        if not PHONE_REGEX.match(row["phone"]):
            raise ValueError("Invalid phone number")
        score = int(row["test_score"])
        if score < 0 or score > 100:
            raise ValueError("Test score must be between 0 and 100")
        datetime.strptime(row["test_date"], "%Y-%m-%d")
        if row["status"] not in VALID_STATUSES:
            raise ValueError("Invalid test status")
        return True
    except Exception as e:
        logging.error(f"[{line_number}] {e}")
        print(f"[{line_number}] {e}")
        return False

def process_row(file_part:str):
    success_count = 0
    error_count = 0
    time_start = datetime.now()
    logging.info(f"Processing {file_part}")
    with open(file_part,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i,row in enumerate(csv_reader):
            if validate_row(row, i):
                success_count += 1
            else:
                error_count += 1

    time_end = datetime.now()
    total_time = (time_end - time_start).total_seconds()

    logging.info(f"Processed {file_part}")
    logging.info(f"Time Start: {time_start}")
    logging.info(f"Time End: {time_end}")
    logging.info(f"Total Time: {total_time}")
    logging.info(f"Success Count: {success_count}")
    logging.error(f"Error Count: {error_count}")
    print(f"Success Count: {success_count}")
    print(f"Error Count: {error_count}")

if __name__ == "__main__":
    process_row("candidates.csv")